from forex_python.converter import CurrencyRates

def convert_and_save(amount, from_currency, to_currencies, filename):
    cr = CurrencyRates()
    for to_currency in to_currencies:
        try:
            result = cr.convert(from_currency, to_currency, amount)
            with open(filename, 'a') as f:
                f.write(f"{from_currency} to {to_currency}, {amount} : {result}\n")
            print(f"{amount} {from_currency} est égal à {result} {to_currency}")
        except Exception as e:
            print(f"La conversion de {from_currency} à {to_currency} n'est pas possible.")


convert_and_save(100, 'EUR', ['USD', 'JPY', 'GBP','PLN',"THB","NOK"], 'history.txt')

