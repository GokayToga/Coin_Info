from colorsys import rgb_to_yiq
from requests import get
from pprint import PrettyPrinter

URL = "https://api.wazirx.com/sapi/v1/tickers/24hr"

data = get(URL).json()

printer = PrettyPrinter()


def get_name():
    names = []
    for i in range(0,500):
        try:
            names.append(data[i]['baseAsset'])
        except:
            print("-----------------------------")
            break                  
    return names

def get_value():
    values = []
    for i in range(0,500):
        try:
            values.append(data[i]['lastPrice'])
        except:
            print("-----------------------------")
            break                  
    return values


def make_list():
    names = get_name()
    values = get_value()
    lists = []
    for i in range(0,500):
        try:
            lists.append(f" Coin name: {names[i]} Coin value: {values[i]}")
        except:
            print("-----------------------------")
            break 


names = get_name()
print(names[2])
