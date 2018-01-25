#!/usr/bin/env python
import argparse,requests,os,platform,sys,psutil
from termcolor import colored
from subprocess import Popen
from time import sleep

def determineOS():
	osType = platform.platform()
	osName = ''
	if 'Windows' in osType:
		osName = 'windows'
	elif 'Darwin' in osType:
		print('don\'t mine with mac')
		osName = 'linux'
	else:
		osName = 'linux'
	return osName

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

def invokeMiner(osName, coin):
	exe = ''
	pid = ''
	try:
		if os == 'windows':
			#invoke batch file
			exe = coin + ".bat"
		elif os == 'linux':
			exe = './' + coin + '.sh'
			pid = Popen(exe).pid
	except:
		#remove exe from rotation, bypass sleep, and send email notification
		print(colored(exe + ' failed to start.  ' + exe + ' removed from rotation and an email has been sent.'))
	return pid

if __name__ == '__main__':
	osName = determineOS()
	args = parser()
	#convert first arg character to uppercase
	coin = upperFirst(args.coin)
	coinFile = args.file
	checkFileExists(coinFile)
	pid = ''
	oldCoin = ''
	while(True):
		newCoin = pickCoin(coin,coinFile)
		if pid:
			if newCoin != oldCoin:
			#	killMiner(pid)
				print(newCoin + " mining started under pid: " + pid)
			#	pid = invokeMiner(os, newCoin)
		else:
			#pid = invokeMiner(osName, newCoin)
			print(newCoin + " mining started under pid: " + pid)
		sleep(15)
