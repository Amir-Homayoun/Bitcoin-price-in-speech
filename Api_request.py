from pprint import pprint
def API():
    import requests

    url = f"https://api.coindesk.com/v1/bpi/currentprice.json"

    response = requests.get(url)
    data = response.json()

    return data
