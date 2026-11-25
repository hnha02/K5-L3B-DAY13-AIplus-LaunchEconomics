# Báo cáo cá nhân — TranThiHaAnh-2A202603887

## 1. Thông tin thành viên

- Họ tên: Trần Thị Hà Anh
- MSSV: 2A202603887
- Email: tranthihaanh200204@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người viết code (CP1–CP2), chuyển sang người kiểm số (CP4–CP5); commit/push bài nộp.

## 2. Phần việc phụ trách

- Nhiệm vụ A và B trong `src/lab13.py`: ba hàm A1, hàm `mo_hinh`, A3 theo loại, A4 chi phí cố định, B1–B4 độ nhạy.
- `report/team/bang_chi_phi.md` (số A, B; Tiệp kiểm tay và đối chiếu).
- Nhiệm vụ D: tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại và viết ba luật dừng trong `report/team/pilot_plan.yaml`.
- Nhiệm vụ E: `report/team/chi_so.md` (chỉ số, event, rủi ro kinh tế).

## 3. Đóng góp cụ thể

- Viết ba hàm A1, qua đủ ba phép thử 1,20 · 1,25 · 1,25.
- Viết `mo_hinh`: tử số tính mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm `thanh_cong`; ra chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn chia số yêu cầu.
- A3: chỉ ra quoc_te 1,88× của 12.000 đ [simulated], chạy lại không giúp (ok lần 1 30%, lần 3 chỉ 2,2%).
- B1–B3: xếp hạng ba yếu tố nhạy nhất (làm lại +51,8%, xem lại +40,7%, lương +23,1%) [simulated]; giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ) [simulated].
- B4: xem lại 100% cho 11.743 đ = 0,98× (12.415 đ = 1,03× với 15,3 phút làm lại) [simulated], hoà vốn khi xem lại ≤ 5,1 phút.
- Tính tỉ lệ mở lại 4,25% (3,97% trong phạm vi) để đặt luật an toàn theo chênh lệch với đối chứng thay vì ngưỡng tuyệt đối 3%.
- Viết `chi_so.md`: 3 chỉ số tính thử (82,83% · 27,12% · 4,25%), 2 chỉ số tự đề xuất, 10 event có `trace_id`, 3 dòng rủi ro kinh tế.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- `src/lab13.py` (chạy `python lab13.py` trong `src/` in ra toàn bộ số A, B, E1)
- `report/team/bang_chi_phi.md`, `report/team/chi_so.md`, phần `stop_rules` và chú thích tỉ lệ mở lại trong `report/team/pilot_plan.yaml`
- Commit: `1005c90` (CP1-CP2: mô hình chi phí, độ nhạy; chỉ số E1, luật dừng D)

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Claude Code: hỗ trợ viết code A1, A2, A3, A4, B và điền bảng. Kiểm tra bằng ba phép thử đáp án biết trước, quy tắc "giảm một nửa = nửa mức tăng của gấp đôi" ở B1, và đối chiếu từng số với slide chữa (lệch không quá 2%).

## 6. Tự đánh giá

- (tự điền)
