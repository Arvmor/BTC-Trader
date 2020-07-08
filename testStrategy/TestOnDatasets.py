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
    b1v = choice(range(-9, -3)) / 10
    b1v2 = choice(range(6)) / 10
    s1v = choice(range(4, 10)) / 10
    s1v2 = choice(range(6)) / 10
    b2v = choice(range(37, 47))
    b2v2 = choice(range(6))
    s2v = choice(range(52, 60))
    s2v2 = choice(range(6))
    b3v = choice(range(-8, -1))
    b3v2 = choice(range(6))
    s3v = choice(range(2, 8))
    s3v2 = choice(range(6))
    b4v = choice(range(10))
    b4v2 = choice(range(6))
    s4v = choice(range(10))
    s4v2 = choice(range(6))
    b5v = choice(range(0, 55, 5)) / 10
    s5v = choice(range(0, 55, 5)) / 10
    b6v = choice(range(5))
    b6v2 = choice(range(5))
    s6v = choice(range(5))
    s6v2 = choice(range(5))
    b7v = choice(range(-8, 0)) / 10
    s7v = choice(range(8)) / 10
    # test on our data which is n lines
    while i != len(price):
        while True:
            if bought == False and i != len(price):
                btcPocket -= btcPocket
                confidence = 0
                # calculating confidence
                if True:
                    if True:
                        if float(tsi[-i]) <= b1v:
                            confidence += 1
                        elif float(tsi[-i]) <= b1v + b1v2:
                            confidence += 0.5
                    if volume[-i][0] == 'R':
                        if float(float(volume[-i][1:])/10) >= b6v:
                            confidence += 1
                        elif float(float(volume[-i][1:])/10) >= b6v - b6v2:
                            confidence += 0.5
                    if True:
                        if float(rsi[-i]) <= b2v:
                            confidence += 1
                        elif float(rsi[-i]) <= b2v + b2v2:
                            confidence += 0.5
                    if True:
                        if float(macd[-i]) <= b3v:
                            confidence += 1
                        elif float(macd[-i]) <= b3v + b3v2:
                            confidence += 0.5
                    if True:
                        if float(bb[-i]) >= b4v:
                            confidence += 1
                        elif float(bb[-i]) >= b4v - b4v2:
                            confidence += 0.5
                # looking for good situation to buy
                if (confidence >= b5v) and float(smiio[-i]) <= b7v:
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
                        if float(tsi[-i]) >= s1v:
                            confidence += 1
                        elif float(tsi[-i]) >= s1v - s1v2:
                            confidence += 0.5
                    if volume[-i][0] == 'G':
                        if float(float(volume[-i][1:])/10) >= s6v:
                            confidence += 1
                        elif float(float(volume[-i][1:])/10) >= s6v - s6v2:
                            confidence += 0.5
                    if True:
                        if float(rsi[-i]) >= s2v:
                            confidence += 1
                        elif float(rsi[-i]) >= s2v - s2v2:
                            confidence += 0.5
                    if True:
                        if float(macd[-i]) >= s3v:
                            confidence += 1
                        elif float(macd[-i]) >= s3v - s3v2:
                            confidence += 0.5
                    if True:
                        if float(bb[-i]) >= s4v:
                            confidence += 1
                        elif float(bb[-i]) >= s4v - s4v2:
                            confidence += 0.5
                # looking for good situation to sell
                if (confidence >= s5v) and float(smiio[-i]) >= s7v:
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
        rialPocket = btcPocket * 190000000
    if btcPocket == 0:
        btcPocket = rialPocket / 190000000
    # if rialPocket > 287200 and btcPocket > 0.01528:
    if highestBalanceRial < rialPocket and highestBalanceBTC < btcPocket:
        # results
        highestBalanceRial = rialPocket
        highestBalanceBTC = btcPocket
        combo = [b2v, s2v, b1v, s1v, b3v, s3v, b4v, s4v, b6v, s6v, b1v2, s1v2,
                 b2v2, s2v2, b3v2, s3v2, b4v2, s4v2, b6v2, s6v2, b5v, s5v, b7v, s7v]
    print(f" {x}/{rounds}, {floor(highestBalanceRial)} {floor(highestBalanceBTC * 1000000)/1000000} {combo}", end='\r')
# finding best result
print(
    f"{highestBalanceRial} ! \n {combo}"
)
input("Press any key to exit ...")
