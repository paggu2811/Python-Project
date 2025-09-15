from models import Order
from tabulate import tabulate
from colors import Color, color_text

Menu_File = "Restaurant1_mini_Project/Data/menu.txt"
Order_File = "Restaurant1_mini_Project/Data/orders.txt"

class OrderManage:
    def _read(self, path):
        try:
            with open(path, "r") as f:
                return [l.strip() for l in f]
        except FileNotFoundError:
            return []

    def _write(self, path, lines):
        with open(path, "w") as f:
            for l in lines:
                f.write(l + "\n")

    def new_order(self):
        oid = int(input("🆕 New order id: "))
        tid = input("🪑 Table id: ")
        dish_ids = input("🍽️ Enter dish ids (space): ").split()
        total = 0
        menu = self._read(Menu_File)
        for did in dish_ids:
            for ln in menu:
                p = ln.split(", ")
                if p[0] == did:
                    total += float(p[3])
                    break
        orders = self._read(Order_File)
        orders.append(str(Order(oid, tid, dish_ids, total)))
        self._write(Order_File, orders)
        print(color_text(f"✅ Order taken. Total ₹{total}", Color.GREEN))

    def cancel_order(self):
        oid = input("❌ Order id to cancel: ")
        orders = self._read(Order_File)
        new = [ln for ln in orders if not ln.startswith(f"{oid},")]
        self._write(Order_File, new)
        print(color_text("🗑️ Cancelled." if len(new) < len(orders) else "❌ ID not found.", Color.YELLOW if len(new) < len(orders) else Color.RED))

    def show_all_orders(self):
        lines = self._read(Order_File)
        if not lines:
            print(color_text("📭 No orders found.", Color.RED))
            return
        data = [ln.split(", ") for ln in lines]
        for row in data:
            row[2] = row[2].replace("|", ", ")
        print(color_text("📦 Orders List:", Color.CYAN))
        print(tabulate(data, headers=["Order ID", "Table ID", "Dish IDs", "Total", "Status"], tablefmt="grid"))


