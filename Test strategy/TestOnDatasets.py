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
for x in range(7000000):
    rialPocket = 100000
    usdtPocket = 0
    i = 0
    tradeMade = 0
    confident = 0
    sold = False
    bought = False
    # random values for AI
    b1v = random.choice(range(10)) / -10
    s1v = random.choice(range(10)) / 10
    b2v = random.choice(range(30, 51))
    s2v = random.choice(range(50, 71))
    b3v = random.choice(range(0, 10))
    s3v = random.choice(range(0, 10))
    b4v = random.choice(range(0, 10))
    s4v = random.choice(range(0, 10))
    b5v = random.choice(range(2, 5)) + (random.choice(range(0, 10, 5))/10)
    s5v = random.choice(range(2, 5)) + (random.choice(range(0, 10, 5))/10)
    # test on our data which is 3810 lines
    while i != 3809:
        while True:
            if bought == False and i != 3809:
                # calculating confidence
                if True:
                    if True:
                        if float(tsi[-i]) <= b1v:
                            confident += 1
                        elif float(tsi[-i]) <= b1v + 0.3:
                            confident += 0.5
                    if True:
                        if float(rsi[-i]) <= b2v:
                            confident += 1
                        elif float(rsi[-i]) <= b2v + 5:
                            confident += 0.5
                    if True:
                        if int(macd[-i])/10 >= b3v:
                            confident += 1
                        elif int(macd[-i])/10 >= b3v + 5:
                            confident += 0.5
                    if True:
                        if float(int(bb[-i])/100) >= b4v:
                            confident += 1
                        elif float(int(bb[-i])/100) >= b4v + 5:
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
                bought = False
                break

        while True:
            if sold == False and i != 3809:
                # calculating confidence
                if True:
                    if True:
                        if float(tsi[-i]) >= s1v:
                            confident += 1
                        elif float(tsi[-i]) >= s1v - 0.3:
                            confident += 0.5
                    if True:
                        if float(rsi[-i]) >= s2v:
                            confident += 1
                        elif float(rsi[-i]) >= s2v - 5:
                            confident += 0.5
                    if True:
                        if int(macd[-i])/10 >= s3v:
                            confident += 1
                        elif int(macd[-i])/10 >= s3v - 5:
                            confident += 0.5
                    if True:
                        if float(int(bb[-i])/100) >= s4v:
                            confident += 1
                        elif float(int(bb[-i])/100) >= s4v - 5:
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
                sold = False
                break
    if usdtPocket == 0:
        usdtPocket = rialPocket / 18400
    if usdtPocket >= 6:
        highestBalance.append(usdtPocket)
        bestValue.append(b1v)
        bestValue2.append(s1v)
        bestValue3.append(b2v)
        bestValue4.append(s2v)
        bestValue5.append(b3v)
        bestValue6.append(s3v)
        bestValue7.append(b4v)
        bestValue8.append(s4v)

# finding best result
maxi = highestBalance.index(max(highestBalance))
print(
    f"{usdtPocket} {highestBalance[maxi]}, RSI's: {bestValue3[maxi]} {bestValue4[maxi]}, TSI's: {bestValue[maxi]} {bestValue2[maxi]}, MACD: {bestValue5[maxi]} {bestValue6[maxi]}, BB: {bestValue7[maxi]} {bestValue8[maxi]} !"
)
