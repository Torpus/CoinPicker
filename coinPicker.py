#!/usr/bin/env python
import argparse,requests,os,platform,sys,psutil
from termcolor import colored
from subprocess import Popen

def determineOS():
	osType = platform.platform()
	os = ''
	if 'Windows' in osType:
		os = 'windows'
	elif 'Darwin' in osType:
		print('don\'t mine with mac')
		exit(1)
	else:
		os = 'linux'
	return os

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
	return coinToMine

def invokeMiner(os, newCoin, oldcoin):
	try:
		if os == 'windows':
			#invoke batch file
			
		else if os == 'linux':
			pid = Popen.
    except:
		#remove exe from rotation, bypass sleep, and send email notification
		print(colored(exe + ' failed to start.  ' + exe + ' removed from rotation and an email has been sent.')

if __name__ == '__main__':
	os = determineOS()
	args = parser()
	#convert first arg character to uppercase
	coin = upperFirst(args.coin)
	coinFile = args.file
	checkFileExists(coinFile)
	while(true):
		newCoin = pickCoin(coin,coinFile)
		if oldCoin:
			if newCoin != oldCoin:
				killMiner(oldCoin)
				invokeMiner(os, newCoin)
		else:
			invokeMiner(os, newCoin)
		sleep(300)
