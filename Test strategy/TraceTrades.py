import random

# load datasets
price = []
rsi = []
tsi = []
macd = []
bb = []
volume = []
# load datasets from files
def load(filename, indicator):
    f = open("./datasets/"+filename, "r")
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

# testing our strategy
for x in range(1):
    rialPocket = 100000
    btcPocket = 0
    confidence = 0
    i = 0
    sold = False
    bought = False
    while i != 4065:
        while True:
            if bought == False and i != 4065:
                confidence = 0
                # calculating confidence
                if True:
                    if True:
                        if float(tsi[-i]) <= -0.9:
                            confidence += 1
                        elif float(tsi[-i]) <= -0.9 + 0.0:
                            confidence += 0.5
                    if volume[-i][0] == 'R':
                        if float(float(volume[-i][1:])/10) >= 0:
                            confidence += 1
                        elif float(float(volume[-i][1:])/10) >= 0 - 0:
                            confidence += 0.5
                    if True:
                        if float(rsi[-i]) <= 39:
                            confidence += 1
                        elif float(rsi[-i]) <= 39 + 7:
                            confidence += 0.5
                    if True:
                        if int(macd[-i])/100000 >= 1:
                            confidence += 1
                        elif int(macd[-i])/100000 >= 1 + 0:
                            confidence += 0.5
                    if True:
                        if float(int(bb[-i])/1000000) >= 8:
                            confidence += 1
                        elif float(int(bb[-i])/1000000) >= 8 + 7:
                            confidence += 0.5
                # looking for good situation to buy
                if (confidence >= 3.5):
                    btcPocket = (rialPocket / int(price[-i])) * 0.9965
                    rialPocket -= rialPocket
                    print(
                        f"B !Confidence:{confidence}, BTC={int(price[-i])}, RSI={rsi[-i]}, TSI={tsi[-i]}, MACD={macd[-i]}, BB={bb[-i]}, Volume={volume[-i]}, {btcPocket}, {i}"
                    )
                    bought = True
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
                        if float(tsi[-i]) >= 0.4:
                            confidence += 1
                        elif float(tsi[-i]) >= 0.4 - 0.0:
                            confidence += 0.5
                    if volume[-i][0] == 'G':
                        if float(float(volume[-i][1:])/10) >= 0:
                            confidence += 1
                        elif float(float(volume[-i][1:])/10) >= 0 - 0:
                            confidence += 0.5
                    if True:
                        if float(rsi[-i]) >= 59:
                            confidence += 1
                        elif float(rsi[-i]) >= 59 - 1:
                            confidence += 0.5
                    if True:
                        if int(macd[-i])/100000 >= 1:
                            confidence += 1
                        elif int(macd[-i])/100000 >= 1 - 0.4:
                            confidence += 0.5
                    if True:
                        if float(int(bb[-i])/1000000) >= 8:
                            confidence += 1
                        elif float(int(bb[-i])/1000000) >= 8 - 3:
                            confidence += 0.5
                # looking for good situation to sell
                if (confidence >= 5):
                    rialPocket = (btcPocket * int(price[-i])) * 0.9965
                    btcPocket -= btcPocket
                    print(
                        f"S !Confidence:{confidence}, BTC={int(price[-i])}, RSI={rsi[-i]}, TSI={tsi[-i]}, MACD={macd[-i]}, BB={bb[-i]}, Volume={volume[-i]}, {rialPocket}, {i}"
                    )
                    sold = True
                i += 1
            else:
                confidence = 0
                sold = False
                break

if rialPocket == 0:
    rialPocket = btcPocket * 178100000
# finding best result
print(f"balance: {rialPocket}")