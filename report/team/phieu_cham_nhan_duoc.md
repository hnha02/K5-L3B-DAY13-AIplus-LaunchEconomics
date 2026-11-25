# Phiếu chấm nhóm AIplus nhận được

Phiếu do AIplus tự soát theo ba tiêu chí của phiếu chấm hội đồng Gate 2a; hội đồng GeminiPro đã xem và đồng ý giữ nguyên điểm.

- Người soát: GeminiPro
- Hồ sơ được soát: `report/team/ho_so_launch_v0.md` của AIplus

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Go có điều kiện cho noi_dia + hang_nang khớp số (0,38× trong phạm vi, quoc_te 1,88×) [simulated]; nêu đủ con số bất lợi kèm điều kiện xử lý: xem lại 100% 0,98×–1,03× → điều kiện 1; power 0,64 → điều kiện 4; ca 7, 20 → điều kiện 3. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mục 1, 2, 3, 7 và dòng đề xuất có nhãn [simulated]; mục 4 ghi "trong đợt chạy thử"; loại quoc_te có lý do bằng số (1,88×). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 5 | Có đối chứng 20 + 20 nhân viên, phân tầng theo depot, đủ mẫu (859/nhóm, DE 6,96, m ≥ 299); nhưng mục 6 chỉ ghi "3 luật dừng", không có ngưỡng, thời hạn hay vai có quyền dừng (các chi tiết này chỉ có trong `pilot_plan.yaml`). |
| **Tổng** | | | | **25 / 30** | |

## Chỗ nên sửa trước khi trình

1. **Mục 6 thiếu chi tiết luật dừng (mất 5 điểm).** Thêm vào mục 6 bản rút gọn từ `pilot_plan.yaml`: mở lại cao hơn đối chứng ≥ 2 điểm, hoặc vượt 6%, hoặc 1 ca hoàn trùng trong 3 ngày → Giám đốc vận hành tắt trong 30 phút; chi phí mỗi việc thành công > 8.000 đ trong 2 tuần → PM thu hẹp về noi_dia; bỏ qua gợi ý > 40% trong 1 tuần → Trưởng nhóm CSKH phỏng vấn 5 nhân viên. Đây cũng chính là lý do nhóm đã trừ điểm GeminiPro.
2. **Rollout và cách chia 20 + 20.** Hồ sơ không nhắc rollout, nhưng `pilot_plan.yaml` có `[0.10, 0.25, 0.50]` (4 → 10 → 20 nhân viên, chỉ số chính chỉ đo từ bước 0,50). Nên ghi một dòng vào mục 6 để hội đồng không hỏi cùng câu nhóm đã hỏi GeminiPro.
3. **Dấu "±" ở mục 2 sai.** Theo B1 trong `bang_chi_phi.md`, giảm một nửa chỉ cho nửa mức tăng: làm lại +51,8% / −25,9%, xem lại +40,7% / −20,3%, token +5,6% / −2,8%. Nên viết "+51,8% khi gấp đôi" thay cho "±51,8%" (cùng lỗi ở `bang_chi_phi.md` dòng 73 và `group_report.md` dòng 26).
4. **Mục 7 ghi "+2.370 đ/việc cố định".** Theo A4, phí cố định mỗi việc tăng từ 1.185 đ lên 2.370 đ, tức tăng thêm 1.185 đ. Nên viết "phí cố định tăng từ 1.185 đ lên 2.370 đ/việc (4.599 → 5.784 đ, 0,48×)" [simulated].
5. **doi_tac 0,85× vẫn rẻ hơn nhân viên nhưng bị loại**, hồ sơ không nêu lý do. `pilot_plan.yaml` ghi "điều khoản riêng"; nên thêm lý do này (và tỉ lệ thành công 54,4% [simulated]) vào dòng đề xuất.
6. **Ngày bắt đầu pilot không có trong hồ sơ.** Các điều kiện ghi "trước ngày bắt đầu" nhưng chỉ `pilot_plan.yaml` có mốc 2026-12-07. Nên ghi mốc này ở mục 6 hoặc dòng đề xuất.

Nếu sửa điểm 1 (và nên sửa thêm điểm 2) ở danh sách trên, tiêu chí pilot có thể lên 10 điểm, tổng 30/30.
