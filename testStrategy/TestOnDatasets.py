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
highestBalanceRial = 0
highestBalanceBTC = 0
combo = []
logs = []
usingDataset = False
usingLog = False
# load datasets from files


def load(filename, indicator):
    f = open("../datasets/"+filename, "r")
    for l in f:
        cPlace = l[:-1]
        indicator.append(cPlace)
    f.close()


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
    usingDataset = True
elif argv[1] == "log":
    load("../log.txt", logs)
    usingLog = True
    for log in logs:
        logchar = 0
        logchar2 = 0
        # Price
        while log[logchar] != ' ':
            logchar += 1
        price.append(log[:logchar])
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

# testing our strategy with random numbers
if usingDataset == True:
    rounds = 40000
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
        # test on our data which is n lines
        while i != len(price):
            while True:
                if bought == False and i != len(price):
                    btcPocket -= btcPocket
                    confidence = 0
                    # calculating confidence
                    if True:
                        if True:
                            if float(tsi[-i]) <= tsiBuy:
                                confidence += 1
                            elif float(tsi[-i]) <= tsiBuy + tsiBuyRange:
                                confidence += 0.5
                        if volume[-i][0] == 'R':
                            if float(float(volume[-i][1:])/10) >= volumeBuy:
                                confidence += 1
                            elif float(float(volume[-i][1:])/10) >= volumeBuy - volumeBuyRange:
                                confidence += 0.5
                        if True:
                            if float(rsi[-i]) <= rsiBuy:
                                confidence += 1
                            elif float(rsi[-i]) <= rsiBuy + rsiBuyRange:
                                confidence += 0.5
                        if True:
                            if float(macd[-i]) <= macdBuy:
                                confidence += 1
                            elif float(macd[-i]) <= macdBuy + macdBuyRange:
                                confidence += 0.5
                        if True:
                            if float(bb[-i]) >= bbBuy:
                                confidence += 1
                            elif float(bb[-i]) >= bbBuy - bbBuyRange:
                                confidence += 0.5
                        if True:
                            if float(roc[-i]) <= rocBuy:
                                confidence += 1
                        if True:
                            if float(srsi1[-i]) <= srsiBuy:
                                confidence += 1
                            if float(srsi2[-i]) <= srsiBuy:
                                confidence += 1
                    # looking for good situation to buy
                    if (confidence >= confidenceBuy) and float(smiio[-i]) <= smiioBuy:
                        btcPocket = (
                            rialPocket / int(price[-i])) * 0.9965
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
                    if True:
                        if True:
                            if float(tsi[-i]) >= tsiSell:
                                confidence += 1
                            elif float(tsi[-i]) >= tsiSell - tsiSellRange:
                                confidence += 0.5
                        if volume[-i][0] == 'G':
                            if float(float(volume[-i][1:])/10) >= volumeSell:
                                confidence += 1
                            elif float(float(volume[-i][1:])/10) >= volumeSell - volumeSellRange:
                                confidence += 0.5
                        if True:
                            if float(rsi[-i]) >= rsiSell:
                                confidence += 1
                            elif float(rsi[-i]) >= rsiSell - rsiSellRange:
                                confidence += 0.5
                        if True:
                            if float(macd[-i]) >= macdSell:
                                confidence += 1
                            elif float(macd[-i]) >= macdSell - macdSellRange:
                                confidence += 0.5
                        if True:
                            if float(bb[-i]) >= bbSell:
                                confidence += 1
                            elif float(bb[-i]) >= bbSell - bbSellRange:
                                confidence += 0.5
                        if True:
                            if float(roc[-i]) >= rocSell:
                                confidence += 1
                        if True:
                            if float(srsi1[-i]) >= srsiSell:
                                confidence += 1
                            elif float(srsi2[-i]) >= srsiSell:
                                confidence += 1
                    # looking for good situation to sell
                    if (confidence >= confidenceSell) and float(smiio[-i]) >= smiioSell:
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
            rialPocket = btcPocket * int(price[-i])
        if btcPocket == 0:
            btcPocket = rialPocket / int(price[-i])
        if highestBalanceRial < rialPocket and highestBalanceBTC < btcPocket:
            # results
            highestBalanceRial = rialPocket
            highestBalanceBTC = btcPocket
            combo = [rsiBuy, rsiSell, tsiBuy, tsiSell, macdBuy, macdSell, bbBuy, bbSell, volumeBuy, volumeSell, tsiBuyRange, tsiSellRange, rsiBuyRange, rsiSellRange, macdBuyRange,
                     macdSellRange, bbBuyRange, bbSellRange, volumeBuyRange, volumeSellRange, confidenceBuy, confidenceSell, smiioBuy, smiioSell, rocBuy, rocSell, srsiBuy, srsiSell]
        print(f" {x}/{rounds}, {floor(highestBalanceRial)} {floor(highestBalanceBTC * 1000000)/1000000}", end='\r')
    # finding best result
    print(
        f"{highestBalanceRial} ! \n {combo}"
    )
    input("Press any key to exit ...")
