import random

# load datasets
price = []
rsi = []
tsi = []
macd = []
bb = []


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

# testing our strategy
for x in range(1):
    rialPocket = 100000
    usdtPocket = 0
    confident = 0
    i = 0
    sold = False
    bought = False
while i != 4009:
    while True:
        if bought == False and i != 4009:
            confident = 0
            # calculating confidence
            if True:
                if True:
                    if float(tsi[-i]) <= -0.8:
                        confident += 1
                    elif float(tsi[-i]) <= -0.8 + 0.4:
                        confident += 0.5
                if True:
                    if float(rsi[-i]) <= 34:
                        confident += 1
                    elif float(rsi[-i]) <= 34 + 9:
                        confident += 0.5
                if True:
                    if int(macd[-i])/1000 >= 5:
                        confident += 1
                    elif int(macd[-i])/1000 >= 5 + 3:
                        confident += 0.5
                if True:
                    if float(int(bb[-i])/1000000) >= 0:
                        confident += 1
                    elif float(int(bb[-i])/1000000) >= 0 + 5:
                        confident += 0.5
            # looking for good situation to buy
            if (confident >= 3):
                usdtPocket = (rialPocket / int(price[-i])) * 0.9965
                rialPocket -= rialPocket
                print(
                    f"B !Confidence:{confident}, usdt={int(price[-i])}, RSI={rsi[-i]}, TSI={tsi[-i]}, MACD={float(macd[-i])/10}, BB={float(bb[-i])/100}, {usdtPocket}, {i}"
                )
                bought = True
            i += 1
        else:
            confident = 0
            bought = False
            break

    while True:
        if sold == False and i != 4009:
            confident = 0
            # calculating confidence
            if True:
                if True:
                    if float(tsi[-i]) >= 0.1:
                        confident += 1
                    elif float(tsi[-i]) >= 0.1 - 0.1:
                        confident += 0.5
                if True:
                    if float(rsi[-i]) >= 74:
                        confident += 1
                    elif float(rsi[-i]) >= 74 - 0:
                        confident += 0.5
                if True:
                    if int(macd[-i])/1000 >= 7:
                        confident += 1
                    elif int(macd[-i])/1000 >= 7 - 8:
                        confident += 0.5
                if True:
                    if float(int(bb[-i])/1000000) >= 9:
                        confident += 1
                    elif float(int(bb[-i])/1000000) >= 9 - 7:
                        confident += 0.5
            # looking for good situation to sell
            if (confident >= 4):
                rialPocket = (usdtPocket * int(price[-i])) * 0.9965
                usdtPocket -= usdtPocket
                print(
                    f"S !Confidence:{confident}, usdt={int(price[-i])}, RSI={rsi[-i]}, TSI={tsi[-i]}, MACD={float(macd[-i])/10}, BB={float(bb[-i])/100}, {rialPocket}, {i}"
                )
                sold = True
            i += 1
        else:
            confident = 0
            sold = False
            break

if rialPocket == 0:
    rialPocket = usdtPocket * 178100000
# finding best result
print(f"balance: {rialPocket}")