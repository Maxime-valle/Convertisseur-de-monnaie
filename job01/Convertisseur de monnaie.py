from forex_python.converter import CurrencyRates

def convert_and_save(to_currencies, filename):
    amount = float(input("Veuillez entrer le montant que vous souhaitez convertir : "))
    from_currency = input("Veuillez entrer la devise d'origine (par exemple 'EUR') : ")
    forex_phthon = CurrencyRates()
    for to_currency in to_currencies:
        try:
            result = forex_phthon.convert(from_currency, to_currency, amount)
            with open(filename, 'a') as f:
                f.write(f"{from_currency} to {to_currency}, {amount} : {result}\n")
            print(f"{amount} {from_currency} est égal à {result} {to_currency}")
        except Exception as e:
            print(f"La conversion de {from_currency} à {to_currency} n'est pas possible.")

convert_and_save(['USD', 'JPY', 'GBP', 'PLN', "THB", "NOK"], 'history.txt')

