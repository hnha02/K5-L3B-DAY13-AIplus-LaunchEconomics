# Team

## Thông tin nhóm

- Tên nhóm: AIplus
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-AIplus-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/hnha02/K5-L3B-DAY13-AIplus-LaunchEconomics · `main` · (điền hash commit chốt)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Trần Thị Hà Anh | 2A202603887 | tranthihaanh200204@gmail.com | hnha02 | Người viết code (CP1–CP2) → người kiểm số (CP4–CP5); phụ trách `chi_so.md`, commit/push |
|   2 | Nguyễn Nghiêm Khánh Tiệp | 2A2020603863 | tiepnnk04@gmail.com | tiepnnk01-10 | Người kiểm số (CP1–CP2), người gắn nhãn 1 (CP3) → người viết code sau giải lao (CP4) |
|   3 | Phùng Thị Nhài | 2A202603725 | nhaipt342k4@gmail.com | nhaipt342k4 | Người gắn nhãn 2 (CP3), kiêm giữ hồ sơ từ đầu buổi; phụ trách `phieu_cham.md`, `group_report.md` |

Nhóm có 3 người nên gộp bốn vai như sau: vai **người kiểm số** do Tiệp giữ ở CP1–CP2, chuyển sang Hà Anh từ CP4 (khi Tiệp nhận viết code). Hai người gắn nhãn độc lập ở CP3 là Tiệp và Nhài; trong lúc đó Hà Anh hoàn thiện CP2.

### Phân công theo checkpoint

| Giờ | Hà Anh | Tiệp | Nhài |
| --- | --- | --- | --- |
| 14:00 · Setup | Cài môi trường, chạy thử `lab13.py` | Cài môi trường | Điền `TEAM.md`, đọc mẫu `ho_so_launch_v0.md` |
| 14:10 · CP1 (A) | Viết 3 hàm A1 (đạt 1,20 · 1,25 · 1,25), `mo_hinh`, A3, A4 | Tính tay đối chiếu, điền bảng A2/A3/A4 vào `bang_chi_phi.md`, gắn nhãn **simulated** | Đọc trước 20 ca lỗi và 5 loại lỗi PAIR; ghi số A vào hồ sơ |
| 14:53 · CP2 (B) | Code B1–B4 | Kiểm "giảm nửa = nửa mức tăng", điền B1–B4, xếp hạng top 3 | Ghi top 3 yếu tố vào hồ sơ |
| 15:35 · CP3 (C) | Hoàn thiện CP2, dựng khung `chi_so.md` | Gắn nhãn 20 ca độc lập (8'), so nhãn, tính đồng thuận (≥ 16/20), viết quy tắc cho ca lệch | Gắn nhãn 20 ca độc lập (8'), cùng làm bảng khắc phục 5 ca trong `bang_loi.md` |
| 16:08 · CP4 (D) | Kiểm số D1, tính tỉ lệ `mo_lai_trong_7_ngay`, viết 3 luật dừng | Code D1, điền `pilot_plan.yaml`, chạy `yaml.safe_load` | Trả lời 5 câu D2, ghi cách chia pilot vào hồ sơ |
| 16:36 · CP5 (E) | `chi_so.md`: 3 chỉ số, 6 event, 2 rủi ro kinh tế | Rà soát: không còn `?`, không có từ cấm, đủ nhãn simulated | Hoàn thiện hồ sơ 7 mục; cả nhóm chốt đề xuất lúc ~16:50 |
| 17:00 · Duyệt chéo | Trình bày 1 phút | Đọc và chấm hồ sơ nhóm n + 1 | Ghi `phieu_cham.md`, đặt 1 câu hỏi |
| 17:45 · Nộp | Commit, push | Báo cáo cá nhân | `group_report.md`, báo cáo cá nhân |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## TranThiHaAnh-2A202603887

### Phần việc phụ trách

- Người viết code CP1–CP2: `src/lab13.py` phần A1, A2, A3, A4, B1–B4, E1.
- Người kiểm số CP4: kiểm D1 của Tiệp; tính tỉ lệ mở lại hiện tại, viết ba luật dừng.
- `report/team/bang_chi_phi.md`, `report/team/chi_so.md`; commit, push.

### Đóng góp cụ thể

