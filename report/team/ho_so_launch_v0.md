# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: AIplus · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc trên 1.200 yêu cầu, gấp 16,3 lần hoá đơn token chia số yêu cầu [simulated]; phạm vi noi_dia + hang_nang 3.414 đ, cộng cố định 4.599 đ ở 45.000 yêu cầu/tháng [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại ±51,8% · 2. Tỉ lệ xem lại ±40,7% · 3. Lương nhân viên +23,1% (giá token chỉ ±5,6%) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Phạm vi noi_dia + hang_nang: 0,38× của 12.000 đ (0,48× nếu khối lượng còn một nửa) [simulated]; **bất lợi:** xem lại 100% lên 0,98× (1,03× với 15,3 phút làm lại) [simulated]; quoc_te 1,88× nên loại khỏi phạm vi | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử: chính 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177) · mở lại 7 ngày 4,25% (51/1.200); 10 event có `trace_id` (`chi_so.md`) | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | (chờ CP3: tỉ lệ đồng thuận .../20, 5 ca đủ năm loại) | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | (chờ CP4: cách chia, n mỗi nhóm, số cụm, mde) · 3 luật dừng an toàn/chi phí/sử dụng đã viết | Chưa | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi → 6.787 đ (+51,8%); xem lại 100% kéo dài → 0,98×; khối lượng còn một nửa → +2.370 đ/việc cố định [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất (nháp, cả nhóm chốt lúc ~16:50):** Go có điều kiện, chỉ cho pilot noi_dia + hang_nang; loại quoc_te (1,88×) và doi_tac (0,85×) [simulated].

- Điều kiện 1: có kế hoạch giảm xem lại theo bậc trước ngày bắt đầu, vì xem lại 100% cho 0,98× tức gần như không tiết kiệm [simulated]; mục tiêu mỗi lần xem lại ≤ 5 phút. Người phụ trách: Trưởng nhóm CSKH. Ngày kiểm tra: (điền).
- Điều kiện 2: bật đủ 10 event có `trace_id`, thay phút xem lại/làm lại simulated bằng phút đo thật sau tuần 1. Người phụ trách: Kỹ sư trưởng agent. Ngày kiểm tra: (điền).
- Điều kiện 3: (từ CP3, ví dụ sửa lỗi hệ thống nghiêm trọng nhất trước ngày bắt đầu). Người phụ trách: (điền). Ngày kiểm tra: (điền).
- Điều kiện 4: (từ CP4, ví dụ Giám đốc vận hành ký chấp nhận đánh đổi cỡ mẫu). Người phụ trách: Giám đốc vận hành. Ngày kiểm tra: (điền).
