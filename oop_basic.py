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

Bài 2: Xây dựng lớp PhuongTrinhBacNhat (ax+b=0) với các thuộc tính a, b. Xây dựng phương thức giải phương trình bậc nhất

Bài 3: Xây dựng lớp PhuongTrinhBac2 (ax^2+bx + x=0) với các thuộc tính a, b, c. Xây dựng phương thức giải phương trình bậc 2

Bài 4: Xây dựng lớp HoaDon có các thuộc tính: maHoaDon, tenSP, soluong, dongia. Xây dựng chức năng cho phép:
Lần lượt nhập thông tincủa các sản phẩm, và in ra danh sách các sản phẩm trong hóa đơn và kèm theo tổng số tiền của hóa đơn đó

Bài 5: Viết class NhanVien gồm các thuộc tính:
+ Tên
+ Tuổi
+ Địa chỉ
+ Tiền lương
+ Tổng số giờ làm
Và các phương thức:
- Phương thức tạo
- inputInfo() : Nhập các thông tin cho nhân viên từ bàn phím
- printInfo() : In ra tất cả các thông tin của nhân viên
- tinhThuong(): Tính toán và trả về số tiền thưởng của nhân viên theo công thức sau:
Nếu tổng số giờ làm của nhân viên >=200 thì thưởng = lương * 20%
Nếu tổng số giờ làm của nhân viên <200 và >=100 thì thưởng = lương * 10%
Nếu tổng số giờ làm của nhân viên <100 thì thưởng = 0

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

Bài 7: Xây dựng lớp tam giác (Triangle) có các thành phần:
* Các thuộc tính: 3 cạnh a, b, c của tam giác.
* Các phương thức:
- Nhập độ dài 3 cạnh
- Xác định kiểu tam giác
- Tính chu vi tam giác
- Tính diện tích tam giác
Bài 8:
Xây dựng lớp hình chữ nhật (Rectangle) có các thành phần sau:
* Các thuộc tính: chiều dài, chiều rộng.
* Các phương thức:
- Nhập chiều dài, chiều rộng
- Tính diện tích
- Tính chu vi

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

Bài 12:
Xây dựng lớp đa giác, hình bình hành thừa kế từ đa giác, hình chữ nhật thừa kế từ hình bình hành và
hình vuông thừa kế từ hình chữ nhật. Nhập vào các thuộc tính cần thiết của mỗi hình và tính chu vi,
diện tích của hình đó.

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

Bài 14:
1. Tạo một lớp có tên Product bao gồm các thuộc tính và phương thức sau:
· Name
· Description
· Price // 0 < Price <= 100
· list rate // lưu các đánh giá của người dùng cho sản phẩm, giá trị từ 1 - 5
· viewInfo() // hiển thị tên, giá và mô tả về sản phẩm
2. Tạo lớp Shop gồm các thuộc tính và phương thức sau:
· List ProductList // lưu danh sách các sản phẩm của shop
· addProduct()  // yêu cầu người dùng nhập thông tin của sản phẩm rồi lưu vào ProductList
· removeProduct() // yêu cầu người dùng nhập vào tên sản phẩm sau đó tìm và xóa sản phẩm có tên
tương ứng trong ProductList
· iterateProductList() // hiển thị các sản phẩm trong ProductList, gọi phương thức  viewInfo() của
lớp Product, tính trung bình cộng đánh giá cho từng sản phẩm và hiển thị thông tin ra màn hình.
· searchProduct() // yêu cầu người dùng nhập vào 2 số, sau đó tìm và hiển thị thông tin của những sản
phẩm có giá nằm giữa hai số đó.
3. Tạo menu:
PRODUCT MANAGEMENT SYSTEM
1. Add new product
2. Remove product
3. Iterate product list
4. Search product
5. Exit
và thực thi các phương thức tương ứng trong lớp Shop với mỗi mục chọn

