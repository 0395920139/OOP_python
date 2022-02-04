'''
Bài 4: Xây dựng lớp HoaDon có các thuộc tính: maHoaDon, tenSP, soluong, dongia. Xây dựng chức năng cho phép:
Lần lượt nhập thông tincủa các sản phẩm, và in ra danh sách các sản phẩm trong hóa đơn và kèm theo tổng số tiền của hóa đơn đó
'''

# from typing import List


class HoaDon:
    # __maHoaDon = None
    def __init__(self,maHoaDon,tenSP,soLuong,donGia) -> None:
        self.maHoaDon = maHoaDon
        self.tenSP = tenSP
        self.soLuong = soLuong
        self.donGia = donGia
    def show_product(self):
        return "Ma Hoa Don {0} - Ten San Pham {1} - so Luong {2} - don Gia - {3} - Tong tien {4}".format(self.maHoaDon,self.tenSP,self.soLuong,self.donGia, self.soLuong* self.donGia)


listHD = []
total = 0
while True:
    maHoaDon = input(" input ma hoa don")
    tenSP = input("ten san pham")
    soLuong = int(input("số lượng"))
    donGia = int(input("dơn giá"))

    hoaDon = HoaDon(maHoaDon,tenSP,soLuong,donGia)
    listHD.append(hoaDon)
    
    chose = input(" ban có muốn nhập nữa không Y/N")
    if chose == "N":
        break
for item in listHD:
    # print(item.show_product())
    total = total + (item.donGia*item.soLuong)
print(" tong tien ", total)