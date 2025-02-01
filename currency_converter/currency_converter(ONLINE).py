from forex_python.converter import CurrencyRates

def currency_conversion(source_currency, target_currency, amount):
    c = CurrencyRates()
    source_currency = source_currency.upper()
    target_currency = target_currency.upper()

    try:
        exchange_rate = c.get_rate(source_currency, target_currency)
        converted_amount = amount * exchange_rate
        print(f"{amount} {source_currency} = {converted_amount:.2f} {target_currency}")
    except Exception as e:
        print("Error: Invalid currency code or network issue")
        print(f"Details: {e}")  # This helps debug errors

# Get user input
try:
    amount = float(input("Enter the amount: "))
    source_currency = input("Source currency (e.g., USD, EUR, CAD): ")
    target_currency = input("Target currency (e.g., USD, EUR, CAD): ")

    currency_conversion(source_currency, target_currency, amount)

except ValueError:
    print("Invalid input! Please enter a numeric amount.")
