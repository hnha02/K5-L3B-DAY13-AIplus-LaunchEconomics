# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Nghiêm Khánh Tiệp · Người gắn nhãn 2: Phùng Thị Nhài (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 19 / 20 = 95% (lệch duy nhất ở ca 13)

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 13 · thống nhất Giới hạn hệ thống:** yêu cầu nằm ngoài phạm vi trợ lý thì nhãn là giới hạn, kể cả khi trợ lý xử lý giới hạn đó kém (trả lời chung chung); cách trợ lý phản hồi kém là việc cần sửa, ghi ở cột khắc phục, không đổi nhãn gốc.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (lý do = mã không hợp lệ), đếm theo ngày; cảnh báo khi vượt 2% số yêu cầu/ngày | Nhận diện mẫu mã đơn sàn TMĐT và tự tra sang mã vận đơn; không tra được thì hiện hướng dẫn kèm ảnh chỉ chỗ lấy mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" không có bản ghi `refund_ledger_write` ket_qua = ok cùng `trace_id`; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo "đang xử lý" và chuyển nhân viên (`handoff_to_staff`) | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo tuần: tỉ lệ `ticket_reopened` có reason = "hoàn thiếu" mà kiểm tra lại thấy số tiền đúng; cảnh báo khi > 1% số yêu cầu đã đóng | Mẫu tin nhắn luôn ghi cách tính, ví dụ "30.000 đ × 50% = 15.000 đ", kèm điều khoản áp dụng | Trưởng nhóm CSKH |
| 13 | Giới hạn hệ thống | Event `handoff_to_staff` với reason = ngoai_pham_vi, đếm theo tuần và theo chủ đề; rà 20 hội thoại/tuần có chủ đề ngoài phạm vi mà không có handoff | Thêm bộ nhận diện chủ đề ngoài phạm vi (bảo hiểm hàng hoá): trả lời rõ "trợ lý không xử lý được", đưa kênh của công ty bảo hiểm và chuyển nhân viên kèm tóm tắt | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu `audit_sample_checked` 100 đơn/tuần so với bảng giá hiện hành; ngưỡng 1% đơn lệch; ghi `phien_ban_bang_gia` vào trace để so | Xoá bộ nhớ đệm ngay khi có bảng giá mới; agent đọc phiên bản bảng giá mỗi lần chạy và từ chối dùng bản hết hiệu lực | Kế toán trưởng |
