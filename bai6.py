'''
Bài 6: Tạo lớp Student, lưu trữ các thông tin một sinh viên:
- Mã sinh viên: chứa 8 kí tự
- Điểm trung bình: từ 0.0 – 10.0
- Tuổi: Phải lớn hơn hoặc bằng 18
- Lớp: Phải bắt đầu bởi kí tự ‘A’ hoặc kí tự ‘C’
a. Phương thức tạo
b. Phương thức inputInfo(), nhập thông tin Student từ bàn phím
c. Phương thức showInfo(), hiển thị tất cả thông tin Student
d. Viết phương thức xét xem Student có được học bổng không? Điểm trung bình trên 8.0 là
được học bổng
'''

from os import path


class Student:
    def __init__(self) -> None:
        pass
    def inputInfo(self):
        studentNo = input("input studentNo")
        if len(studentNo) == 8:
            self.studentNo = studentNo
        else:
            print("er studentNo")
            return "er studentNo"
        averageScore = float(input("input averageScore"))
        if averageScore >=0.0 and averageScore <=10.0:
            self.averageScore = averageScore
        else:
            print("er averageScore")
            return " er averageScore "
        age = int(input("input age "))
        if age >= 18:
            self.age = age
        else:
            return "er age "
        classNo = input("input classNo")

        if classNo.startswith("A") or classNo.startswith("C"):
            self.classNo = classNo
        else:
            return"er classNo"
    def showInfo(self):
        return "studentNo {0} - age {1} - averageScore {2} - classNo {3}".format(self.studentNo,self.age,self.averageScore,self.classNo)
    def scholarship(self):
        if self.averageScore >= 8.0:
            return "studentNo {0}-  averageScore {1} - scholarship".format(self.studentNo,self.averageScore)
        return "No scholarships"
test = Student()
test.inputInfo()
print(test.showInfo())
print(test.scholarship())
        
