import csv
import sys
import datetime

history = {}
date = datetime.datetime.now()
output = {}
close = {}
emas = {}
n = 90
numdays = 1
while (n > 0):
    data = []
    dateS = date.strftime("%Y%m%d")
    try:
        f = dateS[0:4] + "\\" + dateS + "\prices.csv"
        with open(f, newline = '') as file:
            filereader = csv.reader(file)
            for row in filereader:
                data.append(row)
                output[row[0]] = []
                close[row[0]] = []
                emas[row[0]] = []
        history[numdays] = data
        numdays += 1
    except:
        date = date + datetime.timedelta(days = -1)
        continue
    date = date + datetime.timedelta(days = -1)
    n -= 1


def closes(n):
    for k in close:
        close[k].append(0)
    for x in range(1, n + 1):
        for y in range(1, len(history[x]) - 1, 2):
            close[history[x][y][0]].append(history[x][y][5])
    return close


close = closes(80)

#TODO: calculate bollinger bands

#TODO: calculate moving averages
def sma(s, n):
    for k in output:
        output[k].append(0)
        index = len(output[k])
        output[k].append(0)
    for x in range(s, s + n + 1):
        for y in range(1, len(history[x]) - 1, 2):
            val = output[history[x][y][0]][index]
            output[history[x][y][0]][index] = output[history[x][y][0]][index] + float(history[x][y][5])
            if (output[history[x][y][0]][index] > val):
                output[history[x][y][0]][index - 1] += 1
            #if (abs(float(history[x][y + 1][7]) - float(history[x][y + 1][5])) > float(history[x][y + 1][5]) * 0.1):
             #   print ("Probable Split: " + history[x][y][0] + " Day: " + str(x))
    for k in output:
        if (output[k][index - 1] != 0):
            output[k][index] = output[k][index] / output[k][index - 1]

    return output


def ema(s, n, emas):
    mult = 2 / float(n + 1)
    for k in emas:
        sum = 0.0
        if (len(close[k]) >= s + n + 10):
            for x in range(s+n, s+n+10):
                if (len(close[k]) > 1):
                    sum += float(close[k][x])
            sma = float(sum) / (10)
            emas[k].append(sma)
            for x in range(1, n+1):
                emas[k].append((float(close[k][s + x]) - emas[k][x - 1]) * mult + emas[k][x - 1])


#TODO: calculate relative strength index

#TODO: calculate MACD

#TODO: print to csv

output = sma(1, 20)
ema(1, 50, emas)