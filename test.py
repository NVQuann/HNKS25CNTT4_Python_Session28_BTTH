class Product:
    def __init__(self, id, name, price, quantity_sold, discount):
        self.id = id
        self.name = name
        self.price = price
        self.quantity_sold = quantity_sold
        self.discount = discount
        self.total_revenue = 0
        self.revenue_type = ""
        self.calculate_revenue()
        self.classify_revenue()

    def calculate_revenue(self):
        revenue = self.price * self.quantity_sold - self.discount
        self.total_revenue = max(0, revenue)

    def classify_revenue(self):
        if self.total_revenue < 5000000:
            self.revenue_type = "Thấp"
        elif self.total_revenue < 20000000:
            self.revenue_type = "Trung bình"
        elif self.total_revenue < 50000000:
            self.revenue_type = "Khá"
        else:
            self.revenue_type = "Cao"

class  ProductManager:
    def __init__(self):
        self.products = []

    def find_by_id(self, id):
        for product in self.products:
            if product.id.lower() == id.lower():
                return product
        return None

    def add_product(self):
        while True:
            id = input("Nhập mã sản phẩm: ").strip()
            if id == "":
                print("Mã sản phẩm không được để trống!")
            elif self.find_by_id(id):
                print("Mã sản phẩm đã tồn tại!")
            else:
                break

        while True:
            name = input("Nhập tên sản phẩm: ").strip()
            if name == "":
                print("Tên không được để trống!")
            else:
                break

        while True:
            try:
                price = float(input("Nhập giá bán: "))
                if price >= 0:
                    break
                print("Giá bán phải lớn hơn hoặc bằng 0")
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")

        while True:
            try:
                quantity = int(input("Nhập số lượng đã bán: "))
                if 0 <= quantity <= 10000:
                    break
                print("Số lượng phải từ 0 đến 10000") 
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ!")

        while True:
            try:
                discount = float(input("Nhập giảm giá: "))
                if discount >= 0:
                    break
                print("Giảm giá phải lớn hơn hoặc bằng 0")
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")

        product = Product(id, name, price, quantity, discount)
        self.products.append(product)

        print("Thêm sản phẩm thành công.")

    

    def show_all(self):
        if not self.products:
            print("Danh sách sản phẩm đang rỗng!")
            return
        print(f"{'Mã SP':<10} | {'Tên sản phẩm':<25} | {'Giá bán':<15} | {'SL bán':<10} | {'Giảm giá':<15} | {'Tổng doanh thu':<18} | {'Loại doanh thu':<15}")
        for product in self.products:
            print(f"{product.id:<10} | {product.name:<25} | {product.price:<15,.0f} | {product.quantity_sold:<10} | {product.discount:<15} | {product.total_revenue:<18,.0f} | {product.revenue_type:<15}")


    def update_product(self):
        id = input("Nhập mã sản phẩm cần cập nhật: ").strip()
        product = self.find_by_id(id)

        if not product:
            print("Không tìm thấy sản phẩm cần cập nhật!")
            return

        while True:
            try:
                price = float(input("Nhập giá bán mới: "))
                if price >= 0:
                    break
                print("Giá bán phải >= 0!")
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")

        while True:
            try:
                quantity = int(input("Nhập số lượng đã bán mới: "))
                if 0 <= quantity <= 10000:
                    break
                print("Số lượng phải từ 0 đến 10000!")
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ!")

        while True:
            try:
                discount = float(input("Nhập giảm giá mới: "))
                if discount >= 0:
                    break
                print("Giảm giá phải >= 0!")
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")

        product.price = price
        product.quantity_sold = quantity
        product.discount = discount

        product.calculate_revenue()
        product.classify_revenue()

        print("Cập nhật sản phẩm thành công!")
        
    
    def delete_product(self):
        id = input("Nhập mã sản phẩm cần xóa: ").strip()

        product = self.find_by_id(id)

        if not product:
            print("Không tìm thấy sản phẩm cần xóa!")
            return

        confirm = input("Bạn có chắc muốn xóa sản phẩm này không? (Y/N): ").strip().lower()

        if confirm == "y":
            self.products.remove(product)
            print("Xóa sản phẩm thành công!")
        elif confirm == "n":
            print("Đã hủy thao tác xóa!")
        else:
            print("Lựa chọn không hợp lệ!")

    def search_product(self):
        keyword = input("Nhập từ khóa tìm kiếm: ").strip().lower()

        found = False

        for product in self.products:
            if keyword in product.name.lower():
                found = True
                print(
                    f"{product.id:<10} | "
                    f"{product.name:<25} | "
                    f"{product.price:<15,.0f} | "
                    f"{product.total_revenue:<18,.0f} | "
                    f"{product.revenue_type:<15}"
                )

        if not found:
            print("Không tìm thấy sản phẩm phù hợp!")
        

    def statistics(self):
        if not self.products:
            print("Chưa có dữ liệu!")
            return
        
        low = 0
        medium = 0
        rather = 0
        high = 0
        for product in self.products:
            if product.revenue_type == 'Thấp':
                low += 1
            elif product.revenue_type == 'Trung bình':
                medium += 1
            elif product.revenue_type == 'Khá':
                rather += 1
            elif product.revenue_type == 'Cao':
                high += 1


        print("---- Thống kê doanh thu ----")
        print(f"{'Phân loại':<20}{'Số lượng'}")       
        print(f"{'Thấp':<20}{low}") 
        print(f"{'Trung bình':<20}{medium}")
        print(f"{'Khá':<20}{rather}")
        print(f"{'Cao':<20}{high}")



def main():
    manager = ProductManager()
    while True:
        choice = input("""================ MENU ================
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật sản phẩm
4. Xóa sản phẩm
5. Tìm kiếm sản phẩm
6. Thống kê doanh thu
7. Thoát
=====================================
Nhập lựa chọn của bạn: """)
        match choice:
            case "1":
                manager.show_all()
            case "2":
                manager.add_product()
            case "3":
                manager.update_product()
            case "4":
                manager.delete_product()
            case "5":
                manager.search_product()
            case "6":
                manager.statistics()
            case "7":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý sản phẩm!")
                break
            case _:
                print("Lựa chọn không hợp lê!. Vui lòng nhập từ (1-7)")

if __name__ == "__main__":
    main()