elif usingLog == True:
    # random values for Testing the Strategy
    tsiBuy = choice(range(-7, 1)) / 10
    tsiSell = choice(range(0, 8)) / 10
    macdBuy = choice(range(-4, 1))
    macdSell = choice(range(0, 5))
    volumeBuy = choice(range(5))
    volumeSell = choice(range(5))
    rocBuy = choice(range(-10, 20, 5)) / 10
    rocSell = choice(range(0, 25, 5)) / 10
    srsiBuy = choice(range(10, 20))
    srsiSell = choice(range(75, 81))
    confidenceBuy = choice(range(0, 6))
    confidenceSell = choice(range(0, 6))
    # Create combinations
    rounds = 5000
    for x in range(rounds):
        rialPocket = 100000
        btcPocket = 0
        i = 0
        tradeMade = 0
        confidence = 0
        sold = False
        bought = False
        # test on our data which is n lines
        while i != len(price):
            while True:
                if bought == False and i != len(price):
                    btcPocket -= btcPocket
                    confidence = 0
                    # calculating confidence
                    if True:
                        if True:
                            if float(tsi[-i]) <= tsiBuy:
                                confidence += 1
                        if True:
                            if float(macd[-i]) <= macdBuy:
                                confidence += 1
                        if volume[-i][0] == 'R':
                            if float(volume[-i][1:]) >= volumeBuy:
                                confidence += 1
                        if True:
                            if float(roc[-i]) <= rocBuy:
                                confidence += 1
                        if True:
                            if float(srsi1[-i]) <= srsiBuy:
                                confidence += 1
                            if float(srsi2[-i]) <= srsiBuy:
                                confidence += 1
                    # looking for good situation to buy
                    if (confidence >= confidenceBuy):
                        btcPocket = (
                            rialPocket / int(price[-i])) * 0.9965
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
                    if True:
                        if True:
                            if float(tsi[-i]) >= tsiSell:
                                confidence += 1
                        if True:
                            if float(macd[-i]) >= macdSell:
                                confidence += 1
                        if volume[-i][0] == 'G':
                            if float(volume[-i][1:]) >= volumeSell:
                                confidence += 1
                        if True:
                            if float(roc[-i]) >= rocSell:
                                confidence += 1
                        if True:
                            if float(srsi1[-i]) >= srsiSell:
                                confidence += 1
                            elif float(srsi2[-i]) >= srsiSell:
                                confidence += 1
                    # looking for good situation to sell
                    if (confidence >= confidenceSell):
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
            rialPocket = btcPocket * 200000000
        if btcPocket == 0:
            btcPocket = rialPocket / 200000000
        if highestBalanceRial < rialPocket and highestBalanceBTC < btcPocket:
            # results
            highestBalanceRial = rialPocket
            highestBalanceBTC = btcPocket
            combo = [tsiBuy, tsiSell, macdBuy, macdSell, confidenceBuy, confidenceSell,
                     volumeBuy, volumeSell, rocBuy, rocSell, srsiBuy, srsiSell]
        print(
            f" {x}/{rounds}, {floor(highestBalanceRial)} {floor(highestBalanceBTC * 1000000)/1000000}", end='\r')
    # finding best result
    print(
        f"{highestBalanceRial} ! \n {combo}"
    )
    input("Press any key to exit ...")
