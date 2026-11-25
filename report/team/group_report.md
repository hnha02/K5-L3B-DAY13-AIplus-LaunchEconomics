# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: AIplus
- Lớp: L3B
- Thành viên: xem `TEAM.md` (3 người: Trần Thị Hà Anh, Nguyễn Nghiêm Khánh Tiệp, Phùng Thị Nhài)

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a quyết định có cho chạy pilot hay không. Nhóm trả lời bốn câu: có đáng chạy không (chi phí mỗi việc thành công so với 12.000 đ), nhân viên có dùng không (chỉ số và event), khi hỏng thì sao (bảng lỗi PAIR), và pilot thiết kế thế nào để ra được quyết định (đối chứng, cỡ mẫu, luật dừng). Mọi con số do `src/lab13.py` tính và được người kiểm số đối chiếu lại.

## 3. Giải pháp

- **A · Chi phí** ([bang_chi_phi.md](bang_chi_phi.md)): hàm `mo_hinh` tính tử số trên mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm việc thành công; tách theo loại yêu cầu và cộng chi phí cố định 40 triệu đ/tháng.
- **B · Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): gọi lại `mo_hinh` cho 9 kịch bản, 1 cặp, giới hạn số lần chạy và kịch bản xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): hai người gắn nhãn độc lập 20 ca theo năm loại PAIR, so nhãn, bảng khắc phục 5 ca.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): tính cỡ mẫu theo yêu cầu/nhân viên/depot trước khi chọn cách chia; chọn chia theo nhân viên 20 + 20; 3 luật dừng.
- **E · Chỉ số và hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): 3 chỉ số tính thử, 10 event có `trace_id`, 3 rủi ro kinh tế, hồ sơ một trang bảy mục.

## 4. Kết quả

- Chi phí mỗi việc thành công 4.472 đ, gấp 16,3 lần hoá đơn token chia số yêu cầu [simulated]; phạm vi noi_dia + hang_nang cộng cố định 4.599 đ = 0,38× của 12.000 đ [simulated].
- Ba yếu tố nhạy nhất: số ca làm lại (±51,8%), tỉ lệ xem lại (±40,7%), lương nhân viên (+23,1%) [simulated]. Con số bất lợi: xem lại 100% cho 0,98× (1,03× với 15,3 phút làm lại) [simulated].
- quoc_te 1,88× và doi_tac 0,85× [simulated] nên loại khỏi phạm vi pilot.
- Chỉ số trong đợt chạy thử: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%.
- Pilot: theo nhân viên 20 + 20, đủ mẫu cho mức chênh 6 điểm, không đủ cho 5 điểm (power 0,64).
- Bảng lỗi: hai người gắn nhãn độc lập đồng thuận 19/20 = 95%; ca lệch duy nhất (ca 13) thống nhất là Giới hạn hệ thống.
- Đề xuất cuối: (điền sau khi nhóm chốt, xem `ho_so_launch_v0.md`).
- Kết quả duyệt chéo nhóm nhận được: .../30, quyết định của hội đồng: ... (điền sau 17:25).

## 5. Khó khăn và cách xử lý

- **Nhóm chỉ có 3 người** trong khi lab thiết kế 4 vai: gộp vai người kiểm số (Tiệp ở CP1–CP2, Hà Anh từ CP4); hai người gắn nhãn độc lập là Tiệp và Nhài (chi tiết trong `TEAM.md`).
- **Xung đột khi push:** hai người cùng sửa `TEAM.md`; xử lý bằng `git pull --rebase` và gộp tay bảng thành viên.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập; pilot phải thay bằng phút đo thật từ event `staff_review_decision` và `staff_rework_completed` sau tuần 1.
- Với 40 nhân viên, không cách chia theo cụm nào đủ mẫu cho mức chênh 5 điểm; nhóm chấp nhận mức 6 điểm.
- Đợt chạy thử không có nhóm đối chứng, nên chưa thể nói trợ lý đã nâng chỉ số chính.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu statsmodels, `NormalIndPower`.
- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, `docs/du_lieu_va_cong_thuc.md`.
