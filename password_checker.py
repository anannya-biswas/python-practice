password = input("Enter a password: ")

if len(password) < 6:
    print("Too short!")
elif not any(char.isdigit() for char in password):
    print("Add at least one number!")
elif not any(char.isupper() for char in password):
    print("Add at least one uppercase letter!")
else:
    print("Password looks good ✅")
