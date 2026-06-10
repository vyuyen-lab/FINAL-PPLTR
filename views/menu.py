
from services.booking_service import BookingService

class ConsoleMenu:
    def __init__(self):
        self.service = BookingService()

    def run(self):
        while True:
            print("\n" + "="*50)
            print("  HỆ THỐNG ĐẶT VÉ MÁY BAY ONLINE - TOPIC 12 ✈️")
            print("="*50)
            print("1. Thêm chuyến bay mới")
            print("2. Hiển thị danh sách chuyến bay")
            print("3. Tìm kiếm chuyến bay theo điểm đến")
            print("4. Sắp xếp chuyến bay theo giá gốc giảm dần")
            print("5. Thực hiện Đặt vé mới (Giao dịch)")
            print("6. Hiển thị danh sách vé đã đặt")
            print("7. Thống kê hệ thống & Xuất file báo cáo (.csv)")
            print("8. Cập nhật thông tin chuyến bay")
            print("9. Xóa chuyến bay")
            print("0. Thoát chương trình & Đồng bộ dữ liệu")
            print("="*50)
            
            choice = input(" Mời bạn chọn chức năng (0-9): ")
            print("-"*50)

            try:
                if choice == "1":
                    fid = input("Nhập mã chuyến bay (ví dụ: VN123): ")
                    dest = input("Nhập điểm đến: ")
                    price = float(input("Nhập giá vé cơ bản (VND): "))
                    seats = int(input("Nhập số lượng ghế trống: "))
                    self.service.add_flight(fid, dest, price, seats)

                elif choice == "2":
                    flights = self.service.get_all_flights()
                    if not flights:
                        print(" Hiện tại chưa có chuyến bay nào trên hệ thống.")
                    else:
                        print(f"{'MÃ CB':<10} | {'ĐIỂM ĐẾN':<20} | {'GIÁ GỐC (VND)':<15} | {'GHẾ TRỐNG'}")
                        print("-"*60)
                        for f in flights:
                            print(f"{f.flight_id:<10} | {f.destination:<20} | {f.base_price:<15,.0f} | {f.available_seats}")

                elif choice == "3":
                    kw = input("Nhập tên thành phố/điểm đến muốn tìm kiếm: ")
                    results = self.service.search_flight_by_destination(kw)
                    if not results:
                        print(" Không tìm thấy chuyến bay nào phù hợp.")
                    else:
                        for f in results:
                            print(f" [{f.flight_id}] Đến: {f.destination} | Giá: {f.base_price:,.0f} VND | Còn {f.available_seats} ghế.")

                elif choice == "4":
                    self.service.sort_flights_by_price_desc()

                elif choice == "5":
                    tid = input("Nhập mã vé mới: ")
                    name = input("Nhập họ và tên hành khách: ")
                    fid = input("Nhập mã chuyến bay muốn đi: ")
                    ttype = input("Chọn hạng vé (1 - Phổ thông / 2 - Thương gia): ")
                    
                    if ttype == "1":
                        opt = input("Nhập số kg hành lý mang thêm (0 nếu không mua): ")
                    elif ttype == "2":
                        opt = input("Bạn có muốn đặt suất ăn cao cấp không? (Y/N): ")
                    else:
                        print(" Hạng vé vừa chọn không đúng quy định!")
                        continue

                    code = input("Nhập mã khuyến mãi (nhấn Enter nếu không có): ")
                    self.service.book_ticket(tid, name, fid, ttype, opt, code)

                elif choice == "6":
                    tickets = self.service.get_all_tickets()
                    if not tickets:
                        print(" Chưa có vé nào được đặt thành công.")
                    else:
                        print(f"{'MÃ VÉ':<10} | {'HÀNH KHÁCH':<20} | {'MÃ CB':<10} | {'TỔNG TIỀN TRẢ (VND)'}")
                        print("-"*65)
                        for t in tickets:
                            print(f"{t.ticket_id:<10} | {t.passenger_name:<20} | {t.flight.flight_id:<10} | {t.calculate_total_price():<15,.0f}")

                elif choice == "7":
                    self.service.export_statistics_report()

                elif choice == "8":
                    fid = input("Nhập mã chuyến bay cần chỉnh sửa: ")
                    dest = input("Nhập điểm đến mới: ")
                    price = float(input("Nhập giá bán mới: "))
                    seats = int(input("Nhập số lượng ghế trống mới: "))
                    self.service.update_flight(fid, dest, price, seats)

                elif choice == "9":
                    fid = input("Nhập mã chuyến bay cần xóa khỏi hệ thống: ")
                    confirm = input("Bạn có chắc chắn muốn xóa không? (Y/N): ")
                    if confirm.upper() == 'Y':
                        self.service.delete_flight(fid)

                elif choice == "0":
                    self.service.save_data()
                    print(" Dữ liệu đã được lưu trữ vĩnh viễn an toàn. Tạm biệt!")
                    break
                else:
                    print(" Lựa chọn sai mục chức năng, vui lòng nhập lại từ 0 đến 9.")

            except ValueError:
                print(" Lỗi kiểu dữ liệu: Vui lòng nhập đúng định dạng số tiền hoặc số lượng ghế!")
            except Exception as e:
                print(f" Có lỗi không mong muốn xảy ra: {e}")