- Ba hàm A1 qua đủ ba phép thử (1,20 · 1,25 · 1,25); hàm `mo_hinh` cho chi phí mỗi việc thành công 4.472 đ, gấp 16,3 lần hoá đơn chia số yêu cầu [simulated].
- A3: quoc_te 1,88× của 12.000 đ, chạy lại không giúp (ok lần 1 30%, lần 3 2,2%); A4 cộng cố định: 4.599 đ = 0,38× trong phạm vi [simulated].
- B1–B4: xếp hạng làm lại ±51,8%, xem lại ±40,7%, lương +23,1%; giới hạn 2 lần rẻ nhất cho công ty; xem lại 100% cho 0,98× [simulated].
- Tỉ lệ mở lại 4,25% (3,97% trong phạm vi) → luật an toàn so với đối chứng (+2 điểm, trần 6%); ba luật dừng an toàn, chi phí, sử dụng.
- `chi_so.md`: 3 chỉ số tính thử (82,83% · 27,12% · 4,25%), 2 chỉ số đề xuất, 10 event có `trace_id`, 3 rủi ro kinh tế.
- Kiểm D1 bằng cách tính độc lập: khớp 1.251 · 3.103 · 1.000 · 300 · m ≥ 299 · power 0,64.

### Bằng chứng

- Commit `1005c90` (code A, B, E1; `bang_chi_phi.md`, `chi_so.md`, luật dừng), `cd6263e` (chia việc), `6176e71`, `e677d44`
- Báo cáo cá nhân: `report/team/2A202603887_TranThiHaAnh.md`

## NguyenNghiemKhanhTiep-2A2020603863

### Phần việc phụ trách

- Người kiểm số CP1–CP2; người gắn nhãn 1 ở CP3; người viết code CP4 (D1 trong `src/lab13.py`, `report/team/pilot_plan.yaml`); rà soát hồ sơ CP5.

### Đóng góp cụ thể

- Tính lại độc lập A2–A4, B1–B4, khớp 100% với output `lab13.py` (4.472 đ [simulated]; giới hạn 2 lần 6.901.220 đ [simulated]).
- D1: 1.251 yêu cầu mỗi nhóm; 42 người mỗi nhóm (84 > 40); trần 1.000 với 20 nhân viên; 300 với 6 depot; m ≥ 299 (DE 6,96) cho mức chênh 6 điểm; power 0,64 nếu tác động thật 5 điểm.
- `pilot_plan.yaml`: chia theo nhân viên 20 + 20, n 859, 20 cụm, rollback, decision_date 2027-01-08, simulated_inputs; không còn `?`, đọc được bằng `yaml.safe_load`.
- CP3: gắn nhãn độc lập 20 ca; đồng thuận 19/20 = 95%.

### Bằng chứng

- Commit `c69cb34`, `d31806b` (D1, `pilot_plan.yaml`), `bd760e2` (nhãn CP3)
- Báo cáo cá nhân: `report/team/2A2020603863_NguyenNghiemKhanhTiep.md`

## PhungThiNhai-2A202603725

### Phần việc phụ trách

- Người gắn nhãn 2 ở CP3, kiêm giữ hồ sơ: `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md` (cùng Tiệp), D2 trong `report/team/pilot_plan.yaml`, `report/team/group_report.md`, `report/team/phieu_cham.md`.

### Đóng góp cụ thể

- Hồ sơ launch v0 bảy mục, mỗi mục có con số chính, trạng thái, người phụ trách; đề xuất Go có điều kiện cho noi_dia + hang_nang với 4 điều kiện có ngày kiểm tra.
- CP3: gắn nhãn độc lập 20 ca, đồng thuận 19/20 = 95%; cùng Tiệp thống nhất ca 13 (Giới hạn hệ thống); bảng khắc phục 5 ca đủ năm loại.
- D2: năm câu "tách được tác động" cho cách chia 20 + 20 nhân viên; đánh đổi mức chênh 6 điểm (power 0,64).
- Báo cáo nhóm; phiếu chấm hội đồng nhóm n + 1.

### Bằng chứng

- Commit `e99647f`, `bae55bd`, `857aa7c`, `38ed2a9` (hồ sơ), `c725def` (nhãn CP3), `8a40550` (D2, báo cáo nhóm), `5017db6`, `51f8b57`
- Báo cáo cá nhân: `report/team/2A202603725_PhungThiNhai.md`
