exchange_rate={
  "USD": {"EUR": 0.92, "CAD": 1.34, "INR": 82.50},
    "EUR": {"USD": 1.09, "CAD": 1.46, "INR": 89.50},
    "CAD": {"USD": 0.75, "EUR": 0.68, "INR": 60.90},
    "INR": {"USD": 0.012, "EUR": 0.011, "CAD": 0.016}
}

def currency_exchange(source_currency,target_currency,amount):

 source_currency,target_currency=source_currency.upper(),target_currency.upper()
 if source_currency in exchange_rate and target_currency in exchange_rate[source_currency]:
    currency_exchange=amount*exchange_rate[source_currency][target_currency]
    print(f"{amount} {source_currency}is equal to {currency_exchange} {target_currency}") 
 else:
   print("invalid input try again later")
    
while True:
 try:
    amount=float(input("enter the amount:"))
    source_currency=input("Source Currency (USD/EUR/CAD/INR): ")
    target_currency=input("Target Currency (USD/EUR/CAD/INR): ")
    currency_exchange(source_currency,target_currency,amount)
    break
 except:
   print("invalid input,try it again")
