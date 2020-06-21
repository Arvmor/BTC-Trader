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

testValues = [44,56,-0.8,0.2,2,7,6,8,3,2,0.5,0.0,0,7,8,1,0,5,2,4,4,5,0,0,0,0]

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
                        if int(macd[-i])/100000 <= testValues[4]:
                            confidence += 1
                        elif int(macd[-i])/100000 <= testValues[4] + testValues[14]:
                            confidence += 0.5
                    if True:
                        if float(int(bb[-i])/1000000) >= testValues[6]:
                            confidence += 1
                        elif float(int(bb[-i])/1000000) >= testValues[6] + testValues[16]:
                            confidence += 0.5
                # looking for good situation to buy
                if (confidence >= testValues[20]):
                    btcPocket = (rialPocket / int(price[-i])) * 0.9965
                    rialPocket -= rialPocket
                    print(
                        f"B !Confidence:{confidence}, BTC={int(price[-i])}, RSI={rsi[-i]}, TSI={tsi[-i]}, MACD={macd[-i]}, BB={bb[-i]}, Volume={volume[-i]}, SMIIO={smiio[-i]}, {btcPocket}, {4090-i}"
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
                        if int(macd[-i])/100000 >= testValues[5]:
                            confidence += 1
                        elif int(macd[-i])/100000 >= testValues[5] - testValues[15]:
                            confidence += 0.5
                    if True:
                        if float(int(bb[-i])/1000000) >= testValues[7]:
                            confidence += 1
                        elif float(int(bb[-i])/1000000) >= testValues[7] - testValues[17]:
                            confidence += 0.5
                # looking for good situation to sell
                if (confidence >= testValues[21]):
                    rialPocket = (btcPocket * int(price[-i])) * 0.9965
                    btcPocket -= btcPocket
                    print(
                        f"S !Confidence:{confidence}, BTC={int(price[-i])}, RSI={rsi[-i]}, TSI={tsi[-i]}, MACD={macd[-i]}, BB={bb[-i]}, Volume={volume[-i]}, SMIIO={smiio[-i]}, {rialPocket}, {4090-i}"
                    )
                    sold = True
                i += 1
            else:
                confidence = 0
                sold = False
                break

if rialPocket == 0:
    rialPocket = btcPocket * 180000000
# finding best result
print(f"balance: {rialPocket}")