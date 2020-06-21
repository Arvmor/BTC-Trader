import random

# load datasets
price = []
rsi = []
tsi = []
macd = []
bb = []
volume = []
smiio = []
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
bestValue23 = []
bestValue24 = []
bestValue25 = []
bestValue26 = []

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
load("datasetSMIIO.txt", smiio)

# testing our strategy with random numbers
rounds = 100000
for x in range(rounds):
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
    b2v = random.choice(range(35, 45))
    b2v2 = random.choice(range(10))
    s2v = random.choice(range(55, 65))
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
    b6v = random.choice(range(5))
    b6v2 = random.choice(range(5))
    s6v = random.choice(range(5))
    s6v2 = random.choice(range(5))
    b7v = random.choice(range(8)) / -10
    b7v2 = random.choice(range(5)) / 10
    s7v = random.choice(range(8)) / 10
    s7v2 = random.choice(range(5)) / 10
    # test on our data which is 3810 lines
    while i != len(price):
        while True:
            if bought == False and i != len(price):
                confidence = 0
                # calculating confidence
                if True:
                    if True:
                        if float(tsi[-i]) <= b1v:
                            confidence += 1
                        elif float(tsi[-i]) <= b1v + b1v2:
                            confidence += 0.5
                    if True:
                        if float(smiio[-i]) <= b7v:
                            confidence += 1
                        elif float(smiio[-i]) <= b7v + b7v2:
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
                        if int(macd[-i])/100000 <= b3v:
                            confidence += 1
                        elif int(macd[-i])/100000 <= b3v + b3v2:
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
            if sold == False and i != len(price):
                confidence = 0
                # calculating confidence
                if True:
                    if True:
                        if float(tsi[-i]) >= s1v:
                            confidence += 1
                        elif float(tsi[-i]) >= s1v - s1v2:
                            confidence += 0.5
                    if True:
                        if float(smiio[-i]) >= s7v:
                            confidence += 1
                        elif float(smiio[-i]) >= s7v - s7v2:
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
        rialPocket = btcPocket * 180000000
    if rialPocket >= 297452:
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
        bestValue23.append(b7v)
        bestValue24.append(b7v2)
        bestValue25.append(s7v)
        bestValue26.append(s7v2)
    print(f" {x}/{rounds}", end='\r')
# finding best result
maxi = highestBalance.index(max(highestBalance))
print(
    f"{highestBalance[maxi]} !"
)
print(
    f"[{bestValue3[maxi]},{bestValue4[maxi]},{bestValue[maxi]},{bestValue2[maxi]},{bestValue5[maxi]},{bestValue6[maxi]},{bestValue7[maxi]},{bestValue8[maxi]},{bestValue19[maxi]},{bestValue20[maxi]},{bestValue9[maxi]},{bestValue10[maxi]},{bestValue11[maxi]},{bestValue12[maxi]},{bestValue13[maxi]},{bestValue14[maxi]},{bestValue15[maxi]},{bestValue16[maxi]},{bestValue21[maxi]},{bestValue22[maxi]},{bestValue17[maxi]},{bestValue18[maxi]},{bestValue23[maxi]},{bestValue25[maxi]},{bestValue24[maxi]},{bestValue26[maxi]}]"
)
input("Press any key to exit ...")