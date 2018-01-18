#!/usr/bin/env python
import argparse,requests,os.path,platform
from termcolor import colored
from subprocess import call

def determineOS():
    osType = platform.platform()
    if 'Windows' in osType:
        print('windows')
    elif 'Darwin' in osType:
        print('mac')
    else:
        print('linux')

def parser():
    parser = argparse.ArgumentParser(description='coinPicker')
    parser.add_argument('-c','--coin', help='Which Coin to Mine', required=True)
    parser.add_argument('-f','--file', help='List of approved coins', required=True)
    return parser.parse_args()

def checkFileExists(file):
     if not os.path.exists(file):
         print(colored('Path to file is invalid.', 'red'))
         exit(1)

def fetchCoinJson(coinToMine,approvedCoinFile):
    try:
        r = requests.get('http://whattomine.com/coins.json')
    except:
        print(colored('Unable to connect to whattomine.com', 'red'))
        exit(1)
    rJson = r.json()['coins']
    coinList = open(approvedCoinFile, 'r')
    for coin in coinList:
        coin = coin.strip()
        print(coin + ' = ' + str(rJson[coin]['profitability']) + ' :: ' + coinToMine + ' = ' + str(rJson[coinToMine]['profitability']))
        if rJson[coin]['profitability'] > rJson[coinToMine]['profitability']:
            coinToMine = coin
            exe = './' + coinToMine + '.sh'
            print(exe)

if __name__ == '__main__':
    args = parser()
    #convert first arg character to uppercase
    coin = args.coin.title()
    coinFile = args.file
    checkFileExists(coinFile)
    fetchCoinJson(coin,coinFile)
