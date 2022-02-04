'''
Bài 7: Xây dựng lớp tam giác (Triangle) có các thành phần:
* Các thuộc tính: 3 cạnh a, b, c của tam giác.
* Các phương thức:
- Nhập độ dài 3 cạnh
- Xác định kiểu tam giác
- Tính chu vi tam giác
- Tính diện tích tam giác

'''
import math
class Triangle:
    def __init__(self,a,b,c) -> None:
        self.a = a
        self.b = b
        self.c = c
    def check_Triangle(self):
        if self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b:
            print( "Triangle ")
            if self.a*self.a==self.b*self.b+self.c*self.c or self.b*self.b==self.a*self.a+self.c*self.c or self.c*self.c== self.a*self.a+self.b*self.b:
                print( "tam giac vuong")
            if self.a == self.b  and self.a == self.c:
                print(" tam giac dều")
            if self.a == self.b or self.a == self.c or self.b == self.c:
                print("tam giac can")
        else:
            print("k la tam giac")
    def chuVi(self):
        return self.a + self.b + self.c
    def DienTich(self):
        C = self.chuVi()/2
        if C < 0:
            return " khong co"
        S = math.sqrt(C*(C-self.a)*(C-self.b)*(C-self.c))
        return S
test = Triangle(3,2,3)
test.check_Triangle()
print(test.chuVi())
print(test.DienTich())
