'''
Bài 14:
1. Tạo một lớp có tên Product bao gồm các thuộc tính và phương thức sau:
· Name
· Description
· Price // 0 < Price <= 100
· list rate // lưu các đánh giá của người dùng cho sản phẩm, giá trị từ 1 - 5
· viewInfo() // hiển thị tên, giá và mô tả về sản phẩm

2. Tạo lớp Shop gồm các thuộc tính và phương thức sau:
· List ProductList // lưu danh sách các sản phẩm của shop
· addProduct()  // yêu cầu người dùng nhập thông tin của sản phẩm rồi lưu vào ProductList
· removeProduct() // yêu cầu người dùng nhập vào tên sản phẩm sau đó tìm và xóa sản phẩm có tên
tương ứng trong ProductList
· iterateProductList() // hiển thị các sản phẩm trong ProductList, gọi phương thức  viewInfo() của
lớp Product, tính trung bình cộng đánh giá cho từng sản phẩm và hiển thị thông tin ra màn hình.
· searchProduct() // yêu cầu người dùng nhập vào 2 số, sau đó tìm và hiển thị thông tin của những sản
phẩm có giá nằm giữa hai số đó.
3. Tạo menu:
PRODUCT MANAGEMENT SYSTEM
1. Add new product
2. Remove product
3. Iterate product list
4. Search product
5. Exit
và thực thi các phương thức tương ứng trong lớp Shop với mỗi mục chọn


'''

class Product:
    def __init__(self,Name,DescriDption,Price,list_rate = []) -> None:
            self.Name = Name
            self.DescriDption = DescriDption
            self.Price = Price
            self.list_rate = list_rate
    def viewInfo(self):
        return "Name : {0}\tDescription : {1}\tPrice : {2}".format(\
            self.Name,self.DescriDption,self.Price)
class Shop:
    list_product = []
    def __init__(self) -> None:
        pass
    def addProduct(self):
        Name = input("Name : ")
        Description = input("Description : ")
        Price = int(input("Price :"))
        if Price < 0 or Price > 100:
            return "er Price"
        list_rates = []
        while True:
            list_rate = int(input("list rate :"))
            if list_rate < 0 and list_rate > 5:
                return "er list rate"
            list_rates.append(list_rate)
            chose = input("ấn phím bất kỳ để tiếp tục(Thoát ấn phím N) :")
            if chose == "N":
                break
            
        product = Product(Name,Description,Price,list_rates)
        self.list_product.append(product)
        return " add done "
    def removeProduct(self):
        name = input("Name ? : ")
        for item in range(len(self.list_product)):
            if self.list_product[item].Name == name:
                self.list_product.pop(item)
                print("đã xóa")
        return " remove er"
    def iterateProductList(self):
        # print(self.list_product)
        for item in self.list_product:
            sum_rate = 0
            for i in range(len(item.list_rate)):
                sum_rate = sum_rate + item.list_rate[i]
            print(item.viewInfo())
            print("Trung bình đánh giá ",float(sum_rate/(len(item.list_rate)-1)))
        # return item
    def searchProduct(self):
        number_Price1 = int(input("number Price 1 :"))
        number_Price2 = int(input("number Price 2 :"))
        for item in self.list_product:
            if item.Price > number_Price1 and item.Price < number_Price2:
                print(item.viewInfo())


if __name__ == "__main__":
    print("PRODUCT MANAGEMENT SYSTEM\
            \n1. Add new product\
            \n2. Remove product\
            \n3. Iterate product list\
            \n4. Search product\
            \n5. Exit")
    shopp = Shop()
    while True:
        try:
            chose = int(input("Input chose : "))
            if chose == 1:
                shopp.addProduct()
            elif chose == 2:
                shopp.removeProduct()
            elif chose == 3:
                shopp.iterateProductList()
            elif chose == 4:
                shopp.searchProduct()
            elif chose == 5:
                break
            else:
               print("Lỗi cú pháp vui lòng nhập lại >") 
        except:
            print("Lỗi cú pháp vui lòng nhập lại >")





    # def


    