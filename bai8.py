'''
Bài 8:
Xây dựng lớp hình chữ nhật (Rectangle) có các thành phần sau:
* Các thuộc tính: chiều dài, chiều rộng.
* Các phương thức:
- Nhập chiều dài, chiều rộng
- Tính diện tích
- Tính chu vi


'''

class Rectangle:
    __width = None
    __height = None
    def __init__(self) -> None:
        pass
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
    def set_width(self,width):
        self.__width = width
    def set_height(self,height):
        self.__height = height
    def input_info(self):
        width = int(input("input width : ")) 
        height = int(input("input height : "))
        self.set_width(width)
        self.set_height(height)
    def acreage(self):
        return "Acreage rectangle = {0}".format(self.get_width()*self.get_height())
    def perimeter(self):
        return "perimeter rectangle = {0}".format(2*(self.get_height()+self.get_width()))
test = Rectangle()
test.input_info()
print(test.acreage())
print(test.perimeter())