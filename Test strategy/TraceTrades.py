import random

# load datasets
price = []
rsi = []
tsi = []
macd = []
bb = []
volume = []
smiio = []
# load datasets from files
def load(filename, indicator):
    f = open("./datasets/"+filename, "r")
    for l in f:
        cPlace = l[:-1]
        indicator.append(cPlace)
    f.close()

testValues = [37,63,-0.0,0.3,-2,8,9,7,4,4,0.2,0.0,6,0,6,2,9,3,2,3,3.5,4.5,-0.1,0.0,0.0,0.3]

# open file and read the content in a list
load("datasetPrice.txt", price)
load("datasetRSIval.txt", rsi)
load("datasetTSI.txt", tsi)
load("datasetMACD.txt", macd)
load("datasetBB.txt", bb)
load("datasetVolume.txt", volume)
load("datasetSMIIO.txt", smiio)

# testing our strategy
for x in range(1):
    rialPocket = 100000
    btcPocket = 0
    confidence = 0
    i = 0
    sold = False
    bought = False
    while i != len(price):
        while True:
            if bought == False and i != len(price):
                confidence = 0
                # calculating confidence
                if True:
                    if True:
                        if float(tsi[-i]) <= testValues[2]:
                            confidence += 1
                        elif float(tsi[-i]) <= testValues[2] + testValues[10]:
                            confidence += 0.5
                    if True:
                        if float(smiio[-i]) <= testValues[22]:
                            confidence += 1
                        elif float(smiio[-i]) <= testValues[22] + testValues[24]:
                            confidence += 0.5
                    if volume[-i][0] == 'R':
                        if float(float(volume[-i][1:])/10) >= testValues[8]:
                            confidence += 1
                        elif float(float(volume[-i][1:])/10) >= testValues[8] - testValues[18]:
                            confidence += 0.5
                    if True:
                        if float(rsi[-i]) <= testValues[0]:
                            confidence += 1
                        elif float(rsi[-i]) <= testValues[0] + testValues[12]:
                            confidence += 0.5
                    if True:
                        if float(macd[-i]) <= testValues[4]:
                            confidence += 1
                        elif float(macd[-i]) <= testValues[4] + testValues[14]:
                            confidence += 0.5
                    if True:
                        if float(bb[-i]) >= testValues[6]:
                            confidence += 1
                        elif float(bb[-i]) >= testValues[6] + testValues[16]:
                            confidence += 0.5
                # looking for good situation to buy
                if (confidence >= testValues[20]):
                    btcPocket = (rialPocket / int(price[-i])) * 0.9965
                    rialPocket -= rialPocket
                    print(
                        f"B !Confidence:{confidence}/{testValues[20]}, BTC={int(price[-i])}, RSI={rsi[-i]}/{testValues[0]}, TSI={tsi[-i]}/{testValues[2]}, MACD={macd[-i]}/{testValues[4]}, BB={bb[-i]}/{testValues[6]}, Volume={volume[-i]}/{testValues[8]*10}, SMIIO={smiio[-i]}/{testValues[24]}, {btcPocket}, {len(price)-i}"
                    )
                    bought = True
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
                        if float(tsi[-i]) >= testValues[3]:
                            confidence += 1
                        elif float(tsi[-i]) >= testValues[3] - testValues[11]:
                            confidence += 0.5
                    if True:
                        if float(smiio[-i]) >= testValues[23]:
                            confidence += 1
                        elif float(smiio[-i]) >= testValues[23] - testValues[25]:
                            confidence += 0.5
                    if volume[-i][0] == 'G':
                        if float(float(volume[-i][1:])/10) >= testValues[9]:
                            confidence += 1
                        elif float(float(volume[-i][1:])/10) >= testValues[9] - testValues[19]:
                            confidence += 0.5
                    if True:
                        if float(rsi[-i]) >= testValues[1]:
                            confidence += 1
                        elif float(rsi[-i]) >= testValues[1] - testValues[13]:
                            confidence += 0.5
                    if True:
                        if float(macd[-i]) >= testValues[5]:
                            confidence += 1
                        elif float(macd[-i]) >= testValues[5] - testValues[15]:
                            confidence += 0.5
                    if True:
                        if float(bb[-i]) >= testValues[7]:
                            confidence += 1
                        elif float(bb[-i]) >= testValues[7] - testValues[17]:
                            confidence += 0.5
                # looking for good situation to sell
                if (confidence >= testValues[21]):
                    rialPocket = (btcPocket * int(price[-i])) * 0.9965
                    btcPocket -= btcPocket
                    print(
                        f"B !Confidence:{confidence}/{testValues[21]}, BTC={int(price[-i])}, RSI={rsi[-i]}/{testValues[1]}, TSI={tsi[-i]}/{testValues[3]}, MACD={macd[-i]}/{testValues[5]}, BB={bb[-i]}/{testValues[7]}, Volume={volume[-i]}/{testValues[9]*10}, SMIIO={smiio[-i]}/{testValues[25]}, {btcPocket}, {len(price)-i}"
                    )
                    sold = True
                i += 1
            else:
                confidence = 0
                sold = False
                break

if rialPocket == 0:
    rialPocket = btcPocket * 185000000
# finding best result
print(f"balance: {rialPocket}")