exchange_rates = {
    "USD": {"EUR": 0.92, "CAD": 1.34, "INR": 82.50},
    "EUR": {"USD": 1.09, "CAD": 1.46, "INR": 89.50},
    "CAD": {"USD": 0.75, "EUR": 0.68, "INR": 60.90},
    "INR": {"USD": 0.012, "EUR": 0.011, "CAD": 0.016}
}

def currency_exchange():
    while True:
        try:
            amount = float(input("Enter the amount you want to convert: "))
            source_currency = input("The amount is in which currency? (USD/EUR/CAD/INR): ").upper()
            target_currency = input("The amount you want to convert to which currency? (USD/EUR/CAD/INR): ").upper()

            if source_currency in exchange_rates and target_currency in exchange_rates[source_currency]:
                converted_amount = amount * exchange_rates[source_currency][target_currency]
                print(f"\n💰 {amount} {source_currency} is equal to {converted_amount:.2f} {target_currency} 💰\n")
             
                again = input("Do you want to convert another amount? (y/n): ").lower()
                if again != 'y':
                    print("Thank you for using the currency converter! 😊")
                    break  
            else:
                print("\n⚠️ Invalid currency choice. Please enter a valid currency code (USD, EUR, CAD, INR).\n")
        
        except ValueError:
            print("\n❌ Invalid amount entered! Please enter a valid number.\n")


currency_exchange()
