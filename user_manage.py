from models import User
from tabulate import tabulate
from colors import Color, color_text

USER_FILE = "Restaurant1_mini_Project/Data/users.txt"

class UserManage:
    def _read(self):
        try:
            with open(USER_FILE, "r") as f:
                return [l.strip() for l in f]
        except FileNotFoundError:
            return []

    def _write(self, lines):
        with open(USER_FILE, "w") as f:
            for l in lines:
                f.write(l + "\n")

    def add_user(self):
        uid = int(input("🆔 User id: "))
        uname = input("👤 Username: ")
        pw = input("🔑 Password: ")
        role = input("🎭 Role (user/manager): ")
        lines = self._read()
        lines.append(str(User(uid, uname, pw, role)))
        self._write(lines)
        print(color_text("✅ User added.", Color.GREEN))

    def upd_user(self):
        uid = input("✏️ User id to update: ")
        lines = self._read()
        new = []
        found = False
        for ln in lines:
            p = ln.split(", ")
            if p[0] == uid:
                found = True
                if input("Change name? (y/n): ").lower().startswith("y"):
                    p[1] = input("🆕 New name: ")
                if input("Change pass? (y/n): ").lower().startswith("y"):
                    p[2] = input("🆕 New pass: ")
                ln = ", ".join(p)
            new.append(ln)
        self._write(new)
        print(color_text("✅ Updated." if found else "❌ Not found.", Color.GREEN if found else Color.RED))

    def del_user(self):
        uid = input("🗑️ Id to delete: ")
        lines = self._read()
        new = [ln for ln in lines if not ln.startswith(f"{uid},")]
        self._write(new)
        print(color_text("🗑️ Deleted." if len(new) < len(lines) else "❌ Not found.", Color.YELLOW if len(new) < len(lines) else Color.RED))

    def show_all(self):
        lines = self._read()
        if not lines:
            print(color_text("📭 No users found.", Color.RED))
            return
        data = [ln.split(", ") for ln in lines]
        print(color_text("👥 User List:", Color.CYAN))
        print(tabulate(data, headers=["ID", "Username", "Password", "Role"], tablefmt="grid"))

