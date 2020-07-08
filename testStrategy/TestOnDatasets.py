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
elif argv[1] == "log":
    load("../log.txt", logs)
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
rounds = 5000
for x in range(rounds):
    rialPocket = 100000
    btcPocket = 0
    i = 0
    tradeMade = 0
    confidence = 0
    sold = False
    bought = False
    # random values for AI
    tsiBuy = choice(range(-9, -3)) / 10
    tsiBuyRange = choice(range(6)) / 10
    tsiSell = choice(range(4, 10)) / 10
    tsiSellRange = choice(range(6)) / 10
    rsiBuy = choice(range(37, 47))
    rsiBuyRange = choice(range(6))
    rsiSell = choice(range(52, 60))
    rsiSellRange = choice(range(6))
    macdBuy = choice(range(-8, -1))
    macdBuyRange = choice(range(6))
    macdSell = choice(range(2, 8))
    macdSellRange = choice(range(6))
    bbBuy = choice(range(10))
    bbBuyRange = choice(range(6))
    bbSell = choice(range(10))
    bbSellRange = choice(range(6))
    confidenceBuy = choice(range(0, 55, 5)) / 10
    confidenceSell = choice(range(0, 55, 5)) / 10
    volumeBuy = choice(range(5))
    volumeBuyRange = choice(range(5))
    volumeSell = choice(range(5))
    volumeSellRange = choice(range(5))
    smiioBuy = choice(range(-8, 0)) / 10
    smiioSell = choice(range(8)) / 10
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
        rialPocket = btcPocket * 200000000
    if btcPocket == 0:
        btcPocket = rialPocket / 200000000
    if highestBalanceRial < rialPocket and highestBalanceBTC < btcPocket:
        # results
        highestBalanceRial = rialPocket
        highestBalanceBTC = btcPocket
        combo = [rsiBuy, rsiSell, tsiBuy, tsiSell, macdBuy, macdSell, bbBuy, bbSell, volumeBuy, volumeSell, tsiBuyRange, tsiSellRange,
                 rsiBuyRange, rsiSellRange, macdBuyRange, macdSellRange, bbBuyRange, bbSellRange, volumeBuyRange, volumeSellRange, confidenceBuy, confidenceSell, smiioBuy, smiioSell]
    print(f" {x}/{rounds}, {floor(highestBalanceRial)} {floor(highestBalanceBTC * 1000000)/1000000} {combo}", end='\r')
# finding best result
print(
    f"{highestBalanceRial} ! \n {combo}"
)
input("Press any key to exit ...")
