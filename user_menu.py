from menu_manage import MenuManage
from table_manage import TableManage
from order_manage import OrderManage
from colors import Color, color_text

class UserMenu:
    def __init__(self, uname):
        self.tm = TableManage(uname)
        self.om = OrderManage()
        self.mm = MenuManage()
        self.uname = uname
        self.menu()

    def menu(self):
        while True:
            print(color_text("""
======= 👤 User Menu =======
1️⃣ View Menu
2️⃣ Book Table
3️⃣ Cancel Table
4️⃣ New Order
5️⃣ Exit
===========================
""", Color.HEADER))
            ch = input("👉 Choice: ")
            if ch == "1":
                self.mm.show_all()
            elif ch == "2":
                self.tm.book_table()
            elif ch == "3":
                self.tm.cancel_table()
            elif ch == "4":
                self.om.new_order()
            elif ch == "5":
                print(color_text("🙏 Enjoy your meal!", Color.YELLOW))
                break
            else:
                print(color_text("⚠️ Invalid choice.", Color.RED))

