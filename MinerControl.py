import requests
from subprocess import call

r = requests.get('http://whattomine.com/coins.json')
rJson = r.json()['coins']
approvedCoinFile = open('approvedCoinFile', 'r')
coinToMine = "Ethereum"
for coin in approvedCoinFile:
    coin = coin.strip()
    print(coin + ' = ' + str(rJson[coin]['profitability']) + ' :: ' + coinToMine + ' = ' + str(rJson[coinToMine]['profitability']))
    if rJson[coin]['profitability'] > rJson[coinToMine]['profitability']:
        coinToMine = coin
exe = './' + coinToMine + '.sh'
print(exe)
