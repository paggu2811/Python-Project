class Dish:
    def __init__(self, did, name, category, price):
        self.did = did
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"{self.did}, {self.name}, {self.category}, {self.price}"

class Table:
    def __init__(self, tid, seats, status="free", booked_by="-"):
        self.tid = tid
        self.seats = seats
        self.status = status
        self.booked_by = booked_by

    def __str__(self):
        return f"{self.tid}, {self.seats}, {self.status}, {self.booked_by}"

class Order:
    def __init__(self, oid, tid, items, total, status="open"):
        item_str = "|".join(map(str, items))
        self.oid = oid
        self.tid = tid
        self.items = item_str
        self.total = total
        self.status = status

    def __str__(self):
        return f"{self.oid}, {self.tid}, {self.items}, {self.total}, {self.status}"

class User:
    def __init__(self, uid, uname, passwd, role="user"):
        self.uid = uid
        self.uname = uname
        self.passwd = passwd
        self.role = role

    def __str__(self):
        return f"{self.uid}, {self.uname}, {self.passwd}, {self.role}"
