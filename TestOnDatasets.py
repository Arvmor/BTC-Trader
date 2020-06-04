import random

# load datasets
price = []
rsi = []
testR = []
testB = []
testS = []
# open file and read the content in a list
with open(
    "/datasets/datasetPrice.txt", "r"
) as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        price.append(currentPlace)

with open(
    "/datasets/datasetRSIval.txt", "r"
) as fhandle:
    for l in fhandle:
        # remove linebreak which is the last character of the string
        cPlace = l[:-1]

        # add item to the list
        rsi.append(cPlace)
for x in range(200000):
    rialPocket = 100000
    usdtPocket = 0
    i = 0
    sold = False
    bought = False
    bv = random.choice(range(30, 50)) + (random.choice(range(10)) / 10)
    sv = random.choice(range(50, 65)) + (random.choice(range(10)) / 10)
    while True:
        if bought == False and i != 1999:
            buy = float(rsi[-i])
            usdtData = int(price[-i])
            if buy <= bv:
                usdtPocket = (rialPocket / usdtData) * 0.9965
                rialPocket -= rialPocket
                bought = True
            i += 1
        else:
            bought = False
            break

    while True:
        if sold == False and i != 1999:
            sell = float(rsi[-i])
            usdtData = int(price[-i])
            if sell >= sv:
                rialPocket = (usdtPocket * usdtData) * 0.9965
                usdtPocket -= usdtPocket
                sold = True
            i += 1
        else:
            sold = False
            break
    testR.append(rialPocket)
    testB.append(bv)
    testS.append(sv)
maxi = testR.index(max(testR))
print(f"{testR[maxi]}, {testB[maxi]}, {testS[maxi]}")
