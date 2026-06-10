import json
import csv
from models.flight import Flight
from models.ticket import EconomyTicket, BusinessTicket

class BookingService:
    def __init__(self):
        self.flights = []  
        self.tickets = []  
        self.load_data()   

    def add_flight(self, flight_id, destination, base_price, available_seats):
        if any(f.flight_id == flight_id for f in self.flights):
            print(" Lỗi: Mã chuyến bay này đã tồn tại trên hệ thống!")
            return False
        new_flight = Flight(flight_id, destination, base_price, available_seats)
        self.flights.append(new_flight)
        self.save_data()
        print(" Thêm chuyến bay mới thành công!")
        return True

    def get_all_flights(self):
        return self.flights

    def update_flight(self, flight_id, new_destination, new_price, new_seats):
        for f in self.flights:
            if f.flight_id == flight_id:
                f._destination = new_destination
                f._base_price = new_price
                f.available_seats = new_seats
                self.save_data()
                print(" Cập nhật thông tin chuyến bay thành công!")
                return True
        print(" Không tìm thấy chuyến bay cần sửa!")
        return False

    def delete_flight(self, flight_id):
        for f in self.flights:
            if f.flight_id == flight_id:
                self.flights.remove(f)
                self.save_data()
                print(" Đã xóa chuyến bay thành công!")
                return True
        print(" Không tìm thấy chuyến bay cần xóa!")
        return False

    def book_ticket(self, ticket_id, passenger_name, flight_id, ticket_type, extra_option, discount_code=""):
        if any(t.ticket_id == ticket_id for t in self.tickets):
            print(" Lỗi: Mã vé này đã tồn tại!")
            return False

        flight = next((f for f in self.flights if f.flight_id == flight_id), None)
        if not flight:
            print(" Lỗi: Không tồn tại chuyến bay này!")
            return False

        try:
            if ticket_type == "1":
                ticket = EconomyTicket(ticket_id, passenger_name, flight, extra_luggage_kg=int(extra_option), auto_book=True)
            elif ticket_type == "2":
                has_meal = True if extra_option.upper() == 'Y' else False
                ticket = BusinessTicket(ticket_id, passenger_name, flight, has_meal=has_meal, auto_book=True)
            else:
                print(" Loại vé không hợp lệ!")
                return False

            final_price = ticket.calculate_total_price()
            if discount_code.upper() == "UYN":

                print(" Đã áp dụng mã giảm giá 'UYN' - Giảm 10% tổng vé!")

            self.tickets.append(ticket)
            self.save_data()
            print(f" Đặt vé thành công! Tổng tiền thanh toán: {final_price:,.0f} VND")
            return True

        except ValueError as e:
            print(f" Giao dịch thất bại: {e}")
            return False

    def get_all_tickets(self):
        return self.tickets

    def search_flight_by_destination(self, keyword):
        return [f for f in self.flights if keyword.lower() in f.destination.lower()]

    def sort_flights_by_price_desc(self):

        self.flights.sort(key=lambda f: f.base_price, reverse=True)
        print(" Đã sắp xếp danh sách chuyến bay theo giá giảm dần!")

    def export_statistics_report(self):
        total_revenue = 0
        economy_count = 0
        business_count = 0

        for t in self.tickets:
            total_revenue += t.calculate_total_price()
            if isinstance(t, EconomyTicket):
                economy_count += 1
            elif isinstance(t, BusinessTicket):
                business_count += 1

        print("\n --- SỐ LIỆU THỐNG KÊ HỆ THỐNG ---")
        print(f"Tổng doanh thu hiện tại: {total_revenue:,.0f} VND")
        print(f"Số lượng vé Phổ thông (Economy): {economy_count}")
        print(f"Số lượng vé Thương gia (Business): {business_count}")

        try:
            with open("baocao_doanhthu.csv", "w", newline="", encoding="utf-8-sig") as f:
                writer = csv.writer(f)
                writer.writerow(["Tiêu chí thống kê", "Giá trị thực tế"])
                writer.writerow(["Tổng doanh thu (VND)", f"{total_revenue:.0f}"])
                writer.writerow(["Số lượng vé Phổ thông", economy_count])
                writer.writerow(["Số lượng vé Thương gia", business_count])
            print("💾 Đã xuất báo cáo thống kê thành công ra tệp 'baocao_doanhthu.csv'!")
        except Exception as e:
            print(f" Lỗi khi xuất file báo cáo: {e}")

    def save_data(self):
        flight_data = [f.to_dict() for f in self.flights]
        with open("flights.json", "w", encoding="utf-8") as f:
            json.dump(flight_data, f, ensure_ascii=False, indent=4)

        ticket_data = []
        for t in self.tickets:
            t_info = {
                "ticket_id": t.ticket_id,
                "passenger_name": t.passenger_name,
                "flight_id": t.flight.flight_id,
                "type": "Economy" if isinstance(t, EconomyTicket) else "Business",
                "extra_option": t.extra_luggage_kg if isinstance(t, EconomyTicket) else ("Y" if t.has_meal else "N")
            }
            ticket_data.append(t_info)
        with open("tickets.json", "w", encoding="utf-8") as f:
            json.dump(ticket_data, f, ensure_ascii=False, indent=4)

    def load_data(self):
        try:
            with open("flights.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.flights = [Flight.from_dict(item) for item in data]
        except FileNotFoundError:
            self.flights = []

        try:
            with open("tickets.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    
                    fl = next((f for f in self.flights if f.flight_id == item["flight_id"]), None)
                    if fl:
                        if item["type"] == "Economy":
                            t = EconomyTicket(item["ticket_id"], item["passenger_name"], fl, extra_luggage_kg=int(item["extra_option"]), auto_book=False)
                        else:
                            has_meal = True if item["extra_option"] == "Y" else False
                            t = BusinessTicket(item["ticket_id"], item["passenger_name"], fl, has_meal=has_meal, auto_book=False)
                        self.tickets.append(t)
        except FileNotFoundError:
            self.tickets = []