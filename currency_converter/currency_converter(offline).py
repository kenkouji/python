exchange_rates={
    "USD": {"EUR": 0.92, "CAD": 1.34, "INR": 82.50},
    "EUR": {"USD": 1.09, "CAD": 1.46, "INR": 89.50},
    "CAD": {"USD": 0.75, "EUR": 0.68, "INR": 60.90},
    "INR": {"USD": 0.012, "EUR": 0.011, "CAD": 0.016}
}
def currency_conversion(source_currency,target_currency,amount):
 source_currency,target_currency=source_currency.upper(),target_currency.upper()
 if source_currency in exchange_rates and target_currency in exchange_rates[source_currency]:
  converted_amount=amount*exchange_rates[source_currency] [target_currency]
  print(f"{amount}{source_currency} ={converted_amount:.2f}{target_currency}")
 else:
  print("invalid sum entered")
try:
   amount=float(input("enter the amount: "))
   source_currency=input("source currency[USD/EUR/CAD/INR]; ")
   target_currency=input("Target currency[USD/EUR/CAD/INR]: ")
   currency_conversion(source_currency, target_currency, amount)

except ValueError:
   print("invalid input!enter a proper number")
   

