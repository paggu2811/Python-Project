import hashlib

def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_user_entry(uid, username, password, role):
    encrypted_pw = encrypt_password(password)
    return f"{uid}, {username}, {encrypted_pw}, {role}"


users = [
    ("U1", "admin", "admin123", "manager"),
    ("U2", "Pragati", "Pragati@123", "user"),
    ("U3", "sam", "sam@123", "user"),
    
    ]



for uid, uname, passwd, role in users:
    line = create_user_entry(uid, uname, passwd, role)
    print(line)
