def convert_currency(amount, from_currency, to_currency):
    # Define exchange rates relative to USD (as of a certain date)
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.89,
        'GBP': 0.75,
        'JPY': 109.35,
        'INR': 75.0,  # Exchange rate of 1 USD to 75 INR (for example)
        # Add more currencies and their respective exchange rates here
    }

    if from_currency == 'USD':
        amount_usd = amount
    else:
        # Convert from 'from_currency' to USD
        amount_usd = amount / exchange_rates[from_currency]

    if to_currency == 'USD':
        converted_amount = amount_usd
    else:
        # Convert from USD to 'to_currency'
        converted_amount = amount_usd * exchange_rates[to_currency]

    return converted_amount

def main():
    print("Welcome to Currency Converter")
    print("Supported currencies: USD, EUR, GBP, JPY, INR, and more...")

    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency you have (e.g., USD, EUR, GBP): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., USD, EUR, GBP): ").upper()

    result = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {result} {to_currency}")

if __name__ == "__main__":
    main()
