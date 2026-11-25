# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: AIplus · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc trên 1.200 yêu cầu, gấp 16,3 lần hoá đơn token chia số yêu cầu [simulated]; phạm vi noi_dia + hang_nang 3.414 đ, cộng cố định 4.599 đ ở 45.000 yêu cầu/tháng [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại ±51,8% · 2. Tỉ lệ xem lại ±40,7% · 3. Lương nhân viên +23,1% (giá token chỉ ±5,6%) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Phạm vi noi_dia + hang_nang: 0,38× của 12.000 đ (0,48× nếu khối lượng còn một nửa) [simulated]; **bất lợi:** xem lại 100% lên 0,98× (1,03× với 15,3 phút làm lại) [simulated]; quoc_te 1,88× nên loại khỏi phạm vi | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử: chính 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177) · mở lại 7 ngày 4,25% (51/1.200); 10 event có `trace_id` (`chi_so.md`) | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 19/20 = 95% (lệch ca 13, thống nhất Giới hạn hệ thống); 6/20 ca là lỗi hệ thống, gồm báo "đã hoàn" khi sổ cái lỗi (ca 7) và hoàn trùng (ca 20); 5 ca khắc phục đủ năm loại (`bang_loi.md`) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, ngẫu nhiên phân tầng theo depot; 859/nhóm, DE 6,96, m ≥ 299; mde 6 điểm (**bất lợi:** power 0,64 nếu tác động thật 5 điểm); 3 luật dừng; quyết định 2027-01-08 | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi → 6.787 đ (+51,8%); xem lại 100% kéo dài → 0,98×; khối lượng còn một nửa → +2.370 đ/việc cố định [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go có điều kiện, chỉ cho pilot noi_dia + hang_nang; loại quoc_te (1,88×) và doi_tac (0,85×) [simulated].

- Điều kiện 1: có kế hoạch giảm xem lại theo bậc trước ngày bắt đầu, vì xem lại 100% cho 0,98× tức gần như không tiết kiệm [simulated]; mục tiêu mỗi lần xem lại ≤ 5 phút. Người phụ trách: Trưởng nhóm CSKH. Ngày kiểm tra: 2026-12-04, xem lại cuối bước 0,25 (2026-12-20).
- Điều kiện 2: bật đủ 10 event có `trace_id`, thay phút xem lại/làm lại simulated bằng phút đo thật sau tuần 1. Người phụ trách: Kỹ sư trưởng agent. Ngày kiểm tra: 2026-12-04 (event), 2026-12-14 (phút đo thật).
- Điều kiện 3: sửa khoá chống trùng (ca 20) và chỉ báo "đã hoàn" khi sổ cái trả ok (ca 7) trước ngày bắt đầu; đối soát mỗi giờ ngưỡng 0 ca. Người phụ trách: Kỹ sư trưởng agent. Ngày kiểm tra: 2026-12-04.
- Điều kiện 4: Giám đốc vận hành ký chấp nhận mức chênh 6 điểm (power 0,64 nếu tác động thật là 5 điểm) và mốc quyết định 2027-01-08. Người phụ trách: Giám đốc vận hành. Ngày kiểm tra: 2026-12-04.
