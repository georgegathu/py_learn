/*
A simple currency converter app.
Requirements:
- pip install requests
*/

import requests

def get_exchange_rate(base_currency, target_currency):
    """
    Fetch exchange rate from an API.
    Replace 'YOUR_API_KEY' with a valid key from an exchange rate provider.
    """
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url)
        data = response.json()

        if "rates" in data and target_currency in data["rates"]:
            return data["rates"][target_currency]
        else:
            print(f"Unable to find exchange rate for {target_currency}.")
            return None
    except Exception as e:
        print("Error fetching exchange rate:", e)
        return None

def currency_converter():
    print("Welcome to the Currency Converter App!")
    base_currency = input("Enter the base currency (e.g., USD, EUR): ").upper()
    target_currency = input("Enter the target currency (e.g., INR, GBP): ").upper()
    amount = float(input(f"Enter the amount in {base_currency}: "))

    # Fetch the exchange rate
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    
    if exchange_rate:
        converted_amount = amount * exchange_rate
        print(f"\n{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        print("Conversion failed. Please check your input and try again.")

if __name__ == "__main__":
    currency_converter()
