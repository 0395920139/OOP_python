'''

Bài 13:
Mô phỏng sự hoạt dộng của một chiếc đèn pin. Với hai nhóm đối tượng cơ bản là Đèn (FlashLamp)
và Pin (Battery). Đối tượng pin mang trong mình thông tin về trạng thái năng lượng, đối tượng đèn
sữ sử dụng một đối tượng pin để cung cấp năng lượng cho hoạt động chiếu sáng.
Mô tả chi tiết lớp các đối tượng pin và đèn như sau:
Đối tượng Đèn (FlashLamp):
- status: thuộc tính thể hiện trạng thái của đèn (bật hay tắt)
- battery: thuộc tính thể hiện pin của đèn
+ FlashLamp(): hàm tạo
+ setBattery(Battery): lắp pin cho đèn
+ getBatteryInfo(): lấy thông tin pin của đèn
+ turnOn(): bật đèn
+ turnOff(): tắt đèn
Đối tượng Pin (Battery):
- energy: thuộc tính thể hiện năng lượng của pin
+ Battery(): hàm tạo
+ setEnergy(): phương thức sạc pin
+ getEnergy(): phương thức lấy năng lượng pin
+ decreaseEnergy(): phương thức tiêu hao năng lượng pin

1. Xây dựng lớp Pin (Battery) với các thuộc tính và các phương thức đã cho như trong sơ đồ trên.
Trong đó:
- Thuộc tính energy: thể hiện năng lượng của Pin.
- Hàm tạo Battery(): khởi tạo mặc định giá trị năng lượng Pin (energy) là 10
- Các phương thức:
+ setEnergy(energy): Thiết đặt lại giá trị mới cho pin (thực hiện việc sạc pin)
+ getEnergy(): Trả về thông tin năng lượng pin đang có
+ decreaseEnergy(): mỗi lần Pin được sử dụng, năng lượng của Pin sẽ giảm đi 2 đơn vị.

2. Xây dựng lớp FlashLamp với các thuộc tính và phương thức như trong sơ đồ trên. Trong đó:
- Các thuộc tính:
+ status: trạng thái của đèn, nếu status = true tức đèn được bật, ngược lại đèn tắt.
+ battery: đối tượng của Battery() là pin của đèn
- Hàm tạo:
FlashLamp(): khởi tạo trạng thái đèn tắt và chưa có pin.
- Các phương thức:
+ setBattery(b): nạp pin cho đèn, với b là đối tượng của lớp Battery()
+ getBatteryInfo(): lấy về năng lượng Pin của đèn
+ turnOn(): Chuyển trạng thái đèn là true. In ra thông tin đèn có sáng hay không (năng lượng > 0 là
sáng)
+ turnOff(): Chuyển trạng thái đèn là false. In ra thông tin: Đèn tắt.
3. Xây dựng lớp TestFlashLamp chứa phương thức main() với kịch bản như sau:
- Tạo một đối tượng Battery
- Tạo một đối tượng FlashLamp
- Lắp pin cho đèn
- Bật và tắt đèn pin 10 lần
- Hiển thị ra màn hình mức năng lượng còn lại trong pin.
'''

import time


class Battery:
    __energy = 100
    def __init__(self) -> None:
        pass
    def getEnergy(self):
        return self.__energy
    def setEnergy(self,energy):
        self.__energy = energy
    def decreaseEnergy(self,energy):
        energy = energy -2
        self.setEnergy(energy)
        return self.getEnergy()
class FlashLamp:
    status = False
    battery = Battery()
    def __init__(self) -> None:
        pass
    def setBattery(self,b):
        self.battery.setEnergy(b)
    def getBatteryInfo(self):
        return self.battery.getEnergy()
    def turnOn(self):
        self.status = True
        if self.getBatteryInfo() > 0:
            # print("============đã vào")
            energy = self.getBatteryInfo()
            self.battery.decreaseEnergy(energy)
            print(" đèn sáng")
            return " Đèn Sáng"
        print("đèn không sáng")
        return " Đèn không sáng"
    def turnOff(self):
        print("đèn tắt")
        return " đèn tắt"

class TestFlashLamp:
    # battery = Battery()
    flashLamp = FlashLamp()
    def main(self):
        for i in range(10):
            time.sleep(1)
            self.flashLamp.turnOn()
            time.sleep(1)
            self.flashLamp.turnOff()
        print("Số lượng pin còn lại trong đèn",self.flashLamp.getBatteryInfo())

test = TestFlashLamp()  
test.main()        


        






        



