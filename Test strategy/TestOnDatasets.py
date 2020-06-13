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
    sold = False
    bought = False
    # random values for AI
    bv = random.choice(range(10)) / -10
    sv = random.choice(range(10)) / 10
    b2v = random.choice(range(30, 51))
    s2v = random.choice(range(50, 71))
    bmacdv = random.choice(range(0, 10))
    smacdv = random.choice(range(0, 10))
    bbbv = random.choice(range(0, 10))
    sbbv = random.choice(range(0, 10))
    # test on our data
    while i != 3809:
        while True:
            if bought == False and i != 3809:
                if (
                    float(rsi[-i]) <= b2v
                    and float(tsi[-i]) <= bv
                    and int(macd[-i])/10 >= bmacdv
                    and float(int(bb[-i])/100) >= bbbv
                ):
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
                if (
                    float(rsi[-i]) >= s2v
                    and float(tsi[-i]) >= sv
                    and int(macd[-i])/10 >= smacdv
                    and float(int(bb[-i])/100) >= sbbv
                ):
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
        bestValue.append(bv)
        bestValue2.append(sv)
        bestValue3.append(b2v)
        bestValue4.append(s2v)
        bestValue5.append(bmacdv)
        bestValue6.append(smacdv)
        bestValue7.append(bbbv)
        bestValue8.append(sbbv)

# finding best result
maxi = highestBalance.index(max(highestBalance))
print(
    f"{usdtPocket} {highestBalance[maxi]}, RSI's: {bestValue3[maxi]} {bestValue4[maxi]}, TSI's: {bestValue[maxi]} {bestValue2[maxi]}, MACD: {bestValue5[maxi]} {bestValue6[maxi]}, BB: {bestValue7[maxi]} {bestValue8[maxi]} !"
)
