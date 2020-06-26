# Variables
price = []
rsi = []
tsi = []
macd = []
bb = []
volume = []
smiio = []
highestBalance = []
highestBalanceCombo = []

# random values for AI
buyTSI = range(-9,-3)
buyTSI2 = range(6)
sellTSI = range(4,10)
sellTSI2 = range(6)
buyRSI = range(37, 47)
buyRSI2 = range(6)
sellRSI = range(52, 60)
sellRSI2 = range(6)
buyMACD = range(-8, -1)
buyMACD2 = range(6)
sellMACD = range(2,8)
sellMACD2 = range(6)
buyBB = range(10)
buyBB2 = range(6)
sellBB = range(10)
sellBB2 = range(6)
buyConfidence = range(0, 55, 5)
sellConfidence = range(0, 55, 5)
buyVolume = range(5)
buyVolume2 = range(5)
sellVolume = range(5)
sellVolume2 = range(5)
buySMIIO = range(-8, 0)
sellSMIIO = range(8)
# Create combinations
combinations = [[v0,v1,v2/10,v3/10,v4,v5,v6,v7,v8,v9,v10/10,v11/10,v12,v13,v14,v15,v16,v17,v18,v19,v20/10,v21/10,v22/10,v23/10] for v0 in buyRSI
                                                                                                        for v1 in sellRSI
                                                                                                        for v2 in buyTSI
                                                                                                        for v3 in sellTSI
                                                                                                        for v4 in buyMACD
                                                                                                        for v5 in sellMACD
                                                                                                        for v6 in buyBB
                                                                                                        for v7 in sellBB
                                                                                                        for v8 in buyVolume
                                                                                                        for v9 in sellVolume
                                                                                                        for v10 in buyTSI2
                                                                                                        for v11 in sellTSI2
                                                                                                        for v12 in buyRSI2
                                                                                                        for v13 in sellRSI2
                                                                                                        for v14 in buyMACD2
                                                                                                        for v15 in sellMACD2
                                                                                                        for v16 in buyBB2
                                                                                                        for v17 in sellBB2
                                                                                                        for v18 in buyVolume2
                                                                                                        for v19 in sellVolume2
                                                                                                        for v20 in buyConfidence
                                                                                                        for v21 in sellConfidence
                                                                                                        for v22 in buySMIIO
                                                                                                        for v23 in sellSMIIO                                                                                    
]

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
for combo in combinations:
    rialPocket = 100000
    btcPocket = 0
    i = 0
    tradeMade = 0
    confidence = 0
    sold = False
    bought = False
    # test on our data which is n lines
    while i != len(price):
        while True:
            if bought == False and i != len(price):
                confidence = 0
                # calculating confidence
                if True:
                    if True:
                        if float(tsi[-i]) <= combo[2]:
                            confidence += 1
                        elif float(tsi[-i]) <= combo[2] + combo[10]:
                            confidence += 0.5
                    if volume[-i][0] == 'R':
                        if float(float(volume[-i][1:])/10) >= combo[8]:
                            confidence += 1
                        elif float(float(volume[-i][1:])/10) >= combo[8] - combo[18]:
                            confidence += 0.5
                    if True:
                        if float(rsi[-i]) <= combo[0]:
                            confidence += 1
                        elif float(rsi[-i]) <= combo[0] + combo[12]:
                            confidence += 0.5
                    if True:
                        if float(macd[-i]) <= combo[4]:
                            confidence += 1
                        elif float(macd[-i]) <= combo[4] + combo[14]:
                            confidence += 0.5
                    if True:
                        if float(bb[-i]) >= combo[6]:
                            confidence += 1
                        elif float(bb[-i]) >= combo[6] - combo[16]:
                            confidence += 0.5
                # looking for good situation to buy
                if (confidence >= combo[20]) and float(smiio[-i]) <= combo[22]:
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
                        if float(tsi[-i]) >= combo[3]:
                            confidence += 1
                        elif float(tsi[-i]) >= combo[3] - combo[11]:
                            confidence += 0.5
                    if volume[-i][0] == 'G':
                        if float(float(volume[-i][1:])/10) >= combo[9]:
                            confidence += 1
                        elif float(float(volume[-i][1:])/10) >= combo[9] - combo[19]:
                            confidence += 0.5
                    if True:
                        if float(rsi[-i]) >= combo[1]:
                            confidence += 1
                        elif float(rsi[-i]) >= combo[1] - combo[13]:
                            confidence += 0.5
                    if True:
                        if float(macd[-i]) >= combo[5]:
                            confidence += 1
                        elif float(macd[-i]) >= combo[5] - combo[15]:
                            confidence += 0.5
                    if True:
                        if float(bb[-i]) >= combo[7]:
                            confidence += 1
                        elif float(bb[-i]) >= combo[7] - combo[17]:
                            confidence += 0.5
                # looking for good situation to sell
                if (confidence >= combo[21]) and float(smiio[-i]) >= combo[23]:
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
        rialPocket = btcPocket * 185000000
    if rialPocket >= 283000:
        #results
        highestBalance.append(rialPocket)
        highestBalanceCombo.append(combo)
    print(f" {combo}/{combinations}", end='\r')
# finding best result
maxi = highestBalance.index(max(highestBalance))
print(
    f"{highestBalance[maxi]}, Combo={highestBalanceCombo[maxi]} !"
)
input("Press any key to exit ...")