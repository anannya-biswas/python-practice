def convert_length(value, unit):
    conversions = {
        "m": value,
        "cm": value * 100,
        "mm": value * 1000,
        "in": value * 39.3701,
        "ft": value * 3.28084
    }
    return conversions

val = float(input("Enter value in meters: "))
units = convert_length(val, "m")
for k, v in units.items():
    print(f"{v:.2f} {k}")
