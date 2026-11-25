# Báo cáo cá nhân — NguyenNghiemKhanhTiep-2A2020603863

## 1. Thông tin thành viên

- Họ tên: Nguyễn Nghiêm Khánh Tiệp
- MSSV: 2A2020603863
- Email: tiepnnk04@gmail.com
- Vai trong nhóm: người kiểm số (CP1–CP2), người gắn nhãn 1 (CP3), người viết code sau giải lao (CP4)

## 2. Phần việc phụ trách

- CP1–CP2: kiểm số độc lập cho A1–A4, B1–B4, đối chiếu với output `src/lab13.py` và `report/team/bang_chi_phi.md` do Hà Anh viết.
- CP3: gắn nhãn độc lập 20 ca lỗi (người gắn nhãn 1), so nhãn với người gắn nhãn 2.
- CP4: code D1 trong `src/lab13.py`, điền `report/team/pilot_plan.yaml`.
- CP5: rà soát hồ sơ trước khi gửi hội đồng (không còn `?`, không có từ cấm, đủ nhãn simulated).

## 3. Đóng góp cụ thể

- Tính lại toàn bộ A2, A3, A4, B1–B4 bằng một cách tính độc lập (gộp chi phí theo từng yêu cầu trước khi cộng). Kết quả khớp 100% với output `src/lab13.py` của Hà Anh: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu; B3 giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ [simulated]).
- Viết phần D1 trong `src/lab13.py`: hàm `co_mau`, `he_so_thiet_ke`, `m_toi_thieu`, `in_co_mau`. Kết quả: 1.251 yêu cầu mỗi nhóm; theo nhân viên m = 75 cần 42 người mỗi nhóm (84 > 40); 20 nhân viên mỗi nhóm tối đa 1.000; 6 depot tối đa 300; mức chênh 6 điểm cần m ≥ 299 (DE 6,96); nếu tác động thật chỉ 5 điểm thì power còn 0,64.
- Hoàn thiện `pilot_plan.yaml`: chia theo nhân viên 20 + 20, mde 0,06, n 859 mỗi nhóm, 20 cụm; điền identifiability theo D2 của Nhài; rollback; decision_date 2027-01-08 (bước 50% cần khoảng 10 ngày vì mỗi người có 30,7 yêu cầu trong phạm vi mỗi ngày, cộng 7 ngày chờ cửa sổ mở lại); danh sách simulated_inputs. File đọc được bằng `yaml.safe_load`, không còn dấu `?`.
- Rà soát CP5: không còn từ cấm trong `report/team/`.
- CP3: gắn nhãn độc lập 20 ca (người gắn nhãn 1), không trao đổi với Nhài trước khi so. Đồng thuận 19/20 = 95%, lệch ở ca 13.

## 4. Bằng chứng

- Commit `c69cb34`: chú thích D1 (a–e) trong `pilot_plan.yaml`, thông tin trong `TEAM.md`.
- Commit `d31806b`: phần D1 của `src/lab13.py` và các trường còn lại của `pilot_plan.yaml`.
- Commit `bd760e2`: bộ nhãn độc lập của người gắn nhãn 1 trong `report/team/bang_loi.md`, đồng thuận 19/20.
- Kết quả kiểm số khớp `report/team/bang_chi_phi.md`.

## 5. Công cụ AI đã dùng

- Claude Code: hỗ trợ viết script kiểm số độc lập cho A, B, D1, viết phần D1 trong `src/lab13.py` và điền `pilot_plan.yaml`. Tự kiểm tra bằng cách so từng con số với số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch dưới 0,1%), đối chiếu với output `src/lab13.py` của người viết code, và tính tay câu e: 20m ≥ 859 × (0,98 + 0,02m) → m ≥ 298,5 → 299.
- Không dùng AI để gắn nhãn 20 ca lỗi ở CP3.

## 6. Tự đánh giá

- **Làm tốt:** kiểm số độc lập khớp 100% với code của Hà Anh nên nhóm tin được các số A, B trước khi đưa vào hồ sơ; phần D1 chỉ ra được vì sao chia theo yêu cầu hay theo depot đều không dùng được (84 > 40 người; 6 depot chỉ có trần 300) và chọn 20 + 20 nhân viên với mức chênh 6 điểm; `pilot_plan.yaml` đủ trường, đọc được bằng `yaml.safe_load`. Nhãn CP3 tự gắn, trùng với Nhài 19/20.
- **Hiểu được:** chia theo cụm thì cỡ mẫu hiệu dụng không vượt được c / ICC, nên thêm yêu cầu cho mỗi người không cứu được khi số cụm ít (20 cụm thì trần 1.000 < 1.251); chi phí mỗi việc thành công phải tính cả lần chạy hỏng ở tử số; ca 13 là giới hạn hệ thống vì yêu cầu nằm ngoài phạm vi, còn cách trợ lý trả lời kém là việc cần sửa.
- **Chưa tốt:** dựa vào Claude Code để viết phần D1 và script kiểm số, nên phải tính tay lại câu e và đối chiếu từng số mới chắc là đúng. Mục 6 hồ sơ chỉ ghi "3 luật dừng" mà không chép ngưỡng và vai có quyền dừng từ `pilot_plan.yaml`, nhóm bị hội đồng GeminiPro trừ 5 điểm tiêu chí pilot; lúc rà soát CP5 tôi chỉ kiểm từ cấm và dấu `?` nên không phát hiện. Có xung đột `TEAM.md` khi lấy lại phần sửa cục bộ sau khi pull.
- **Lần sau:** khi rà soát, đọc hồ sơ theo đúng ba tiêu chí của phiếu chấm chứ không chỉ kiểm định dạng; tự viết công thức cỡ mẫu trước rồi mới dùng AI để soát; pull trước khi sửa file chung.
