#!/usr/bin/env python
import argparse,requests,os,platform,sys,psutil
from termcolor import colored
from subprocess import Popen

def determineOS():
    osType = platform.platform()
    if 'Windows' in osType:
        print('windows')
    elif 'Darwin' in osType:
        print('mac')
    else:
        print('linux')

def upperFirst(x):
    return x[0].upper() + x[1:]

def parser():
    parser = argparse.ArgumentParser(description='coinPicker')
    parser.add_argument('-c','--coin', help='Which Coin to Mine', required=True)
    parser.add_argument('-f','--file', help='List of approved coins', required=True)
    return parser.parse_args()

def checkFileExists(file):
     if not os.path.exists(file):
         print(colored('Path to file is invalid.', 'red'))
         exit(1)

def pickCoin(coinToMine,approvedCoinFile):
    try:
        r = requests.get('http://whattomine.com/coins.json')
    except:
        print(colored('Unable to connect to whattomine.com', 'red'))
        exit(1)
    rJson = r.json()['coins']
    coinList = open(approvedCoinFile, 'r')
    for coin in coinList:
        coin = coin.strip()
        if coin != coinToMine:
            print(coin + ' = ' + str(rJson[coin]['profitability']) + ' :: ' + coinToMine + ' = ' + str(rJson[coinToMine]['profitability']))
            if rJson[coin]['profitability'] > rJson[coinToMine]['profitability']:
                coinToMine = coin
    exe = './' + coinToMine + '.bat'
    return exe

def invokeMiner(exe):
    try:
        #check previous instance if there is one
        #kill old instance if not same else done
    except:
        #remove exe from rotation and send email
        print(colored(exe + ' failed to start.  ' + exe + ' removed from rotation and an email has been sent.')

if __name__ == '__main__':
    while(true):
        args = parser()
        #convert first arg character to uppercase
        coin = upperFirst(args.coin)
        coinFile = args.file
        checkFileExists(coinFile)
        pickCoin(coin,coinFile)
        sleep(300)
