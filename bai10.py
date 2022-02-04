'''

Bài 10: Xây dựng lớp số phức có các thành phần sau:
+ Các thuộc tính:
- Phần thực
- Phần ảo
+ Các hàm thành phần:
- Cộng hai số phức
- Trừ hai số phức
- Nhân hai số phức
- Chia hai số phức
Nhập vào 2 số phức và thực hiện các phép toán trên hai số phức đó.

'''

class complex_numbers:
    phanThuc = None
    phanAo = None
    def __init__(self) -> None:
        pass

    def input_complex_numbers(cls):
        cls.phanThuc = int(input("Phần Thực :"))
        cls.phanAo = int(input("Phần  ảo : "))

    def add(self):
        soPhuc1 = complex_numbers()
        soPhuc1.input_complex_numbers()
        soPhuc2 = complex_numbers()
        soPhuc2.input_complex_numbers()
        self.phanThuc = soPhuc1.phanThuc + soPhuc2.phanThuc
        self.phanAo = soPhuc1.phanAo + soPhuc2.phanAo
        return "complex numbers = {0} + ({1})i ".format(self.phanThuc,self.phanAo)
    def sub(self):
        soPhuc1 = complex_numbers()
        soPhuc1.input_complex_numbers()
        soPhuc2 = complex_numbers()
        soPhuc2.input_complex_numbers()
        self.phanThuc = soPhuc1.phanThuc - soPhuc2.phanThuc
        self.phanAo = soPhuc1.phanAo - soPhuc2.phanAo
        return "complex numbers = {0} + ({1})i ".format(self.phanThuc,self.phanAo)
    def mul(self):
        soPhuc1 = complex_numbers()
        soPhuc1.input_complex_numbers()
        soPhuc2 = complex_numbers()
        soPhuc2.input_complex_numbers()
        self.phanThuc = (soPhuc1.phanThuc*soPhuc2.phanThuc) - (soPhuc1.phanAo*soPhuc2.phanAo)
        self.phanAo = (soPhuc1.phanThuc*soPhuc2.phanAo) + (soPhuc1.phanAo*soPhuc2.phanThuc)
        return "complex numbers = {0} + ({1})i ".format(self.phanThuc,self.phanAo)
    def div(self):
        soPhuc1 = complex_numbers()
        soPhuc1.input_complex_numbers()
        soPhuc2 = complex_numbers()
        soPhuc2.input_complex_numbers()
        self.phanThuc = ((soPhuc1.phanThuc*soPhuc2.phanThuc) + (soPhuc1.phanAo*soPhuc2.phanAo))/(soPhuc2.phanThuc*soPhuc2.phanThuc + soPhuc2.phanAo*soPhuc2.phanAo)
        self.phanAo =  ((soPhuc1.phanAo*soPhuc2.phanThuc) - (soPhuc1.phanThuc*soPhuc2.phanAo))/(soPhuc2.phanThuc*soPhuc2.phanThuc + soPhuc2.phanAo*soPhuc2.phanAo)
        return "complex numbers = {0} + ({1})i ".format(self.phanThuc,self.phanAo)
      
test = complex_numbers()
add = test.add()
print(add)
