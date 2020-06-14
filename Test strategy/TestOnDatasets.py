import random

# load datasets
price = []
rsi = []
tsi = []
macd = []
bb = []
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
# testing our strategy
for x in range(15000):
    rialPocket = 100000
    usdtPocket = 0
    i = 0
    tradeMade = 0
    confident = 0
    sold = False
    bought = False
    # random values for AI
    b1v = random.choice(range(10)) / -10
    b1v2 = random.choice(range(6)) / 10
    s1v = random.choice(range(10)) / 10
    s1v2 = random.choice(range(6)) / 10
    b2v = random.choice(range(30, 51))
    b2v2 = random.choice(range(10))
    s2v = random.choice(range(50, 71))
    s2v2 = random.choice(range(10))
    b3v = random.choice(range(10))
    b3v2 = random.choice(range(10))
    s3v = random.choice(range(10))
    s3v2 = random.choice(range(10))
    b4v = random.choice(range(10))
    b4v2 = random.choice(range(10))
    s4v = random.choice(range(10))
    s4v2 = random.choice(range(10))
    b5v = random.choice(range(2, 5)) + (random.choice(range(0, 10, 5))/10)
    s5v = random.choice(range(2, 5)) + (random.choice(range(0, 10, 5))/10)
    # test on our data which is 3810 lines
    while i != 3809:
        while True:
            if bought == False and i != 3809:
                confident = 0
                # calculating confidence
                if True:
                    if True:
                        if float(tsi[-i]) <= b1v:
                            confident += 1
                        elif float(tsi[-i]) <= b1v + b1v2:
                            confident += 0.5
                    if True:
                        if float(rsi[-i]) <= b2v:
                            confident += 1
                        elif float(rsi[-i]) <= b2v + b2v2:
                            confident += 0.5
                    if True:
                        if int(macd[-i])/10 >= b3v:
                            confident += 1
                        elif int(macd[-i])/10 >= b3v + b3v2:
                            confident += 0.5
                    if True:
                        if float(int(bb[-i])/100) >= b4v:
                            confident += 1
                        elif float(int(bb[-i])/100) >= b4v + b4v2:
                            confident += 0.5
                # looking for good situation to buy
                if (confident >= b5v):
                    usdtPocket = (
                        rialPocket / int(price[-i])) * 0.9965
                    rialPocket -= rialPocket
                    bought = True
                    tradeMade += 1
                i += 1
            else:
                confident = 0
                bought = False
                break

        while True:
            if sold == False and i != 3809:
                confident = 0
                # calculating confidence
                if True:
                    if True:
                        if float(tsi[-i]) >= s1v:
                            confident += 1
                        elif float(tsi[-i]) >= s1v - s1v2:
                            confident += 0.5
                    if True:
                        if float(rsi[-i]) >= s2v:
                            confident += 1
                        elif float(rsi[-i]) >= s2v - s2v2:
                            confident += 0.5
                    if True:
                        if int(macd[-i])/10 >= s3v:
                            confident += 1
                        elif int(macd[-i])/10 >= s3v - s3v2:
                            confident += 0.5
                    if True:
                        if float(int(bb[-i])/100) >= s4v:
                            confident += 1
                        elif float(int(bb[-i])/100) >= s4v - s4v2:
                            confident += 0.5
                # looking for good situation to sell
                if (confident >= s5v):
                    rialPocket = (
                        usdtPocket * int(price[-i])) * 0.9965
                    usdtPocket -= usdtPocket
                    sold = True
                    tradeMade += 1
                i += 1
            else:
                confident = 0
                sold = False
                break
    if usdtPocket == 0:
        usdtPocket = rialPocket / 18400
    if usdtPocket >= 9:
        #results
        highestBalance.append(usdtPocket)
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

# finding best result
maxi = highestBalance.index(max(highestBalance))
print(
    f"{highestBalance[maxi]}, RSI's: {bestValue3[maxi]} {bestValue4[maxi]}, TSI's: {bestValue[maxi]} {bestValue2[maxi]}, MACD: {bestValue5[maxi]} {bestValue6[maxi]}, BB: {bestValue7[maxi]} {bestValue8[maxi]} !"
)
print(
    f"TSIc: {bestValue9[maxi]} {bestValue10[maxi]}, RSIc: {bestValue11[maxi]} {bestValue12[maxi]}, MACDc {bestValue13[maxi]} {bestValue14[maxi]}, BBc: {bestValue15[maxi]} {bestValue16[maxi]}, Confidenc: {bestValue17[maxi]} {bestValue18[maxi]}"
)