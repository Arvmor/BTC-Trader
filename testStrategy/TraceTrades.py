#!/usr/bin/env python3
from sys import argv
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
testValues = [50, 50, -0.9, 0.2, -1, 9, 4, 8, 1, 0, 0.2, 0.5, 1,
              5, 2, 5, 9, 2, 2, 2, 3.5, 6.5, -0.1, 0.0, -3.0, 1.5, 50, 90]
# load datasets from files


def load(filename, indicator, mode, rare=0):
    f = open(f"../{mode}/{filename}", "r")
    if rare == 0:
        for l in f:
            cPlace = l[:-1]
            indicator.append(float(cPlace))
    else:
        for l in f:
            cPlace = l[:-1]
            indicator.append(cPlace)
    f.close()


def Average(lst):
    return sum(lst) / len(lst)


if argv[1] == "dataset":
    # open file and read the content in a list
    load("datasetPrice.txt", price, "datasets")
    load("datasetRSIval.txt", rsi, "datasets")
    load("datasetTSI.txt", tsi, "datasets")
    load("datasetMACD.txt", macd, "datasets")
    load("datasetBB.txt", bb, "datasets")
    load("datasetVolume.txt", volume, "datasets", 1)
    load("datasetSMIIO.txt", smiio, "datasets")
    load("datasetROC.txt", roc, "datasets")
    load("datasetSRSI.txt", srsi1, "datasets")
    load("datasetSRSI2.txt", srsi2, "datasets")
elif argv[1] == "log":
    load("datasetPrice.txt", price, "log")
    load("datasetRSIval.txt", rsi, "log")
    load("datasetTSI.txt", tsi, "log")
    load("datasetMACD.txt", macd, "log")
    load("datasetBB.txt", bb, "log")
    load("datasetVolume.txt", volume, "log", 1)
    load("datasetSMIIO.txt", smiio, "log")
    load("datasetROC.txt", roc, "log")
    load("datasetSRSI.txt", srsi1, "log")
    load("datasetSRSI2.txt", srsi2, "log")
if len(argv) >= 3:
    testValues = argv[2][1:-1].split(", ")
    for value in range(len(testValues)):
        testValues[value] = float(testValues[value])
# testing our strategy
totalSum = []
profit = [100000000]
rialPocket = 100000000
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
                if True:
                    if float(roc[-i]) <= testValues[24]:
                        confidence += 1
                if True:
                    if float(srsi1[-i]) <= testValues[26]:
                        confidence += 1
                    elif float(srsi2[-i]) <= testValues[26]:
                        confidence += 1
            # looking for good situation to buy
            if True:
                # Normal Trade
                if ((confidence >= testValues[20]) and float(smiio[-i]) <= testValues[22]) or bestPriceSet == True:
                    if bestPriceSet == False:
                        bestPrice = int(price[-i]) * 1
                        bestPriceSet = True
                    if bestPrice >= int(price[-i]):
                        btcPocket = (rialPocket / int(price[-i])) * 0.9965
                        print(
                            f"B !Confidence:{confidence}/{testValues[20]}, BTC={int(price[-i])}, RSI={rsi[-i]}/{testValues[0]}, TSI={tsi[-i]}/{testValues[2]}, MACD={macd[-i]}/{testValues[4]}, BB={bb[-i]}/{testValues[6]}, Volume={volume[-i]}/{testValues[8]*10}, SMIIO={smiio[-i]}/{testValues[22]}, ROC={roc[-i]}/{testValues[24]} SRSI={srsi1[-i]} {srsi2[-i]}/{testValues[26]}, {btcPocket}, {len(price)-i}"
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
                if True:
                    if float(roc[-i]) >= testValues[25]:
                        confidence += 1
                if True:
                    if float(srsi1[-i]) >= testValues[27]:
                        confidence += 1
                    elif float(srsi2[-i]) >= testValues[27]:
                        confidence += 1
            # looking for good situation to sell
            if True:
                if ((confidence >= testValues[21]) and float(smiio[-i]) >= testValues[23]) or bestPriceSet == True:
                    if bestPriceSet == False:
                        bestPrice = int(price[-i]) * 1
                        bestPriceSet = True
                    if bestPrice <= int(price[-i]):
                        rialPocket = (btcPocket * int(price[-i])) * 0.9965
                        profit.append(rialPocket)
                        print(
                            f"S !Confidence:{confidence}/{testValues[21]}, BTC={int(price[-i])}, RSI={rsi[-i]}/{testValues[1]}, TSI={tsi[-i]}/{testValues[3]}, MACD={macd[-i]}/{testValues[5]}, BB={bb[-i]}/{testValues[7]}, Volume={volume[-i]}/{testValues[9]*10}, SMIIO={smiio[-i]}/{testValues[23]}, ROC={roc[-i]}/{testValues[25]} SRSI={srsi1[-i]} {srsi2[-i]}/{testValues[27]}, {rialPocket}, {len(price)-i}"
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
    rialPocket = btcPocket * 230000000
if btcPocket == 0:
    btcPocket = rialPocket / 230000000
# average profit per trade
profit.append(rialPocket)
for value in range(len(profit)-1):
    totalSum.append(profit[value+1] - profit[value])
print(
    f"balance: {rialPocket/1000}, {btcPocket/1000}, Average Profit: {int(Average(totalSum))/1000000}%")
