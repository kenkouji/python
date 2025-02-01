exchange_rates = {
    "USD": {"EUR": 0.92, "CAD": 1.34, "INR": 82.50},
    "EUR": {"USD": 1.09, "CAD": 1.46, "INR": 89.50},
    "CAD": {"USD": 0.75, "EUR": 0.68, "INR": 60.90},
    "INR": {"USD": 0.012, "EUR": 0.011, "CAD": 0.016}
}

def currency_exchange():
    while True:
        try:
            amount = float(input("\nEnter the amount: "))
            source_currency = input("Source Currency (USD/EUR/CAD/INR): ").strip().upper()
            target_currency = input("Target Currency (USD/EUR/CAD/INR): ").strip().upper()

            # Check if currencies exist
            if source_currency in exchange_rates and target_currency in exchange_rates[source_currency]:
                converted_amount = amount * exchange_rates[source_currency][target_currency]
                print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")
                break  # Exit loop if conversion is successful
            else:
                print("Invalid currency code! Please try again.")

        except ValueError:
            print("Invalid amount! Please enter a numeric value.")

while True:  # Main loop to keep running
    currency_exchange()

    again = input("\nDo you want to convert another currency? (y/n): ").strip().lower()
    if again != "y":
        print("Thank you for using the currency converter!")
        break  # Exit the program
