#!/usr/bin/env python3
from random import choice
from math import floor
from sys import argv

# load datasets
price = []
rsi = []
tsi = []
macd = []
bb = []
volume = []
smiio = []
roc = []
srsi1 = []
srsi2 = []
pvt = []
highestBalanceRial = 0
highestBalanceBTC = 0
combo = []
logs = []
usingDataset = False
usingLog = False
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


def writeFile(filePath, variableName):  # save data into file
    f = open("../log/"+filePath, "+w")
    for d in variableName:
        f.write("%s\n" % d)
    f.close()


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
    load("datasetPVT.txt", pvt, "datasets")
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
# testing our strategy with random numbers
rounds = 500
for x in range(rounds):
    rialPocket = 100000
    btcPocket = 0
    i = 0
    tradeMade = 0
    confidence = 0
    sold = False
    bought = False
    # random values for Testing the Strategy
    tsiBuy = choice(range(-9, 1)) / 10
    tsiBuyRange = choice(range(10)) / 10
    tsiSell = choice(range(10)) / 10
    tsiSellRange = choice(range(10)) / 10
    rsiBuy = choice(range(25, 55, 5))
    rsiBuyRange = choice(range(10))
    rsiSell = choice(range(45, 90, 5))
    rsiSellRange = choice(range(10))
    macdBuy = choice(range(-9, 1))
    macdBuyRange = choice(range(10))
    macdSell = choice(range(10))
    macdSellRange = choice(range(10))
    bbBuy = choice(range(10))
    bbBuyRange = choice(range(10))
    bbSell = choice(range(10))
    bbSellRange = choice(range(10))
    confidenceBuy = choice(range(0, 75, 5)) / 10
    confidenceSell = choice(range(0, 75, 5)) / 10
    volumeBuy = choice(range(3))
    volumeBuyRange = choice(range(3))
    volumeSell = choice(range(3))
    volumeSellRange = choice(range(3))
    smiioBuy = choice(range(-9, 1)) / 10
    smiioSell = choice(range(10)) / 10
    rocBuy = choice(range(-30, 5, 5)) / 10
    rocSell = choice(range(0, 35, 5)) / 10
    srsiBuy = choice(range(0, 55, 5))
    srsiSell = choice(range(50, 105, 5))
    pvtBuy = choice(range(0, 102, 2)) / 10
    pvtSell = choice(range(0, 102, 2)) / -10
    # test on our data which is n lines
    while i != len(price):
        while True:
            if bought == False and i != len(price):
                btcPocket -= btcPocket
                confidence = 0
                # calculating confidence
                if tsi[-i] <= tsiBuy:
                    confidence += 1
                elif tsi[-i] <= tsiBuy + tsiBuyRange:
                    confidence += 0.5
                if volume[-i][0] == 'R':
                    if float(float(volume[-i][1:])/10) >= volumeBuy:
                        confidence += 1
                elif float(float(volume[-i][1:])/10) >= volumeBuy - volumeBuyRange:
                    confidence += 0.5
                if rsi[-i] <= rsiBuy:
                    confidence += 1
                elif rsi[-i] <= rsiBuy + rsiBuyRange:
                    confidence += 0.5
                if macd[-i] <= macdBuy:
                    confidence += 1
                elif macd[-i] <= macdBuy + macdBuyRange:
                    confidence += 0.5
                if bb[-i] >= bbBuy:
                    confidence += 1
                elif bb[-i] >= bbBuy - bbBuyRange:
                    confidence += 0.5
                if roc[-i] <= rocBuy:
                    confidence += 1
                if srsi1[-i] <= srsiBuy:
                    confidence += 1
                elif srsi2[-i] <= srsiBuy:
                    confidence += 1
                # looking for good situation to buy
                if (confidence >= confidenceBuy) and smiio[-i] <= smiioBuy and pvt[-i] <= pvtBuy:
                    btcPocket = (
                        int(rialPocket) / int(price[-i])) * 0.9965
                    bought = True
                    tradeMade += 1
                i += 1
            else:
                confidence = 0
                bought = False
                break

        while True:
            if sold == False and i != len(price):
                rialPocket -= rialPocket
                confidence = 0
                # calculating confidence
                if tsi[-i] >= tsiSell:
                    confidence += 1
                elif tsi[-i] >= tsiSell - tsiSellRange:
                    confidence += 0.5
                if volume[-i][0] == 'G':
                    if float(float(volume[-i][1:])/10) >= volumeSell:
                        confidence += 1
                elif float(float(volume[-i][1:])/10) >= volumeSell - volumeSellRange:
                    confidence += 0.5
                if rsi[-i] >= rsiSell:
                    confidence += 1
                elif rsi[-i] >= rsiSell - rsiSellRange:
                    confidence += 0.5
                if macd[-i] >= macdSell:
                    confidence += 1
                elif macd[-i] >= macdSell - macdSellRange:
                    confidence += 0.5
                if bb[-i] >= bbSell:
                    confidence += 1
                elif bb[-i] >= bbSell - bbSellRange:
                    confidence += 0.5
                if roc[-i] >= rocSell:
                    confidence += 1
                if srsi1[-i] >= srsiSell:
                    confidence += 1
                elif srsi2[-i] >= srsiSell:
                    confidence += 1
                # looking for good situation to sell
                if (confidence >= confidenceSell) and smiio[-i] >= smiioSell and pvt[-i] >= pvtSell:
                    rialPocket = (
                        btcPocket * int(price[-i])) * 0.9965
                    sold = True
                    tradeMade += 1
                i += 1
            else:
                confidence = 0
                sold = False
                break
    if rialPocket == 0:
        rialPocket = btcPocket * 230000000
    if btcPocket == 0:
        btcPocket = rialPocket / 230000000
    if highestBalanceRial < rialPocket and highestBalanceBTC < btcPocket:
        highestBalanceRial = rialPocket
        highestBalanceBTC = btcPocket
        combo = [rsiBuy, rsiSell, tsiBuy, tsiSell, macdBuy, macdSell, bbBuy, bbSell, volumeBuy, volumeSell, tsiBuyRange, tsiSellRange, rsiBuyRange, rsiSellRange, macdBuyRange,
                 macdSellRange, bbBuyRange, bbSellRange, volumeBuyRange, volumeSellRange, confidenceBuy, confidenceSell, smiioBuy, smiioSell, rocBuy, rocSell, srsiBuy, srsiSell, pvtBuy, pvtSell]
    print(f" {x}/{rounds}, {floor(highestBalanceRial)} {floor(highestBalanceBTC * 1000000)/1000000}", end='\r')
# finding best result
print(
    f"{highestBalanceRial} {highestBalanceBTC}! \n {combo}"
)
input("Press any key to exit ...")
