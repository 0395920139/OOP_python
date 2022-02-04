'''
Bài 2: Xây dựng lớp PhuongTrinhBacNhat (ax+b=0) với các thuộc tính a, b. Xây dựng phương thức giải phương trình bậc nhất
'''
#math 1.0.1
class PhuongTrinhBacNhat:
    __a = 0
    __b = 0
    def __init__(self) -> None:
        pass
    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b


    def set_a(self,a):
        self.__a =  a
    def set_b(self,b):
        self.__b = b

    def inputInfo(self):
        a = int(input("nhập a"))
        b = int(input("nhập b"))
        self.set_a(a)
        self.set_b(b)
        # print(self.get_a(),self.get_b())

    def Check_a(self):
        print(self.get_a(),self.get_b())
        if self.get_a() == 0:
            if self.get_b() == 0:
                return "Phương trình có tập nghiệm là R"
            return "Phương trình vô nghiệm"
        # print(cls.a,cls.b)
        # print(self.get_a(),self.get_b())
        x = -(self.get_b() / self.get_a())
        return  "Phương trình có nghiệm là x = {0}".format(x)

test = PhuongTrinhBacNhat()
test.inputInfo()
print(test.Check_a())