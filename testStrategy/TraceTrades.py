#!/usr/bin/env python3
from sys import argv
import numpy as np
# Vars
price = []
rsi = []
tsi = []
macd = []
bb = []
volume = []
smiio = []
roc = []
logs = []
srsi1 = []
srsi2 = []
testValues = [44, 56, -0.8, 0.4, -1, 7, 9, 8, 2, 1,
              0.5, 0.3, 1, 8, 9, 3, 3, 4, 2, 2, 3.5, 4.0, 0, 0]
# load datasets from files


def load(filename, indicator):
    f = open("../datasets/"+filename, "r")
    for l in f:
        cPlace = l[:-1]
        indicator.append(cPlace)
    f.close()


def Average(lst):
    return sum(lst) / len(lst)


if argv[1] == "dataset":
    # open file and read the content in a list
    load("datasetPrice.txt", price)
    load("datasetRSIval.txt", rsi)
    load("datasetTSI.txt", tsi)
    load("datasetMACD.txt", macd)
    load("datasetBB.txt", bb)
    load("datasetVolume.txt", volume)
    load("datasetSMIIO.txt", smiio)
    load("datasetROC.txt", roc)
    load("datasetSRSI.txt", srsi1)
    load("datasetSRSI2.txt", srsi2)
elif argv[1] == "log":
    load("../log.txt", logs)
    for log in logs:
        logchar = 0
        logchar2 = 0
        # Price
        while log[logchar] != ' ':
            logchar += 1
        price.append(int(log[:logchar])/10)
        # RSI
        logchar2 = logchar + 1
        logchar += 1
        while log[logchar2] != ' ':
            logchar2 += 1
        rsi.append(log[logchar:logchar2])
        # TSI
        logchar = logchar2 + 1
        logchar2 += 1
        while log[logchar] != ' ':
            logchar += 1
        tsi.append(log[logchar2:logchar])
        # MACD
        logchar2 = logchar + 1
        logchar += 1
        while log[logchar2] != ' ':
            logchar2 += 1
        macd.append(log[logchar:logchar2])
        # BB
        logchar = logchar2 + 1
        logchar2 += 1
        while log[logchar] != ' ':
            logchar += 1
        bb.append(log[logchar2:logchar])
        # Volume
        logchar2 = logchar + 1
        logchar += 1
        while log[logchar2] != ' ':
            logchar2 += 1
        volume.append(log[logchar:logchar2])
        # SMIIO
        logchar = logchar2 + 1
        logchar2 += 1
        while log[logchar] != ' ':
            logchar += 1
        smiio.append(log[logchar2:logchar])
        # ROC
        logchar2 = logchar + 1
        logchar += 1
        while log[logchar2] != ' ':
            logchar2 += 1
        roc.append(log[logchar:logchar2])
        # SRSI
        logchar = logchar2 + 1
        logchar2 += 1
        while log[logchar] != ' ':
            logchar += 1
        srsi1.append(log[logchar2:logchar])
        # SRSI
        logchar2 = logchar + 1
        logchar += 1
        while log[logchar2] != ' ':
            logchar2 += 1
        srsi2.append(log[logchar:logchar2])
if len(argv) >= 3:
    testValues = argv[2][1:-1].split(", ")
    for value in range(len(testValues)):
        testValues[value] = float(testValues[value])
