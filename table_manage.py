from models import Table
from tabulate import tabulate
from colors import Color, color_text

Table_File = "Restaurant1_mini_Project/Data/tables.txt"

class TableManage:
    def __init__(self, user):
        self.user = user

    def _read(self):
        try:
            with open(Table_File, "r") as f:
                return [l.strip() for l in f]
        except FileNotFoundError:
            return []

    def _write(self, lines):
        with open(Table_File, "w") as f:
            for l in lines:
                f.write(l + "\n")

    def book_table(self):
        tid = input("🪑 Table id: ")
        new = []
        ok = False
        for ln in self._read():
            p = ln.split(", ")
            if p[0] == tid and p[2] == "free":
                p[2], p[3] = "booked", self.user
                ok = True
            new.append(", ".join(p))
        self._write(new)
        print(color_text("🎉 Booked." if ok else "❌ Unavailable or wrong id.", Color.GREEN if ok else Color.RED))

    def cancel_table(self):
        tid = input("❌ Table id: ")
        new = []
        ok = False
        for ln in self._read():
            p = ln.split(", ")
            if p[0] == tid and p[2] == "booked" and p[3] == self.user:
                p[2], p[3] = "free", "-"
                ok = True
            new.append(", ".join(p))
        self._write(new)
        print(color_text("🗑️ Cancelled." if ok else "⚠️ Not your booking or bad id.", Color.YELLOW if ok else Color.RED))

    def show_all_tables(self):
        lines = self._read()
        if not lines:
            print(color_text("📭 No tables found.", Color.RED))
            return
        data = [ln.split(", ") for ln in lines]
        print(color_text("🪑 Table List:", Color.CYAN))
        print(tabulate(data, headers=["Table ID", "Seats", "Status", "Booked By"], tablefmt="grid"))

