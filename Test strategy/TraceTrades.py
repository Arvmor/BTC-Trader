import random

# load datasets
price = []
rsi = []
tsi = []
macd = []
bb = []


def load(filename, indicator):
    f = open(filename, "r")
    for l in f:
        cPlace = l[:-1]
        indicator.append(cPlace)
    f.close()


# open file and read the content in a list
load("datasetPrice.txt", price)
load("datasetRSIval.txt", rsi)
load("datasetTSI.txt", tsi)
load("datasetMACD2.txt", macd)
load("datasetBB.txt", bb)

# testing our strategy
for x in range(1):
    rialPocket = 100000
    usdtPocket = 0
    i = 0
    sold = False
    bought = False
while i != 3809:
    while True:
        if bought == False and i != 3809:
            if (
                float(rsi[-i]) <= 50
                and float(tsi[-i]) <= -0.0
                and int(macd[-i]) >= 3497
                and float(int(bb[-i])/100) >= 10
            ):
                usdtPocket = (rialPocket / int(price[-i])) * 0.9965
                rialPocket -= rialPocket
                print(
                    f"Bought ! usdt={int(price[-i])}, RSI={rsi[-i]}, TSI={tsi[-i]}, MACD={macd[-i]}, BB={bb[-i]}, {usdtPocket}, {i}"
                )
                bought = True
            i += 1
        else:
            bought = False
            break

    while True:
        if sold == False and i != 3809:
            if (
                float(rsi[-i]) >= 63
                and float(tsi[-i]) >= 0.1
                and int(macd[-i]) >= 3497
                and float(int(bb[-i])/100) >= 10
            ):
                rialPocket = (usdtPocket * int(price[-i])) * 0.9965
                usdtPocket -= usdtPocket
                print(
                    f"Sold ! usdt={int(price[-i])}, RSI={rsi[-i]}, TSI={tsi[-i]}, MACD={macd[-i]}, BB={bb[-i]}, {rialPocket}, {i}"
                )
                sold = True
            i += 1
        else:
            sold = False
            break

if rialPocket == 0:
    rialPocket = usdtPocket
# finding best result
print(f"balance: {rialPocket}")
