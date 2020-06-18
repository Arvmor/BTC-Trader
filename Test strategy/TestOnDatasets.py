import random

# load datasets
price = []
rsi = []
tsi = []
macd = []
bb = []
volume = []
highestBalance = []
bestValue = []
bestValue2 = []
bestValue3 = []
bestValue4 = []
bestValue5 = []
bestValue6 = []
bestValue7 = []
bestValue8 = []
bestValue9 = []
bestValue10 = []
bestValue11 = []
bestValue12 = []
bestValue13 = []
bestValue14 = []
bestValue15 = []
bestValue16 = []
bestValue17 = []
bestValue18 = []
bestValue19 = []
bestValue20 = []
bestValue21 = []
bestValue22 = []

# load datasets from files
def load(filename, indicator):
    f = open("../datasets/"+filename, "r")
    for l in f:
        cPlace = l[:-1]
        indicator.append(cPlace)
    f.close()


# open file and read the content in a list
load("datasetPrice.txt", price)
load("datasetRSIval.txt", rsi)
load("datasetTSI.txt", tsi)
load("datasetMACD.txt", macd)
load("datasetBB.txt", bb)
load("datasetVolume.txt", volume)

# testing our strategy with random numbers
for x in range(100000):
    rialPocket = 100000
    btcPocket = 0
    i = 0
    tradeMade = 0
    confidence = 0
    sold = False
    bought = False
    # random values for AI
    b1v = random.choice(range(10)) / -10
    b1v2 = random.choice(range(6)) / 10
    s1v = random.choice(range(10)) / 10
    s1v2 = random.choice(range(6)) / 10
    b2v = random.choice(range(25, 45))
    b2v2 = random.choice(range(10))
    s2v = random.choice(range(55, 75))
    s2v2 = random.choice(range(10))
    b3v = random.choice(range(10))
    b3v2 = random.choice(range(10))
    s3v = random.choice(range(10))
    s3v2 = random.choice(range(10))
    b4v = random.choice(range(10))
    b4v2 = random.choice(range(10))
    s4v = random.choice(range(10))
    s4v2 = random.choice(range(10))
    b5v = random.choice(range(2, 6)) + (random.choice(range(0, 10, 5))/10)
    s5v = random.choice(range(2, 6)) + (random.choice(range(0, 10, 5))/10)
    b6v = random.choice(range(0, 5))
    b6v2 = random.choice(range(0, 5))
    s6v = random.choice(range(0, 5))
    s6v2 = random.choice(range(0, 5))
    # test on our data which is 3810 lines
    while i != 4065:
        while True:
            if bought == False and i != 4065:
                confidence = 0
                # calculating confidence
                if True:
                    if True:
                        if float(tsi[-i]) <= b1v:
                            confidence += 1
                        elif float(tsi[-i]) <= b1v + b1v2:
                            confidence += 0.5
                    if volume[-i][0] == 'R':
                        if float(volume[-i][1:]/10) >= b6v:
                            confidence += 1
                        elif float(volume[-i][1:]/10) >= b6v - b6v2:
                            confidence += 0.5
                    if True:
                        if float(rsi[-i]) <= b2v:
                            confidence += 1
                        elif float(rsi[-i]) <= b2v + b2v2:
                            confidence += 0.5
                    if True:
                        if int(macd[-i])/100000 >= b3v:
                            confidence += 1
                        elif int(macd[-i])/100000 >= b3v + b3v2:
                            confidence += 0.5
                    if True:
                        if float(int(bb[-i])/1000000) >= b4v:
                            confidence += 1
                        elif float(int(bb[-i])/1000000) >= b4v + b4v2:
                            confidence += 0.5
                # looking for good situation to buy
                if (confidence >= b5v):
                    btcPocket = (
                        rialPocket / int(price[-i])) * 0.9965
                    rialPocket -= rialPocket
                    bought = True
                    tradeMade += 1
                i += 1
            else:
                confidence = 0
                bought = False
                break

        while True:
            if sold == False and i != 4065:
                confidence = 0
                # calculating confidence
                if True:
                    if True:
                        if float(tsi[-i]) >= s1v:
                            confidence += 1
                        elif float(tsi[-i]) >= s1v - s1v2:
                            confidence += 0.5
                    if volume[-i][0] == 'G':
                        if float(volume[-i][1:]/10) >= s6v:
                            confidence += 1
                        elif float(volume[-i][1:]/10) >= s6v - s6v2:
                            confidence += 0.5
                    if True:
                        if float(rsi[-i]) >= s2v:
                            confidence += 1
                        elif float(rsi[-i]) >= s2v - s2v2:
                            confidence += 0.5
                    if True:
                        if int(macd[-i])/100000 >= s3v:
                            confidence += 1
                        elif int(macd[-i])/100000 >= s3v - s3v2:
                            confidence += 0.5
                    if True:
                        if float(int(bb[-i])/1000000) >= s4v:
                            confidence += 1
                        elif float(int(bb[-i])/1000000) >= s4v - s4v2:
                            confidence += 0.5
                # looking for good situation to sell
                if (confidence >= s5v):
                    rialPocket = (
                        btcPocket * int(price[-i])) * 0.9965
                    btcPocket -= btcPocket
                    sold = True
                    tradeMade += 1
                i += 1
            else:
                confidence = 0
                sold = False
                break
    if rialPocket == 0:
        rialPocket = btcPocket * 178100000
    if rialPocket >= 209000:
        #results
        highestBalance.append(rialPocket)
        bestValue.append(b1v)
        bestValue2.append(s1v)
        bestValue3.append(b2v)
        bestValue4.append(s2v)
        bestValue5.append(b3v)
        bestValue6.append(s3v)
        bestValue7.append(b4v)
        bestValue8.append(s4v)
        bestValue9.append(b1v2)
        bestValue10.append(s1v2)
        bestValue11.append(b2v2)
        bestValue12.append(s2v2)
        bestValue13.append(b3v2)
        bestValue14.append(s3v2)
        bestValue15.append(b4v2)
        bestValue16.append(s4v2)
        bestValue17.append(b5v)
        bestValue18.append(s5v)
        bestValue19.append(b6v)
        bestValue20.append(s6v)
        bestValue21.append(b6v2)
        bestValue22.append(s6v2)
    print(f"{x}/100000", end='\r')
# finding best result
maxi = highestBalance.index(max(highestBalance))
print(
    f"{highestBalance[maxi]}, RSI's: {bestValue3[maxi]} {bestValue4[maxi]}, TSI's: {bestValue[maxi]} {bestValue2[maxi]}, MACD: {bestValue5[maxi]} {bestValue6[maxi]}, BB: {bestValue7[maxi]} {bestValue8[maxi]} !"
)
print(
    f"TSIc: {bestValue9[maxi]} {bestValue10[maxi]}, RSIc: {bestValue11[maxi]} {bestValue12[maxi]}, MACDc {bestValue13[maxi]} {bestValue14[maxi]}, BBc: {bestValue15[maxi]} {bestValue16[maxi]}, Confidence: {bestValue17[maxi]} {bestValue18[maxi]}"
)