from models import Dish
from tabulate import tabulate

Menu_File = "Restaurant1_mini_Project/Data/menu.txt"

class MenuManage:
    def _read(self):
        try:
            with open(Menu_File, "r") as f:
                return [l.strip() for l in f]
        except FileNotFoundError:
            return []

    def _write(self, lines):
        with open(Menu_File, "w") as f:
            for l in lines:
                f.write(l + "\n")

    def add_dish(self):
        did = int(input("Dish id : "))
        name = input("Name : ")
        cat = input("Category : ")
        price = float(input("Price : "))
        lines = self._read()
        lines.append(str(Dish(did, name, cat, price)))
        self._write(lines)
        print("Dish added.")

    def upd_dish(self):
        did = input("Dish id to update : ")
        lines = self._read()
        new = []
        found = False
        for ln in lines:
            parts = ln.split(", ")
            if parts[0] == did:
                found = True
                if input("Do  You want to update name? (y/n): ").lower().startswith("y"):
                    parts[1] = input("New name : ")
                if input("Do you want to update category? (y/n): ").lower().startswith("y"):
                    parts[2] = input("New category : ")
                if input("Do you want to Update price? (y/n): ").lower().startswith("y"):
                    parts[3] = str(float(input("New price : ")))
                ln = ", ".join(parts)
            new.append(ln)
        self._write(new)
        print("Updated." if found else "ID not found.")    

    def del_dish(self):
        did = input("Dish id to delete : ")
        lines = self._read()
        new = [ln for ln in lines if not ln.startswith(f"{did},")]
        self._write(new)
        print("Deleted." if len(new) < len(lines) else "ID not found.") 
         
    def show_all(self):
        lines = self._read()
        if not lines:
            print("Menu is empty.")
            return
    
        data = [line.split(", ") for line in lines]
        print(tabulate(data, headers=["ID", "Name", "Category", "Price"], tablefmt="grid"))

    def search(self):
        key = input("Search keyword : ").lower()
        data = []
        for ln in self._read():
            if key in ln.lower():
                data.append(ln.split(", "))
        if data:
            print(tabulate(data, headers=["ID", "Name", "Category", "Price"], tablefmt="grid"))
        else:
            print("No match found.")
