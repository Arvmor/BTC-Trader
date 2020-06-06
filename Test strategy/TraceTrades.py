import random

# load datasets
price = []
rsi = []
tsi = []
macd = []


def load(filename, indicator):
    with open(
        "C:/Users/123/Documents/GitHub/USD-Trader - code/datasets/" + filename, "r"
    ) as fhandle:
        for l in fhandle:
            cPlace = l[:-1]
            indicator.append(cPlace)


# open file and read the content in a list
load("datasetPrice.txt", price)
load("datasetRSIval.txt", rsi)
load("datasetTSI.txt", tsi)
load("datasetMACD.txt", macd)

# testing our strategy
for x in range(1):
    rialPocket = 100000
    usdtPocket = 0
    i = 0
    sold = False
    bought = False
    while i != 1999:
        while True:
            if bought == False and i != 1999:
                if float(rsi[-i]) <= 48.5 and float(tsi[-i]) <= 0 and int(macd[-i]) >= 72:
                    usdtPocket = (rialPocket / int(price[-i])) * 0.9965
                    rialPocket -= rialPocket
                    print(
                        f"Bought ! usdt={int(price[-i])}, RSI={rsi[-i]} TSI={tsi[-i]}, MACD={macd[-i]},{usdtPocket}, {i}"
                    )
                    bought = True
                i += 1
            else:
                bought = False
                break

        while True:
            if sold == False and i != 1999:
                if float(rsi[-i]) >= 61.1 and float(tsi[-i]) >= 0.7 and int(macd[-i]) >= 72:
                    rialPocket = (usdtPocket * int(price[-i])) * 0.9965
                    usdtPocket -= usdtPocket
                    print(
                        f"Sold ! usdt={int(price[-i])}, RSI={rsi[-i]} TSI={tsi[-i]}, MACD={macd[-i]},{rialPocket}, {i}"
                    )
                    sold = True
                i += 1
            else:
                sold = False
                break

if rialPocket == 0:
    rialPocket = usdtPocket * 17600
# finding best result
print(f"balance: {rialPocket}")
