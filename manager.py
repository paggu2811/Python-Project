from menu_manage import MenuManage
from table_manage import TableManage
from order_manage import OrderManage
from user_manage import UserManage
from colors import Color, color_text
from hashlib import sha256  


def encrypt_password(password):
    return sha256(password.encode()).hexdigest()

class ManagerMenu:
    def __init__(self, uname):
        mm, tm, om, um = MenuManage(), TableManage(uname), OrderManage(), UserManage()
        while True:
            print(color_text("""
******** 👨‍💼  Welcome To Manager Menu *******
1️⃣ Menu
2️⃣ Table
3️⃣ Order
4️⃣ User
5️⃣ Change My Password
6️⃣ Exit
*********************************************
""", Color.HEADER))
            ch = input("👉 Choice: ")
            if ch == "1":
                self.menu_block(mm)
            elif ch == "2":
                self.table_block(tm)
            elif ch == "3":
                self.order_block(om)
            elif ch == "4":
                self.user_block(um)
            elif ch == "5":
                self.change_pass(uname)
            elif ch == "6":
                print(color_text("👋 Bye!", Color.YELLOW))
                break
            else:
                print(color_text("⚠️ Bad choice. Please Select Correct Choice ", Color.RED))

    def menu_block(self, mm):
        opt = input("(a)dd (u)pdate (d)elete (s)how (f)ind ? ")
        if opt == "a":
            mm.add_dish()
        elif opt == "u":
            mm.upd_dish()
        elif opt == "d":
            mm.del_dish()
        elif opt == "s": 
            mm.show_all()
        elif opt == "f": 
            mm.search()

    def table_block(self, tm):
        opt = input("(b)ook (c)ancel (s)how ? ")
        if opt == "b":
            tm.book_table()
        elif opt == "c": 
            tm.cancel_table()
        elif opt == "s":
            tm.show_all_tables()

    def order_block(self, om):
        opt = input("(n)ew (c)ancel (s)how ? ")
        if opt == "n": 
            om.new_order()
        elif opt == "c":
            om.cancel_order()
        elif opt == "s":
            om.show_all_orders()

    def user_block(self, um):
        opt = input("(a)dd (u)pdate (d)elete (s)how ? ")
        if opt == "a": 
            um.add_user()
        elif opt == "u":
            um.upd_user()
        elif opt == "d":
            um.del_user()
        elif opt == "s":
            um.show_all()

    def change_pass(self, uname):
        um = UserManage()
        lines = um._read()
        new = []
        done = False
        for ln in lines:
            p = ln.split(", ")
            if p[1] == uname:
                new_pw = input("🔐 New password: ")
                p[2] = encrypt_password(new_pw) 
                ln = ", ".join(p)
                done = True
            new.append(ln)
        um._write(new)
        print(color_text("🔑 Password updated Successfully." if done else "⚠️ User not found.", Color.GREEN if done else Color.RED))
