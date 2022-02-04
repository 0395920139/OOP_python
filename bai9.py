'''
Bài 9: Xây dựng lớp Phân số (Fraction) có các thành phần sau:
* Các thuộc tính: Tử số, mẫu số.
* Phương thức tạo để khởi tạo giá trị cho tử số và mẫu số.
* Các phương thức setter và getter.
* Các phương thức:
- Nhập phân số
- In Phân số
- Rút gọn phân số
- Nghịch đảo phân số
- add(), sub(), mul(), div() tương ứng để thực hiện cộng, trừ, nhân, chia hai phân số cho nhau
'''
# from _typeshed import Self


def greatest_common_divisor(a,b):
        if b == 0:
            return a
        return greatest_common_divisor(b,a%b)  
class Fraction:
    _Numerator = None
    _Denominator = None
    def __init__(self) -> None:
        pass
    def get_Denominator(self):
        return self._Denominator
    def get_Numerator(self):
        return self._Numerator
    def set_Denominator(self,Denominator):
        self._Denominator = Denominator
    def set_Numerator(self,Numerator):
        self._Numerator = Numerator
    def input_fraction(self):
        Numerator = int(input("input Numerator "))
        Denominator = int(input("input Denominator"))
        self.set_Denominator(Denominator)
        self.set_Numerator(Numerator)
    def show_fraction(self):
        return "Fraction = {0}/{1}".format(self.get_Numerator(),self.get_Denominator())    
    def simplify_fractions(self):
        UCLN = greatest_common_divisor(self.get_Numerator(),self.get_Denominator())
        new_numerator = self.get_Numerator()/UCLN
        new_denominator =self.get_Denominator()/UCLN
        return "Simplify Fractions = {0}/{1}".format(new_numerator,new_denominator)
    def inverse_fractions(self):
        return "inverse fractions = {0}/{1}".format(self.get_Denominator(),self.get_Numerator())   
    def add(self):
        Numerator1 = int(input("input Numerator 1"))
        Denominator1 = int(input("input Denominator 1"))
        Numerator2 = int(input("input Numerator 2"))
        Denominator2 = int(input("input Denominator 2"))
        add_Fraction_Numerator = (Numerator1*Denominator2) +(Denominator1*Numerator2)
        add_Fraction_Denominator = Denominator1*Denominator2
        UCLN = greatest_common_divisor(add_Fraction_Numerator,add_Fraction_Denominator)
        new_numerator = add_Fraction_Numerator/UCLN
        new_denominator = add_Fraction_Denominator/UCLN
        return "add Fractions = {0}/{1}".format(new_numerator,new_denominator)
    def sub(self):
        Numerator1 = int(input("input Numerator 1"))
        Denominator1 = int(input("input Denominator 1"))
        Numerator2 = int(input("input Numerator 2"))
        Denominator2 = int(input("input Denominator 2"))
        sub_Fraction_Numerator = (Numerator1*Denominator2) +(Denominator1*Numerator2)
        sub_Fraction_Denominator = Denominator1*Denominator2
        UCLN = greatest_common_divisor(sub_Fraction_Numerator,sub_Fraction_Denominator)
        new_numerator = sub_Fraction_Numerator/UCLN
        new_denominator = sub_Fraction_Denominator/UCLN
        return "sub Fractions = {0}/{1}".format(new_numerator,new_denominator)
    def mul(self):
        Numerator1 = int(input("input Numerator 1"))
        Denominator1 = int(input("input Denominator 1"))
        Numerator2 = int(input("input Numerator 2"))
        Denominator2 = int(input("input Denominator 2"))
        mul_Fraction_Numerator = Numerator1*Numerator2
        mul_Fraction_Denominator = Denominator1*Denominator2
        UCLN = greatest_common_divisor(mul_Fraction_Numerator,mul_Fraction_Denominator)
        new_numerator = mul_Fraction_Numerator/UCLN
        new_denominator = mul_Fraction_Denominator/UCLN
        return "mul Fractions = {0}/{1}".format(new_numerator,new_denominator)
    def div(self):
        Numerator1 = int(input("input Numerator 1"))
        Denominator1 = int(input("input Denominator 1"))
        Numerator2 = int(input("input Numerator 2"))
        Denominator2 = int(input("input Denominator 2"))
        div_Fraction_Numerator = Numerator1*Denominator2
        div_Fraction_Denominator = Denominator1*Numerator2
        UCLN = greatest_common_divisor(div_Fraction_Numerator,div_Fraction_Denominator)
        new_numerator = div_Fraction_Numerator/UCLN
        new_denominator = div_Fraction_Denominator/UCLN
        return "div Fractions = {0}/{1}".format(new_numerator,new_denominator)
        # Denominator = int(input("input Denominator 1"))
test = Fraction()
test.input_fraction()
print(test.show_fraction())
print(test.simplify_fractions())
print(test.inverse_fractions())
print(test.add())
print(test.sub())
print(test.div())
print(test.mul())

