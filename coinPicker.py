#!/usr/bin/env python
import argparse,requests,os,platform,sys
from termcolor import colored
from subprocess import Popen
from psutil import Process

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
    print(exe)
    with open("prevCoin", "w+") as prevCoinFile:
        prevCoin = prevCoinFile.readline()
        prevCoin = prevCoin.strip()
        if prevCoin:
            if prevCoin != coinToMine:
                prevPid = prevCoinFile.readline().strip()
                print(prevPid)
                p = Process(prevPid)
                print("Killing pid: " + prevPid)
                Popen.kill(p)
        prevCoinFile.close()
        myProc = Popen([exe], shell=True)
        pid = myProc.pid
        prevCoinFile = open("prevCoin", "w")
        prevCoinFile.write(coinToMine + "\n" + str(pid))
        prevCoinFile.close()

if __name__ == '__main__':
    args = parser()
    #convert first arg character to uppercase
    coin = upperFirst(args.coin)
    coinFile = args.file
    checkFileExists(coinFile)
    pickCoin(coin,coinFile)