# testing our strategy
totalSum = []
profit = [100000000]
rialPocket = 100000000
#            105518789
btcPocket = 0
confidence = 0
DayTradeConfidence = 0
i = 0
bestPrice = 0
sold = False
bought = False
bestPriceSet = False
while i != len(price):
    while True:
        if bought == False and i != len(price):
            btcPocket -= btcPocket
            confidence = 0
            DayTradeConfidence = 0
            # calculating Normal confidence
            if True:
                if True:
                    if float(tsi[-i]) <= testValues[2]:
                        confidence += 1
                    elif float(tsi[-i]) <= testValues[2] + testValues[10]:
                        confidence += 0.5
                if volume[-i][0] == 'R':
                    if float(float(volume[-i][1:])/10) >= testValues[8]:
                        confidence += 1
                    elif float(float(volume[-i][1:])/10) >= testValues[8] - testValues[18]:
                        confidence += 0.5
                if True:
                    if float(rsi[-i]) <= testValues[0]:
                        confidence += 1
                    elif float(rsi[-i]) <= testValues[0] + testValues[12]:
                        confidence += 0.5
                if True:
                    if float(macd[-i]) <= testValues[4]:
                        confidence += 1
                    elif float(macd[-i]) <= testValues[4] + testValues[14]:
                        confidence += 0.5
                if True:
                    if float(bb[-i]) >= testValues[6]:
                        confidence += 1
                    elif float(bb[-i]) >= testValues[6] - testValues[16]:
                        confidence += 0.5
            # calculating DayTrade confidence
            if float(bb[-i]) <= 3.7:
                if True:
                    if float(macd[-i]) <= -1:
                        DayTradeConfidence += 1
                if True:
                    if float(roc[-i]) <= 0:
                        DayTradeConfidence += 1
                if True:
                    if float(srsi1[-i]) <= 30:
                        DayTradeConfidence += 1
                    elif float(srsi2[-i]) <= 30:
                        DayTradeConfidence += 1
                if True:
                    if float(tsi[-i]) <= testValues[2]:
                        DayTradeConfidence += 1
            # looking for good situation to buy
            if True:
                # Normal Trade
                if ((confidence >= testValues[20]) and float(smiio[-i]) <= testValues[22]) or bestPriceSet == True:
                    if bestPriceSet == False:
                        bestPrice = int(price[-i]) * 1
                        bestPriceSet = True
                    if bestPrice >= int(price[-i]):
                        btcPocket = (rialPocket / int(price[-i])) * 0.9965
                        # print(
                        #     f"B !Confidence:{confidence}/{testValues[20]}, BTC={int(price[-i])}, RSI={rsi[-i]}/{testValues[0]}, TSI={tsi[-i]}/{testValues[2]}, MACD={macd[-i]}/{testValues[4]}, BB={bb[-i]}/{testValues[6]}, Volume={volume[-i]}/{testValues[8]*10}, SMIIO={smiio[-i]}/{testValues[22]}, ROC={roc[-i]}, {btcPocket}, {int(((len(price)-i)*25)/3600)}"
                        # )
                        bought = True
                        bestPriceSet = False
                # DayTrade
                elif ((DayTradeConfidence == 4) and volume[-i][0] == 'R' and float(bb[-i]) <= 3.7 and float(smiio[-i]) <= testValues[22]) or bestPriceSet == True:
                    if bestPriceSet == False:
                        bestPrice = int(price[-i]) * 1
                        bestPriceSet = True
                    if bestPrice >= int(price[-i]):
                        btcPocket = (rialPocket / int(price[-i])) * 0.9965
                        print(
                            f"BD ! BTC={int(price[-i])} MACD={macd[-i]}, BB={bb[-i]}, ROC={roc[-i]}, {btcPocket}, {int(((len(price)-i)*25)/3600)}"
                        )
                        bought = True
                        bestPriceSet = False
            i += 1
        else:
            confidence = 0
            DayTradeConfidence = 0
            bought = False
            break

    while True:
        if sold == False and i != len(price):
            rialPocket -= rialPocket
            confidence = 0
            DayTradeConfidence = 0
            # calculating confidence
            if True:
                if True:
                    if float(tsi[-i]) >= testValues[3]:
                        confidence += 1
                    elif float(tsi[-i]) >= testValues[3] - testValues[11]:
                        confidence += 0.5
                if volume[-i][0] == 'G':
                    if float(float(volume[-i][1:])/10) >= testValues[9]:
                        confidence += 1
                    elif float(float(volume[-i][1:])/10) >= testValues[9] - testValues[19]:
                        confidence += 0.5
                if True:
                    if float(rsi[-i]) >= testValues[1]:
                        confidence += 1
                    elif float(rsi[-i]) >= testValues[1] - testValues[13]:
                        confidence += 0.5
                if True:
                    if float(macd[-i]) >= testValues[5]:
                        confidence += 1
                    elif float(macd[-i]) >= testValues[5] - testValues[15]:
                        confidence += 0.5
                if True:
                    if float(bb[-i]) >= testValues[7]:
                        confidence += 1
                    elif float(bb[-i]) >= testValues[7] - testValues[17]:
                        confidence += 0.5
            # calculating DayTrade confidence
            if float(bb[-i]) <= 3.7:
                if True:
                    if float(macd[-i]) >= 0.1:
                        DayTradeConfidence += 1
                if True:
                    if float(roc[-i]) >= 0.5:
                        DayTradeConfidence += 1
                if True:
                    if float(srsi1[-i]) >= 80:
                        DayTradeConfidence += 1
                    elif float(srsi2[-i]) >= 80:
                        DayTradeConfidence += 1
                if True:
                    if float(tsi[-i]) >= testValues[3]:
                        DayTradeConfidence += 1
            # looking for good situation to sell
            if True:
                if ((confidence >= testValues[21]) and float(smiio[-i]) >= testValues[23]) or bestPriceSet == True:
                    if bestPriceSet == False:
                        bestPrice = int(price[-i]) * 1
                        bestPriceSet = True
                    if bestPrice <= int(price[-i]):
                        rialPocket = (btcPocket * int(price[-i])) * 0.9965
                        profit.append(rialPocket)
                        # print(
                        #     f"S !Confidence:{confidence}/{testValues[21]}, BTC={int(price[-i])}, RSI={rsi[-i]}/{testValues[1]}, TSI={tsi[-i]}/{testValues[3]}, MACD={macd[-i]}/{testValues[5]}, BB={bb[-i]}/{testValues[7]}, Volume={volume[-i]}/{testValues[9]*10}, SMIIO={smiio[-i]}/{testValues[23]}, ROC={roc[-i]}, {rialPocket}, {int(((len(price)-i)*25)/3600)}"
                        # )
                        sold = True
                        bestPriceSet = False
                elif ((DayTradeConfidence == 4) and volume[-i][0] == 'G' and float(bb[-i]) >= 3.7 and float(smiio[-i]) >= testValues[23]) or bestPriceSet == True:
                    if bestPriceSet == False:
                        bestPrice = int(price[-i]) * 1
                        bestPriceSet = True
                    if bestPrice <= int(price[-i]):
                        rialPocket = (btcPocket * int(price[-i])) * 0.9965
                        profit.append(rialPocket)
                        print(
                            f"SD ! BTC={int(price[-i])}, MACD={macd[-i]}, BB={bb[-i]}, ROC={roc[-i]}, {rialPocket}, {int(((len(price)-i)*25)/3600)}"
                        )
                        sold = True
                        bestPriceSet = False
            i += 1
        else:
            confidence = 0
            DayTradeConfidence = 0
            sold = False
            break

if rialPocket == 0:
    rialPocket = btcPocket * 205000000
if btcPocket == 0:
    btcPocket = rialPocket / 205000000
# average profit per trade
for value in range(len(profit)-1):
    totalSum.append(profit[value+1] - profit[value])
print(
    f"balance: {rialPocket}, {btcPocket}, Average Profit: {int(Average(totalSum))/1000000}%")
