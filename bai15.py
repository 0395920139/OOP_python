'''
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


'''


# import re


from asyncio.windows_events import NULL
from pickle import TRUE
# from tabnanny import check
# from turtle import back


class BankAcount:
    def __init__(self,accountNumer,accountName) -> None:
        self.accountNumer = accountNumer
        self.accountName = accountName
        self.__balance = 0
    def getAccountNumber(self):
        return self.accountNumer
    def getaccountName(self):
        return self.accountName
    def get_balance(self):
        return self.__balance
    def deposit(self,money):
        self.__balance = self.get_balance() + money
    
class Bank:
    list_BankAcount = []
    def __init__(self) -> None:
        pass
    def search(self,account_number):
        # account_number = int(input("input account number : ")) 
        for item in range(len(self.list_BankAcount)):
            if self.list_BankAcount[item].getAccountNumber() == account_number:
                return item
        return -1
    def getTotal(self): 
        return len(self.list_BankAcount) + 1

    def getItem(self,account_number):
        # account_number = int(input("input account number : "))
        for item in self.list_BankAcount:
            if item.getAccountNumber() == account_number:
                return item
        return NULL
    def addAccount(self,accountNumber,accountName):
        ''' + addAccount(accountNumber, accountName)
            Phương thức này nhận 2 xâu ký tự lần lượt là số tài khoản và tên chủ tài khoản. Nếu số tài khoản đã
            tồn tại trong hệ thống thì hàm sẽ trả về giá trị false; ngược lại hàm sẽ thêm một tài khoản mới có
            thông tin là tham số truyền vào và trả về giá trị true.
        '''
        check_user = self.getItem(accountNumber)
        if check_user == NULL:
            bank = BankAcount(accountNumber,accountName)
            self.list_BankAcount.append(bank)
            return True
        else:
            return False
    def depositMoney(self,accountNumber, money):
    # '''
    #     + depositMoney(accountNumber, money)
    #     Thực hiện nạp tiền vào tài khoản; nếu tồn tại số tài khoản trong hệ thống thì cập nhật lại số tiền của
    #     tài khoản và trả về giá trị true, ngược lại trả về false
    # '''

        check_user = self.getItem(accountNumber)
        if check_user == NULL:
            return False
        else:
            check_user.deposit(money)
            return True
    def withdrawMoney(self,accountNumber, money):
        '''
         + withdrawMoney(accountNumber, money)

        Thực hiện rút tiền từ tài khoản; nếu tồn tại số tài khoản trong hệ thống và số tiền trong tài khoản >=
        số tiền cần rút thì cập nhật lại số tiền của tài khoản và trả về giá trị true, ngược lại trả về false.        
        '''
        check_user = self.getItem(accountNumber)
        if check_user == NULL:
            return NULL
        else:
            if check_user.get_balance() >= money:
                check_user.deposit(-money)
                return True
            return False
    def removeAccount(self,accountNumber):
        '''
            + removeAccount(accountNumber)
            Loại bỏ tài khoản có số tài khoản được truyền vào khỏi danh sách; nếu không tồn tại tài khoản nào
            có số tài khoản đó thì trả về false; ngược lại trả về true.  
        '''
        check_user = self.search(accountNumber)
        if check_user == -1:
            return False
        self.list_BankAcount.pop(check_user)
        return True
    def create_bank_account(self):
        accountNumber = int(input(" Nhập Số tài khoản : "))
        accountName = input("Nhập tên tài khoản :")
        user = self.addAccount(accountNumber,accountName)
        if user == False:
            return "tài khoản đã tồn tại"
        return " Đã Đăng kí thành công"
    def show_bank_account(self):
        accountNumber = int(input(" Nhập Số tài khoản : "))
        user = self.getItem(accountNumber)
        if user == NULL:
            return " Tài khoản chưa tồn tại "
        else:
            data = "Card : " + str(user.getAccountNumber()) + "| Name : " + user.getaccountName() + "| balance : "+ str(user.get_balance())
            return data
    # def deposit_money()
# show_bank
# showBank

'''
Hãy xây dựng chương trình quản lý ngân hàng với các chức năng sau:
    + nhập thông tin số tài khoản có trong ngân hàng nếu có thì in ra danh sách chức năng,
        nếu không có hiện thông báo bạn có muốn tạo tài khoảng không ?
    + Đăng kí tài khoản nếu chưa có


'''

if __name__ == "__main__":
    bank = Bank()
    while True:
        try:
            print("-------------------------------------------------")
            print("MigorBank ")
            print("1. Nhập số tài khoản hiện có trong Ngân Hàng   :")
            print("2. Đăng kí số tài khoản trong Ngân Hàng        :")
            print("3. Nạp tiền vào tài khoản                      :")
            print("4. Rút tiền khỏi tài khoản                     :")
            print("5. Xóa tài khoản                               :")
            print("6. kết thúc                                    :")
            chose = int(input(" Vui Lòng nhập lựa chọn "))
            if chose == 1:
                print("------------------------------------------------------")
                print("---------",bank.show_bank_account())
            elif chose == 2:
                print(bank.create_bank_account())
            elif chose == 3:
                print("----------------------------------------")
                accountNumber = int(input("Nhập số tài khoản muốn nạp"))
                money = int(input("Nhập số tiền muốn nạp"))
                check = bank.depositMoney(accountNumber,money)
                if check:
                    print(" Nạp thành công ")
                else:
                    print(" tài khoản không tồn tại")
            elif chose == 4:
                print("----------------------------------------")
                accountNumber = int(input("Nhập số tài khoản muốn rút"))
                money = int(input("Nhập số tiền muốn rút"))
                check = bank.withdrawMoney(accountNumber,money)
                if check == True:
                    print("Rút thành công")
                elif check == NULL:
                    print("Tài khoản không tồn tại")
                else:
                    print("Số tiền không đủ để rút ")
            elif chose == 5:
                print("----------------------------------------")
                accountNumber = int(input("Nhập số tài khoản muốn rút"))
                check = bank.removeAccount(accountNumber)
                if check:
                    print("xóa thành công ")
                else:
                    print("tài khoản k tồn tại")
            elif chose == 6:
                break
        except:
            print(" Nhập sai định dạng  ")
    print(" cảm ơn đã sử dụng sản phẩm của chúng tôi : ")

        # pass
        

    
    




    
    