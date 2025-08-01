import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    
    if target_currency not in data['rates']:
        print("Currency not found.")
        return None
    
    return data['rates'][target_currency]

def convert_currency():
    base = input("From (currency code): ").upper()
    target = input("To (currency code): ").upper()
    amount = float(input("Amount: "))
    
    rate = get_exchange_rate(base, target)
    if rate:
        converted = amount * rate
        print(f"{amount} {base} = {converted:.2f} {target}")

convert_currency()
