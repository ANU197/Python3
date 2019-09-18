# a = 'anurag'
# b = 'porwal'
# print(a+" "+b)

import requests
from bs4 import BeautifulSoup
URL1 = 'https://www.x-rates.com/table/?from=INR&amount=1'
headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
r = requests.get(URL1, headers=headers)

soup = BeautifulSoup(r.content, "lxml")


ls = soup.findAll("table", {"class": "ratesTable"})
currency1 = []
cur = []
currencyDict = {}
for row in ls:
        currency = row.get_text()
        currency1 = currency.replace("\t", "").strip().split("\n")
        print(currency1)
        # cur = currency1[4]
        # name = currency1[1]
        # key = name+"-"+cur[2:5]
        # val = float(cur[8:15])
        # currencyDict[key] = val

    # INR = float(input("Enter Amount(INR):"))
    # print('\n')
    # print('Enter the name of the currency you want to convert amount to? Available options:\n')
    # for item in currencyDict.keys():
    #     print(item)
    #
    # print('\n')
    # currency = input('Please enter one of them: ')
    # print(f"{INR} INR is equal to {INR*currencyDict[currency]} {currency}")
