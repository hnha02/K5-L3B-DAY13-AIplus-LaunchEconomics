# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): AIplus
- Nhóm được chấm: GeminiPro

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Go có điều kiện cho noi_dia + hang_nang khớp số của nhóm (0,38× trong phạm vi, quoc_te 1,88×); nêu đủ con số bất lợi kèm cách xử lý: xem lại 100% 0,98×–1,03× → điều kiện 4 giảm xem lại theo bậc; power 0,642 → điều kiện 2 ký chấp nhận; hoàn trùng ca 7, 20 → điều kiện 1. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi số dựa trên phút giả lập (mục 1, 2, 3, 7) có nhãn `simulated`; số đo từ trace ghi rõ (274,7 đ/yc, chỉ số mục 4); loại quoc_te có lý do bằng số (1,88×, ok lần 3 chỉ 2,2%). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 5 | Có đối chứng đồng thời 20 + 20, đủ mẫu (859/nhóm, DE 6,96, m ≥ 299), luật dừng có ngưỡng và thời hạn (+2 điểm / trần 6% / 1 ca hoàn trùng trong 3 ngày → tắt trong 30 phút); nhưng không ghi vai nào có quyền ra lệnh dừng, và rollout 10%→25%→50% mâu thuẫn với chia cố định 20 + 20. |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Chi phí trong phạm vi noi_dia + hang_nang là 0,38× của 12.000 đ [simulated] và nhóm đã nêu các con số bất lợi kèm điều kiện xử lý; hội đồng đồng ý với 4 điều kiện của nhóm, thêm điều kiện ghi rõ vai có quyền dừng pilot và làm rõ nhóm đối chứng ở từng bước rollout trước ngày mở pilot.

**Một câu hỏi cho đội trình:** Ai có quyền ra lệnh tắt pilot trong 30 phút khi luật dừng an toàn bị kích hoạt?

**Câu trả lời của đội trình (ghi lại tại buổi):** ...
