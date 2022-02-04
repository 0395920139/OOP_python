'''
Bài 11:
Xây dựng lớp Vectơ có các thành phần sau:
+ Các thuộc tính:
- Hoành độ đầu
- Tung độ đầu
- Hoành đô cuối
- Tung độ cuối
+ Các phương thức:
- Kiểm tra hai vectơ có bằng nhau không?
- Tính góc giữa 2 vectơ
- Tính module của 2 vectơ
- Kiểm tra hai vectơ có cùng phương không?
- Cộng hai vectơ
- Trư hai vectơ
- Nhân hai vectơ
Nhập vào 2 vectơ và thực hiện các phép toán trên hai vectơ đó.
'''
import math

# from oop_Python1.embi.bai11 import vecto

def greatest_common_divisor(a,b):
        if b == 0:
            return a
        return greatest_common_divisor(b,a%b)  

class Vecto:
    x_head = None
    y_head = None
    x_last = None
    y_last = None
    def __init__(self) -> None:
        pass
    def input_vecto(self):
        self.x_head = int(input("input x Head : " ))
        self.y_head = int(input("input y Head : " ))
        self.x_last = int(input("input x last : " ))
        self.y_last = int(input("input y last : " ))
    def length_verto(self, x1,y1,x2,y2):
        data = math.sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2))
        return data
    def linear_equation(self, x1,y1,x2,y2):
        a = (y2 - y1)/(x2 -x1)
        b = y1 - (a*x1)
        return a,b
    def equal_verto(self):
        verto1 = Vecto()
        verto1.input_vecto()
        verto2 = Vecto()
        verto2.input_vecto()
        if self.length_verto(verto1.x_head,verto1.y_head,verto1.x_last,verto1.y_last) == self.length_verto(verto2.x_head,verto2.y_head,verto2.x_last,verto2.y_last):
            a1,b1 = self.linear_equation(verto1.x_head,verto1.y_head,verto1.x_last,verto1.y_last)
            a2,b2 = self.linear_equation(verto2.x_head,verto2.y_head,verto2.x_last,verto2.y_last)
            if greatest_common_divisor(a1,a2) == greatest_common_divisor(b1,b2):
                return "2 verto bằng nhau"
        return " 2 verto không bằng nhau"
    def goc_verto(self):
        verto1 = Vecto()
        verto1.input_vecto()
        verto2 = Vecto()
        verto2.input_vecto()
        a1,b1 = self.linear_equation(verto1.x_head,verto1.y_head,verto1.x_last,verto1.y_last)
        a2,b2 = self.linear_equation(verto2.x_head,verto2.y_head,verto2.x_last,verto2.y_last)
        mau = math.sqrt(a1*a1 + b1*b1)*math.sqrt(a2*a2+b2*b2)
        data = (a1*a2 + b1*b2)/mau
        goc = math.acos(data)
        return goc
    def module_verto(self):
        pass
    def verto_cung_phuong(self):
        verto1 = Vecto()
        verto1.input_vecto()
        verto2 = Vecto()
        verto2.input_vecto()
        a1,b1 = self.linear_equation(verto1.x_head,verto1.y_head,verto1.x_last,verto1.y_last)
        a2,b2 = self.linear_equation(verto2.x_head,verto2.y_head,verto2.x_last,verto2.y_last)
        if greatest_common_divisor(a1,a2) == greatest_common_divisor(b1,b2):
            return "2 verto cùng phương"
        return " 2 verto khác phương"
    def add(self):
        verto1 = Vecto()
        verto1.input_vecto()
        verto2 = Vecto()
        verto2.input_vecto()
        a1,b1 = self.linear_equation(verto1.x_head,verto1.y_head,verto1.x_last,verto1.y_last)
        a2,b2 = self.linear_equation(verto2.x_head,verto2.y_head,verto2.x_last,verto2.y_last)
        new_a = a1+ a2
        new_b = b1 + b2
        return new_a,new_b
    def sub(self):
        verto1 = Vecto()
        verto1.input_vecto()
        verto2 = Vecto()
        verto2.input_vecto()
        a1,b1 = self.linear_equation(verto1.x_head,verto1.y_head,verto1.x_last,verto1.y_last)
        a2,b2 = self.linear_equation(verto2.x_head,verto2.y_head,verto2.x_last,verto2.y_last)
        new_a = a1 - a2
        new_b = b1 - b2
        return new_a,new_b

    def mul(self):
        verto1 = Vecto()
        verto1.input_vecto()
        verto2 = Vecto()
        verto2.input_vecto()
        a1,b1 = self.linear_equation(verto1.x_head,verto1.y_head,verto1.x_last,verto1.y_last)
        a2,b2 = self.linear_equation(verto2.x_head,verto2.y_head,verto2.x_last,verto2.y_last)
        mau = math.sqrt(a1*a1 + b1*b1)*math.sqrt(a2*a2+b2*b2)
        data = (a1*a2 + b1*b2)/mau
        # goc = math.acos(data)
        length_verto1 = self.length_verto(verto1.x_head,verto1.y_head,verto1.x_last,verto1.y_last)
        length_verto2 =self.length_verto(verto2.x_head,verto2.y_head,verto2.x_last,verto2.y_last)
        mul_verto = length_verto1*length_verto2*data
        return mul_verto

    


if __name__ == "__main__":
    test =Vecto()
    test.goc_verto()