def temp_converter():
    c = float(input("Enter temp in Celsius: "))
    f = (c * 9/5) + 32
    print(f"{c}°C = {f}°F")

def length_converter():
    m = float(input("Enter length in meters: "))
    feet = m * 3.28084
    print(f"{m} meters = {feet:.2f} feet")

def weight_converter():
    kg = float(input("Enter weight in kg: "))
    lb = kg * 2.20462
    print(f"{kg} kg = {lb:.2f} lbs")

while True:
    print("\n1. Temp\n2. Length\n3. Weight\n4. Exit")
    choice = input("Choose: ")
    if choice == '1':
        temp_converter()
    elif choice == '2':
        length_converter()
    elif choice == '3':
        weight_converter()
    else:
        break
