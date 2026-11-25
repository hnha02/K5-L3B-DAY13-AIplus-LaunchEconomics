"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # Lần chạy thứ i xảy ra khi i-1 lần trước đều sai: tổng (1-p)^(i-1), i = 1..k
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # Tử số: mọi lần chạy (kể cả lần lỗi); mẫu số: chỉ việc thành công. k triệt tiêu → 1/p.
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # Bỏ lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn → chuyển nhân viên, không xem lại/làm lại
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    token, tool = tien_token.sum(), tien_tool.sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai   # simulated
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai   # simulated
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=token, tool=tool,
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(token + tool) / len(reqs))


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    print(f"{'gap_hoa_don':12s} {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:>14.1f} lần")
    tc = ket_qua['tong']
    print(f"Tỉ trọng [simulated]: làm lại {ket_qua['lam_lai'] / tc:.1%} · xem lại {ket_qua['xem_lai'] / tc:.1%}"
          f" · giờ nhân viên {(ket_qua['lam_lai'] + ket_qua['xem_lai']) / tc:.1%}")
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong = (tc + khong_tc * BASELINE) / len(reqs)
    print(f"Chi phí cả hệ thống mỗi yêu cầu (cộng {khong_tc} ca nhân viên làm thay): "
          f"{he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× [simulated]")

    # ---------- CP1 · Nhiệm vụ A3 · theo từng loại ----------
    print('\nA3 · Theo loại yêu cầu [cps simulated]')
    print(f"{'loai':10s} {'so_yc':>6s} {'ti_le_tc':>9s} {'chay/yc':>8s} {'cps':>8s} {'so_12k':>7s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, r)
        so_chay = runs['request_id'].isin(r['request_id']).sum()
        print(f"{loai:10s} {len(r):6d} {kq['thanh_cong'] / len(r):9.1%} {so_chay / len(r):8.2f}"
              f" {kq['cps']:8,.0f} {kq['cps'] / BASELINE:6.2f}×")
    # Chạy lại có giúp không: tỉ lệ status ok theo lần thử
    ok = runs.merge(reqs[['request_id', 'loai']]).assign(ok=lambda d: d['status'] == 'ok')
    print('\nTỉ lệ ok theo lần thử (attempt):')
    print(ok.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').round(3))

    # ---------- CP1 · Nhiệm vụ A4 · chi phí cố định, phạm vi noi_dia + hang_nang ----------
    CO_DINH, YC_THANG = 40_000_000, 45_000
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    print(f"\nA4 · Phạm vi noi_dia + hang_nang: tổng {kq_pv['tong']:,.0f} đ / {kq_pv['thanh_cong']} việc"
          f" = {kq_pv['cps']:,.0f} đ [simulated]")
    for ten, yc in [('45.000 yc/tháng', YC_THANG), ('một nửa khối lượng', YC_THANG / 2)]:
        tc_thang = yc * kq_pv['thanh_cong'] / len(reqs)
        cd = CO_DINH / tc_thang
        print(f"  {ten:20s} việc TC/tháng {tc_thang:8,.0f} · cố định/việc {cd:6,.0f} đ"
              f" · cps + cố định {kq_pv['cps'] + cd:6,.0f} đ = {(kq_pv['cps'] + cd) / BASELINE:.2f}×")

    # ---------- CP2 · Nhiệm vụ B1 + B2 · độ nhạy ----------
    kich_ban = {
        'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':            dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':       dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':            dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':       dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':             dict(luong_phut=2500),
        'Tối đa 2 lần chạy':          dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':             dict(max_lan_chay=1),
        'B2: token ×2 + xem lại ×2':  dict(gia_vao=52, gia_ra=260, he_so_xem_lai=2),
    }
    goc = ket_qua['cps']
    print(f"\nB1/B2 · Độ nhạy [simulated] · gốc {goc:,.0f} đ")
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f"  {ten:28s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%")

    # ---------- CP2 · Nhiệm vụ B3 · giới hạn chạy lại, chi phí cả hệ thống ----------
    print('\nB3 · Giới hạn số lần chạy [simulated]')
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong = len(reqs) - kq['thanh_cong']
        print(f"  {k} lần: trợ lý {kq['tong']:>10,.0f} · không TC {khong:4d}"
              f" · cả hệ thống {kq['tong'] + khong * BASELINE:>10,.0f} · cps {kq['cps']:,.0f}")

    # ---------- CP2 · Nhiệm vụ B4 · xem lại 100% trong phạm vi noi_dia + hang_nang ----------
    run_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    co_ok = run_pv.loc[run_pv['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    tok_tool = (run_pv['tokens_in'] / 1000 * GIA_VAO + run_pv['tokens_out'] / 1000 * GIA_RA
                + run_pv['tool_calls'] * GIA_TOOL).sum()
    pl = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    print(f"\nB4 · Xem lại 100% ({len(pham_vi)} yc, {co_ok} có lần chạy ok, {so_lam_lai} ca làm lại,"
          f" token+tool {tok_tool:,.0f} đ) [simulated]")
    print(f"  Phút làm lại trong dữ liệu: trung bình {pl.mean():.1f}, trung vị {pl.median():.1f}")
    for phut_ll in [9, pl.mean()]:
        tong_b4 = co_ok * 5 * LUONG_PHUT + so_lam_lai * phut_ll * LUONG_PHUT + tok_tool
        cps_b4 = tong_b4 / kq_pv['thanh_cong']
        hoa_von = (BASELINE * kq_pv['thanh_cong'] - so_lam_lai * phut_ll * LUONG_PHUT - tok_tool) / (co_ok * LUONG_PHUT)
        print(f"  làm lại {phut_ll:4.1f} phút/ca: tổng {tong_b4:,.0f} đ → {cps_b4:,.0f} đ = {cps_b4 / BASELINE:.2f}×"
              f" · hoà vốn khi xem lại ≤ {hoa_von:.1f} phút")

    # ---------- E1 · Chỉ số tính thử + tỉ lệ mở lại (dùng cho luật an toàn ở D) ----------
    chinh = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    mo_lai = reqs['mo_lai_trong_7_ngay'] == 1
    print('\nE1 · Chỉ số trong đợt chạy thử')
    print(f"  Chính: {chinh.mean():.2%} ({chinh.sum()}/{len(reqs)})")
    print(f"  Dùng (bỏ qua gợi ý): {bo_qua.mean():.2%} ({bo_qua.sum()}/{len(xem)})")
    print(f"  An toàn (mở lại 7 ngày): {mo_lai.mean():.2%} ({mo_lai.sum()}/{len(reqs)});"
          f" trong phạm vi noi_dia + hang_nang {(pham_vi['mo_lai_trong_7_ngay'] == 1).mean():.2%}")
    print(f"  Tỉ lệ làm lại trong phạm vi: {so_lam_lai / len(pham_vi):.1%} ({so_lam_lai}/{len(pham_vi)})")

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
