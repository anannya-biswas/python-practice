from cryptography.fernet import Fernet
import os

# Generate and save key only once
if not os.path.exists("key.key"):
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

with open("key.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

def add_password():
    account = input("Account: ")
    pwd = input("Password: ")
    enc_pwd = cipher.encrypt(pwd.encode())
    with open("passwords.txt", "a") as file:
        file.write(f"{account}:{enc_pwd.decode()}\n")
    print("Password stored.")

def view_passwords():
    try:
        with open("passwords.txt", "r") as file:
            for line in file.readlines():
                account, enc_pwd = line.strip().split(":")
                dec_pwd = cipher.decrypt(enc_pwd.encode()).decode()
                print(f"{account} → {dec_pwd}")
    except FileNotFoundError:
        print("No passwords saved yet.")

while True:
    print("\n1. Add Password\n2. View Passwords\n3. Exit")
    choice = input("Choose: ")
    if choice == '1':
        add_password()
    elif choice == '2':
        view_passwords()
    elif choice == '3':
        break
