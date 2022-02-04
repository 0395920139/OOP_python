
'''

Bài 5: Viết class NhanVien gồm các thuộc tính:
+ Tên
+ Tuổi
+ Địa chỉ
+ Tiền lương
+ Tổng số giờ làm
Và các phương thức:
- Phương thức tạo
- inputInfo() : Nhập các thông tin cho nhân viên từ bàn phím
- printInfo() : In ra tất cả các thông tin của nhân viên
- tinhThuong(): Tính toán và trả về số tiền thưởng của nhân viên theo công thức sau:
Nếu tổng số giờ làm của nhân viên >=200 thì thưởng = lương * 20%
Nếu tổng số giờ làm của nhân viên <200 và >=100 thì thưởng = lương * 10%
Nếu tổng số giờ làm của nhân viên <100 thì thưởng = 0

'''

from os import name


class NhanVien:
    def __init__(self) -> None:
        pass
    def inputInfo(self):
        name = input("input name")
        age = int(input("age"))
        address = input(" address")
        salary = int(input('salary'))
        totalTime = int(input('totalTime'))
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary
        self.totalTime = totalTime
        # NhanVien(name,age,address,salary,totalTime)
    def showInfo(self):
        return "Name {0} - age {1} - address - {2} - salary - {3} - totalTime {4}h".format(self.name,self.age,self.address,self.salary,self.totalTime)
    def Bonus(self):
        if self.totalTime >= 200 :
            return "Bonus {0}".format(self.salary*0.2)
        if self.totalTime >= 100:
            return "Bonus {0}".format(self.salary*0.1)
        return "No Bonus"
test = NhanVien()
test.inputInfo()
print(test.showInfo())
print(test.Bonus())