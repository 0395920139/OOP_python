

'''
Bài 16: 
Xây dựng một lớp có tên So gồm các thuộc tính và phương thức sau:
    + Các thuộc tính:
    number
    + Các phương thức:
    Các phương thức tạo không tham số, đầy đủ tham số
    Các phương thức getter, setter
    inputNumber() để nhập liệu
    showNumber() để hiển thị
    kiemTraNguyen() để kiểm tra number có phải số nguyên không
    kiemTraChanLe()
    kiemTraAmDuong()
    kiemTraChanDuong()
    kiemTraLeAm()
'''



class so:
    __number = None
    def __init__(self) -> None:
        pass
    def getter(self):
        return self.__number
    def setter(self,number):
        self.__number = number
    def inputNumber(self):
        number = int(input("input number"))
        self.setter(number)
    def showNumber(self):
        return self.getter()
    def KiemTraNguyen(self):
        if self.getter() == int(self.getter()):
            return " Là Số nguyên"
        else:
            return "không phải là số nguyên"
    def kiemTraChanLe(self):
        check = self.getter()/2
        if check == int(check):
            return " là số chẵn"
        else:
            return " là số lẻ "
    def kiemTraAmDuong(self):
        if self.getter() > 0:
            print("là số dương")
        elif self.getter() < 0:
            print("là số âm")
        else:
            print(" là số 0")