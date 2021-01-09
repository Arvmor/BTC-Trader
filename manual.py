Values = [50, 50, -0.9, 0.2, -1, 9, 4, 8, 1, 0, 0.2, 0.5, 1, 5,
          2, 5, 9, 2, 2, 2, 3.5, 6.5, -0.1, 0.0, -3.0, 1.5, 50, 90]
rsiValue = input("rsiValue ") # eg: 51.11
tsiValue = input("tsiValue ") # eg: 0.66
macdValue = input("macdValue ") # eg: 645132
bbValue = input("bbValue ") # eg: 493648123
vValue = input("vValue ") # eg: G4.5
smiioValue = input("smiioValue ") # eg: -0.57
ROCValue = input("ROCValue ") # eg: 4.541
srsiValue = input("srsiValue ") # eg: 25
srsiValue2 = input("srsiValue2 ") # eg: 86
# Calculating The Confidence
confidence = 0
if True:
    if float(tsiValue) >= Values[3]:
        confidence += 1
    elif float(tsiValue) >= Values[3] - Values[11]:
        confidence += 0.5
if vValue[0] == 'G':
    if float(float(vValue[1:])/10) >= Values[9]:
        confidence += 1
    elif float(float(vValue[1:])/10) >= Values[9] - Values[19]:
        confidence += 0.5
if True:
    if float(rsiValue) >= Values[1]:
        confidence += 1
    elif float(rsiValue) >= Values[1] - Values[13]:
        confidence += 0.5
if True:
    if float(macdValue)/100000 >= Values[5]:
        confidence += 1
    elif float(macdValue)/100000 >= Values[5] - Values[15]:
        confidence += 0.5
if True:
    if float(bbValue)/1000000 >= Values[7]:
        confidence += 1
    elif float(bbValue)/1000000 >= Values[7] - Values[17]:
        confidence += 0.5
if True:
    if float(ROCValue) >= Values[25]:
        confidence += 1
if True:
    if float(srsiValue) >= Values[27]:
        confidence += 1
    elif float(srsiValue2) >= Values[27]:
        confidence += 1
printText = f"\n SELL: \nPoint:{confidence}/{Values[21]}, RSI:{rsiValue}/{Values[1]}, TSI:{tsiValue}/{Values[3]}, MACD:{float(macdValue)}/{Values[5]}, BB:{float(bbValue)}/{Values[7]}, Volume:{vValue}/{Values[9]*10}, SMIIO:{smiioValue}/{Values[23]}, ROC:{ROCValue}/{Values[25]}, SRSI:{srsiValue} {srsiValue2}/{Values[27]}"
print(printText)

if (confidence >= Values[21]) and float(smiioValue) >= Values[23]:
    print("sell")

# Calculating The Confidence
confidence = 0
if True:
    if float(tsiValue) <= Values[2]:
        confidence += 1
    elif float(tsiValue) <= Values[2] + Values[10]:
        confidence += 0.5
if vValue[0] == 'R':
    if float(float(vValue[1:])/10) >= Values[8]:
        confidence += 1
    elif float(float(vValue[1:])/10) >= Values[8] - Values[18]:
        confidence += 0.5
if True:
    if (float(rsiValue) <= Values[0] and float(rsiValue) >= 10):
        confidence += 1
    elif (float(rsiValue) <= Values[0] + Values[12] and float(rsiValue) >= 10):
        confidence += 0.5
if True:
    if float(macdValue)/100000 <= Values[4]:
        confidence += 1
    elif float(macdValue)/100000 <= Values[4] + Values[14]:
        confidence += 0.5
if True:
    if float(bbValue)/1000000 >= Values[6]:
        confidence += 1
    elif float(bbValue)/1000000 >= Values[6] - Values[16]:
        confidence += 0.5
if True:
    if float(ROCValue) <= Values[24]:
        confidence += 1
if True:
    if float(srsiValue) <= Values[26]:
        confidence += 1
    elif float(srsiValue2) <= Values[26]:
        confidence += 1
# Printing RealTime Stats
printText = f"\n BUY: \nPoint:{confidence}/{Values[20]}, RSI:{rsiValue}/{Values[0]}, TSI:{tsiValue}/{Values[2]}, MACD:{float(macdValue)}/{Values[4]}, BB:{float(bbValue)}/{Values[6]}, Volume:{vValue}/{Values[8]*10}, SMIIO:{smiioValue}/{Values[22]}, ROC:{ROCValue}/{Values[24]}, SRSI:{srsiValue} {srsiValue2}/{Values[26]}"
print(printText)
if (confidence >= Values[20]) and float(smiioValue) <= Values[22]:
    print("buy")