Bài 15: 
Hãy cài đặt lớp BankAcount theo mô tả như dưới đây:
    - accountNumber : Số tài khoản ngân hàng
    - accountName : Tên chủ tài khoản
    - balance : Số tiền có trong tài khoản
    + BankAccount(accountName, accountNumber): Phương thức thiết lập để tạo tài khoản với số tiền
    =0; tên tài khoản và số tài khoản là tham số truyền vào.
    + getAccountNumber() : Lấy về thông tin số tài khoản
    + getAccountName() : Trả về tên chủ tài khoản
    + getBalance() : Trả về số tiền hiện có trong tài khoản
    + deposit(money): Nạp tiền vào tài khoản
    Hãy cài đặt lớp Bank như mô tả dưới đây
    + list BankAccount
    Chứa danh sách các tài khoản hiện có tại ngân hàng.
    Có 7 phương thức được mô tả như dưới đây:
    + search(accountNumber)
    Phương thức này trả về chỉ số của tài khoản ngân hàng có số tài khoản là tham số trong list; nếu
    không  tồn tại tài khoản nào có số tài khoản như tham số thì hàm trả về -1.
    + getTotal()
    Phương thức này trả về số lượng tài khoản hiện có tại ngân hàng.
    + getItem(accountNumber)
    Phương thức này nhận tham số đầu vào là số tài khoản ngân hàng, và trả về đối tượng BankAccount
    có số tài khoản là tham số truyền vào; nếu số tài khoản không hợp lệ hàm sẽ trả về giá trị null.
    + addAccount(accountNumber, accountName)
    Phương thức này nhận 2 xâu ký tự lần lượt là số tài khoản và tên chủ tài khoản. Nếu số tài khoản đã
    tồn tại trong hệ thống thì hàm sẽ trả về giá trị false; ngược lại hàm sẽ thêm một tài khoản mới có
    thông tin là tham số truyền vào và trả về giá trị true.
    + depositMoney(accountNumber, money)
    Thực hiện nạp tiền vào tài khoản; nếu tồn tại số tài khoản trong hệ thống thì cập nhật lại số tiền của
    tài khoản và trả về giá trị true, ngược lại trả về false
    + withdrawMoney(accountNumber, money)

    Thực hiện rút tiền từ tài khoản; nếu tồn tại số tài khoản trong hệ thống và số tiền trong tài khoản >=
    số tiền cần rút thì cập nhật lại số tiền của tài khoản và trả về giá trị true, ngược lại trả về false.
    + removeAccount(accountNumber)
    Loại bỏ tài khoản có số tài khoản được truyền vào khỏi danh sách; nếu không tồn tại tài khoản nào
    có số tài khoản đó thì trả về false; ngược lại trả về true.
    Hãy xây dựng chương trình quản lý ngân hàng với các chức năng sau:
    Nhập một danh sách các tài khoản hiện có của ngân hàng
    Sinh ngẫu nhiên số tiền trong tài khoản cho các tài khoản hiện có trong hệ thống
    Hiển thị ra màn hình thông tin các tài khoản cho ngân hàng
    Nạp thêm 500 triệu đồng cho số tài khoản 1050008855
    Thực hiện rút 30 triệu đồng từ tài khoản 1050008854
    Hiển thị in ra màn hình thông báo số dư và tình trạng giao dịch sau khi thực hiện nạp và rút tiền
    tại các tài khoản ở trên.

=> QUan hệ giữa Bank và BankAccount: 1 Bank có nhiều BankAccount

Bài 16: 
Xây dựng một lớp có tên So gồm các thuộc tính và phương thức sau:
    + Các thuộc tính:
    number
    + Các phương thức:
    Các phương thức tạo không tham số, đầy đủ tham số
    Các phương thức getter, setter
    inputNumber() để nhập liệu
    showNumber() để hiển thị
    kiemTraNguyen() để kiểm tra number có phải số nguyên không
    kiemTraChanLe()
    kiemTraAmDuong()
    kiemTraChanDuong()
    kiemTraLeAm()

Bài 18:
Câu 1:
    Tạo lớp Person chứa thông tin
    - Tên
    - Giới tính
    - Ngày sinh
    - Địa chỉ
    1. Viết phương thức inputInfo(), nhập thông tin Person từ bàn phím
    2. Viết phương thức showInfo(), hiển thị tất cả thông tin Person
Câu 2:
    Tạo lớp Student thừa kế Person, lưu trữ các thông tin một sinh viên
    - Mã sinh viên: chứa 8 kí tự
    - Điểm trung bình: từ 0.0 – 10.0
    - Email: phải chứa kí tự @ và không tồn tại khoảng trắng
    1. Override phương thức inputInfo(), nhập thông tin Student từ bàn phím
    2. Override phương thức showInfo(), hiển thị tất cả thông tin Student
    3. Viết phương thức xét xem Student có được học bổng không? Điểm trung bình trên 8.0 là
    được học bổng
