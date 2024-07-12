from Api_request import API
def MAIN():
    data=API()

    def price_founder(currency):
        return data['bpi'][currency.upper()]['rate']

    return f"""Bitcoin in Dollar is: {price_founder('usd')}
Bitcoin in Euro is: {price_founder('eur')}
Bitcoin in Pond is: {price_founder('GBP')}"""