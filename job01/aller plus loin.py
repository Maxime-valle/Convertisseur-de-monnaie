from forex_python.converter import CurrencyRates

class CustomCurrencyConverter:
    def __init__(self):
        self.cr = CurrencyRates()
        self.custom_rates = {}

    def add_rate(self, from_currency, to_currency, rate):
        self.custom_rates[(from_currency, to_currency)] = rate

    def convert(self, amount, from_currency, to_currency):
        if (from_currency, to_currency) in self.custom_rates:
            return amount * self.custom_rates[(from_currency, to_currency)]
        else:
            try:
                return self.cr.convert(from_currency, to_currency, amount)
            except Exception as e:
                print(f"La conversion de {from_currency} à {to_currency} n'est pas possible.")
                return None

# Exemple d'utilisation
ccc = CustomCurrencyConverter()
ccc.add_rate('USD', 'EUR', 0.85)
print(ccc.convert(100, 'USD', 'EUR'))