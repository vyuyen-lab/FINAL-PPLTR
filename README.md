## FINAL PROJECT: HỆ THỐNG ĐẶT VÉ MÁY BAY TRỰC TUYẾN

 Kiến trúc và Lưu trữ dữ liệu

Dự án được xây dựng dựa trên Mô hình Lập trình Hướng đối tượng (OOP) và Kiến trúc Phân tầng (Layered Architecture), lưu trữ dữ liệu thông qua cấu trúc đối tượng của Python và xuất ra tệp tin:

*   **Kiến trúc Phân tầng:** Chia tách rõ ràng 3 thư mục `models/` (Data), `services/` (Business Logic), và `views/` (CLI Menu).
*   **Trong bộ nhớ:** Dữ liệu toàn hệ thống được lưu trong các danh sách (`List`), mỗi phần tử là một đối tượng (`Object`) đại diện cho một Chuyến bay hoặc một Vé máy bay.
*   **Lưu trữ vật lý:** Hỗ trợ lưu trữ bền vững dưới hai định dạng:
    *   `flights.json` / `tickets.json`: Lưu trữ có cấu trúc chuẩn, đảm bảo tính toàn vẹn dữ liệu đối tượng khi tắt/mở chương trình (Tiêu chí nâng cao).
    *   `baocao_doanhthu.csv`: Lưu trữ dạng văn bản thuần túy theo định dạng phân tách bằng dấu phẩy, đáp ứng tốt yêu cầu xuất báo cáo thống kê.

---

## Các tính năng cốt lõi

Hệ thống cung cấp một Menu tương tác với 6 nhóm chức năng chính:

1. **Quản lý Thực thể (Input, Update, Delete & Validation):** - Khởi tạo, chỉnh sửa và xóa hồ sơ chuyến bay.
   * *Điểm nhấn:* Tích hợp cơ chế kiểm tra tính hợp lệ của dữ liệu bằng khối lệnh `try...except` (chặn số âm, chặn ký tự chữ vào trường giá tiền), đảm bảo hệ thống không bị crash.
2. **Hiển thị danh sách (Display):** - Trích xuất toàn bộ dữ liệu hiện có và in ra màn hình dưới dạng thông tin rõ ràng, dễ nhìn.
3. **Tìm kiếm thông minh (Advanced Search):** - Hỗ trợ tìm kiếm chuỗi con (khớp một phần) theo Điểm đến của chuyến bay (Không phân biệt chữ hoa/chữ thường).
4. **Sắp xếp dữ liệu (Sort):** - Sắp xếp danh sách chuyến bay dựa trên mức giá gốc (theo thứ tự giảm dần).
5. **Nghiệp vụ Giao dịch & Thống kê (Transaction & Statistics):** - Xử lý đặt vé phức tạp (tính thêm phí hành lý/suất ăn, áp dụng mã giảm giá), tính toán tổng số lượng khách hàng và tổng doanh thu toàn hệ thống.
   * *Điểm nhấn:* Gom nhóm và đối chiếu số liệu chi tiết giữa 2 phân khúc vé (Phổ thông và Thương gia) thông qua tính Đa hình (Polymorphism).
6. **Sao lưu & Thoát (File I/O):** - Đồng bộ hóa dữ liệu từ RAM xuống ổ cứng (vào các tệp `.json` và `.csv`) trước khi đóng chương trình, đảm bảo tính toàn vẹn của dữ liệu cho những lần khởi động sau.

---

## Hướng dẫn cài đặt và sử dụng

**Các bước chạy chương trình:**

1. Clone repository này về máy hoặc tải toàn bộ mã nguồn.
2. Mở Terminal / Command Prompt tại thư mục chứa dự án.
3. Chạy lệnh: `python main.py`
4. Sử dụng các phím số từ `0` đến `9` để điều hướng menu và nhập dữ liệu theo các chỉ dẫn trên màn hình.

---

## Đánh giá mức độ hoàn thành


- [x] Áp dụng chuẩn 4 tính chất OOP (Đóng gói, Kế thừa, Đa hình, Trừu tượng) (2.0 đ)
- [x] Phân tầng kiến trúc (Layered Architecture) & Clean Code (1.5 đ)
- [x] Menu CLI hoạt động ổn định & Nhập liệu chặn lỗi thành công (1.5 đ)
- [x] Đầy đủ nghiệp vụ cơ bản (CRUD) (1.0 đ)
- [x] Tìm kiếm khớp một phần chuỗi & Sắp xếp dữ liệu (1.0 đ)
- [x] Đọc/ghi file JSON an toàn (1.0 đ)
- [x] Logic giao dịch phức tạp (Tính tiền vé, giảm giá, dịch vụ) (1.0 đ + Nâng cao)
- [x] Thống kê nâng cao & Xuất file CSV (1.0 đ + Nâng cao)
- [x] Quản lý mã nguồn dạng Modular, sử dụng Git & GitHub (0.5 đ + Nâng cao)

**Mục tiêu phải đạt : 10/10 Điểm**

---

## Thông tin

*   **Sinh viên thực hiện:** Vy Uyên
*   **Ngành học:** Sư phạm Tin học
*   **Học phần:** Phương pháp lập trình
