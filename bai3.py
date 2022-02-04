'''
Bài 3: Xây dựng lớp PhuongTrinhBac2 (ax^2+bx + x=0) với các thuộc tính a, b, c. Xây dựng phương thức giải phương trình bậc 2
'''
import math

class PhuongTrinhBac2:
    def __init__(self,a,b,c) -> None:
        self.a = a
        self.b = b
        self.c = c
        # self.deta = b*b - (4*a*c)
    def GiaiPuongTrinh(self):
        deta = self.b*self.b - (4*self.a*self.c)
        print(deta)
        if self.a == 0:
            return "PT không hợp lệ"
        if deta > 0:
            x1 = (-self.b - math.sqrt(deta)/(2*self.a))
            x2 = (-self.b + math.sqrt(deta)/(2*self.a))
            return 'pt có 2 nghiệm x1 = {0} , x2 = {1}'.format(x1,x2)
        if deta == 0:
            return "pt có nghiệm duy nhất là x{0}".format((-self.b)/self.a)
        return "Pt vô nghiệm"

test = PhuongTrinhBac2(1,5,2)
print(test.GiaiPuongTrinh())