Câu 3:
    Tạo lớp StudentTest để kiểm tra chức năng của lớp Student
    Tạo Menu chọn như sau:
    a. Chọn 1: Nhập vào n sinh viên (n là số lượng sinh viên, được nhập từ bàn phím)
    b. Chọn 2: Hiển thị thông tin tất cả các sinh viên ra màn hình
    c. Chọn 3: Hiển thị sinh viên có điểm trung bình cao nhất và sinh viên có điểm trung bình
    thấp nhất
    d. Chọn 4: Tìm kiếm sinh viên theo mã sinh viên. Nhập vào mã sinh viên. Nếu tồn tại sinh viên
    có mã đó thì in ra màn hình thông tin sinh viên. Nếu không tồn tại thì in ra: Không có sinhviên
    nào có mã là <giá trị của mã sinh viên>
    e. Chọn 5: Hiển thị tất cả các sinh viên theo thứ tự tên trong bảng chữ cái (A->Z)
    f. Chọn 6: Hiển thị tất cả các sinh viên được học bổng, và sắp xếp theo thứ tự điểm cao
    xuống thấp
    g. Chọn 7: Thoát

Câu 4:
    Tạo lớp Teacher, kế thừa từ Person, lưu trữ thông tin một giảng viên
    - Lớp dạy (phải bắt đầu bằng 1 trong các chữ: G, H, I, K, L, M)
    - Lương một giờ dạy
    - Số giờ dạy trong tháng
    1. Override phương thức inputInfo(), nhập thông tin Teacher từ bàn phím
    2. Override phương thức showInfo(), hiển thị tất cả thông tin Teacher
    3. Viết phương thức tính lương thực nhận, trả về lương thực nhận theo công thức:

    Nếu lớp dạy là lớp buổi sáng và chiều (Giờ G, H, I, K) thì
    Lương thực nhận = lương một giờ dạy * số giờ dạy trong tháng;
    Nếu lớp dạy là lớp buổi tối (Giờ L, giờ M) thì
    Lương thực nhân = lương một giờ dạy * số giờ dạy trong tháng + 200000đ;
Câu 5:
    Tạo lớp TeacherTest, chứa hàm Main kiểm tra chức năng của Teacher
    Tạo menu lựa chọn như sau:
    a. Chọn 1: Nhập vào n giảng viên (n là số lượng sinh viên, được nhập từ bàn phím)
    b. Chọn 2: Hiển thị thông tin tất cả các giảng viên ra màn hình
    c. Chọn 3: Hiển thị giảng viên có lương cao nhất
    d. Chọn 4: Thoát

Bài 19:
    1. Tạo lớp có tên Animal gồm các thuộc tính và phương thức:
    · Ten
    · Tuoi
    · MoTa
    · xemThongTin() //hiển thị loại, tên, tuổi và mô tả của động vật
    · tiengKeu()
    2. Tạo các lớp Tiger, Dog, Cat theo các yêu cầu sau:
    Thừa kế từ lớp Animal
    Ghi đè phương thức tiengKeu() để thể hiện những tiếng kêu đặc trưng của từng loài vật
    3. Tạo lớp có tên Chuong gồm:
    · maChuong
    · Một list có tên AnimalList
    · themConVat(animal) //thêm một con vật vào AnimalList
    · xoaConVat(ten) //xóa con vật có tên tương ứng khỏi AnimalList
    4. Tạo lớp có tên Zoo gồm:
    · Một list có tên DanhSachChuong
    · themChuong(chuong) //thêm chuồng vào DanhSachChuong
    · xoaChuong(machuong) //xóa chuồng có mã tương ứng khỏi DanhSachChuong
    5. Tạo lớp có tên TestZoo chứa phương thức main() để quản lý sở thú theo dạng Menu như
    sau:
        1. Thêm chuồng
        2. Xóa chuồng
        3. Thêm con vật
        4. Xóa con vật
        5. Xem tất cả các con vật
        6. Thoát
    6. Khi người dùng chọn 3 thì yêu cầu người dùng nhập vào loại con vật muốn thêm (Tiger,
    Dog, Cat) rồi nhập các thông tin của con vật và thêm vào AnimaList.
    7. Khi người dùng chọn 5 thì hiển thị thông tin cùng tiếng kêu của từng con vật trong sở thú


"""