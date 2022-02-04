"""
Bài 1: Tạo class có tên SoHoc gồm có các thuộc tính và phương thức sau:
+ Thuộc tính: number1, number2
+ Phương thức:
- Phương thức tạo __init()__
- Các phương thức get, set cho tất cả các thuộc tính
- inputInfo(): dùng để nhập 2 số number1, number2
- printInfo(): dùng để hiển thị number1, number2
- addition(): dùng để cộng number1, number2
- subtract(): trừ number1, number2
- multi(): dùng để nhân number1, number2
- division(): dùng để chia number1, number2
math 1.0.0


"""
class SoHoc():
    __number1 = None
    __number2 = None
    def __init__(self) -> None:
        pass
    def get_number1(self):
        return self.__number1
    def get_number2(self):
        return self.__number2
    def set_number1(self,number1):
        self.__number1 = number1
    def set_number2(self,number2):
        self.__number2 = number2
    def inputInfo(self):
        number_1 = int(input("enter number")) 
        number_2 = int(input("enter number")) 
        self.set_number1(number_1)
        self.set_number2(number_2)
    def printInfo(self):
        return "number1 {0} and number {1} ".format(self.get_number1(),self.get_number2())
    def addition(self):
        Sum = self.get_number1() + self.get_number2()
        return "Sum = number1 + number2 = {0} + {1} = {2}".format(self.get_number1(),self.get_number2(),Sum)
    def subtract(self):
        Sub = self.get_number1() - self.get_number2()
        return "Sub = number1 - number2 = {0} - {1} = {2}".format(self.get_number1(),self.get_number2(),Sub)
    def multi(self):
        Mul = self.get_number1() * self.get_number2()
        return "Mul = number1 * number2 = {0} * {1} = {2}".format(self.get_number1(),self.get_number2(),Mul)
    def division(self):
        Div = self.get_number1() / self.get_number2()
        return "Div = number1 / number2 = {0} / {1} = {2}".format(self.get_number1(),self.get_number2(),Div)

test = SoHoc()
test.inputInfo()
print(test.printInfo())
print(test.addition())
print(test.subtract())
print(test.multi())
print(test.division())




    
