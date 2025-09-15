from manager import ManagerMenu
from user_menu import UserMenu
from user_manage import UserManage
from colors import Color, color_text
import hashlib

USER_FILE = "Restaurant1_mini_Project/Data/users.txt"


def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def read_users():
    try:
        with open(USER_FILE, "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []


def login():
    uname = input("👤 Username: ")
    passwd = input("🔑 Password: ")
    encrypted_input = encrypt_password(passwd)  

    for ln in read_users():
        uid, u, pw, role = ln.split(", ")
        if u == uname and pw == encrypted_input:
            return uname, role
    return None, None


def main():
    while True:
        print(color_text("""
********* 🍽️  Welcome To Restaurant System ********
1️⃣ Login
2️⃣ Exit
****************************************
""", Color.HEADER))
        ch = input("👉 Choice: ")
        if ch == "1":
            uname, role = login()
            if role == "manager":
                print(color_text(f"🎩 Welcome Manager {uname}", Color.CYAN))
                ManagerMenu(uname)
            elif role == "user":
                print(color_text(f"👋 Welcome {uname}", Color.CYAN))
                UserMenu(uname)
            else:
                print(color_text("❌ Invalid credentials.", Color.RED))
        elif ch == "2":
            print(color_text("👋 Goodbye!", Color.YELLOW))
            break
        else:
            print(color_text("⚠️ Invalid choice.", Color.RED))

if __name__ == "__main__":
    main()
