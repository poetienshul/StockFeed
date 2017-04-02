import requests
import time
import datetime
import csv

url_primary = "https://api.stockvider.com/data/NASDAQ/ticker/indicator?start_date=2014-05-01&end_date=2017-03-31&api-key=0483f9db4ec53f3228c0"

def main():				#currently writes CSV with date, close, volume, and movement as -1, 0, or 1
    tick = "AAPL"
    EODdict = EOD(tick)
    f.write("date,close,volume,move\n")
    prev = 0
    movement=0
    for key in EODdict:
        volume = EODdict[key]['VOLUME']
        close = EODdict[key]['CLOSE']
        if prev != 0:
            diff = close - prev
            diff = diff/close
            if diff < 0.02 and diff > -0.02:
                movement = 0
            elif close > prev:
                movement = 1
            else:
                movement = -1
        prev = close
        f.write(key + "," + str(close) +","+str(volume)+","+str(movement)+"\n")


#old methods to fetch technical indicators
def EMA(ticker):
    url = url_primary
    url = url.replace("ticker", ticker)
    url = url.replace("indicator", "EMA")

    url += "&time_period=14"

    response = requests.get(url)
    data = response.json()
    print(data)
    return data['Dataset']

def EOD(ticker):
	url = url_primary
	url = url.replace("ticker", ticker)
	url = url.replace("indicator", "EOD")

	response = requests.get(url)
	data = response.json()
	print(data)
	return data['Dataset']

def MACD(ticker): #signal period = 9, slow = 26, fast = 12
	url = url_primary
	url = url.replace("ticker", ticker)
	url = url.replace("indicator", "MACD")

	response = requests.get(url)
	data = response.json()
	print(data)
	return data['Dataset']

def RSI(ticker): #over 14 days
	url = url_primary
	url = url.replace("ticker", ticker)
	url = url.replace("indicator", "RSI")

	response = requests.get(url)
	data = response.json()
	print(data)

	return data['Dataset']

def MFI(ticker): #over 14 days
	url = url_primary
	url = url.replace("ticker", ticker)
	url = url.replace("indicator", "MFI")

	response = requests.get(url)
	data = response.json()
	print(data)

	return data['Dataset']

def STOCH(ticker): #slow stoch
	url = url_primary
	url = url.replace("ticker", ticker)
	url = url.replace("indicator", "STOCH")

	response = requests.get(url)
	data = response.json()
	print(data)
	return data['Dataset']

def BBAND(ticker):
	url = url_primary
	url = url_primary
	url = url.replace("ticker", ticker)
	url = url.replace("indicator", "BBANDS")

	response = requests.get(url)
	data = response.json()
	print(data)
	return data['Dataset']

def PPO(ticker):
	url = url_primary
	url = url_primary
	url = url.replace("ticker", ticker)
	url = url.replace("indicator", "PPO")
	print(url)
	response = requests.get(url)
	data = response.json()
	print(data)
	return data['Dataset']


main()
