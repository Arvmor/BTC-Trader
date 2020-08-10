#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests
import json
from os import system
from math import floor
from sys import argv, exit
from signal import signal, SIGINT
from logging import basicConfig, CRITICAL, critical
import datetime
import credentials  # library containing your login credentials

if argv[1] != "sell" and argv[1] != "buy" and argv[1] != "normal":
    print("""
    Please use 'sell' or 'buy' or 'normal' arguments
    Example:
    python3 main.py sell
    """)
    exit()
print(argv[1])
basicConfig(level=CRITICAL, filename='log.txt',
            filemode='a', format='%(message)s')
# variables
confidence = 0
usdtPocket = 0
btcPocket = 0
printText = ''
sold = False
bought = False
Values = [50, 50, -0.9, 0.2, -1, 9, 4, 8, 1, 0, 0.2, 0.5, 1, 5,
          2, 5, 9, 2, 2, 2, 3.5, 6.5, -0.1, 0.0, -3.0, 1.5, 50, 90]
# functions


def writeFile(orderType, variableName, mode, log):
    with open(f"/var/www/html/{orderType}Text.php", mode) as fileHandle:
        if log == 1:
            for d in variableName:
                fileHandle.write("%s\n" % d)
        else:
            for d in variableName:
                fileHandle.write("%s" % d)


def signal_handler(signal, frame):
    driver.quit()
    exit(0)


def accBalance():
    global usdtPocket, btcPocket
    # getting account Money Balance
    url = "https://api.nobitex.ir/users/wallets/balance"
    payload = {"currency": "btc"}
    headers = {"Authorization": "Token " + authKey}
    response = requests.request("POST", url, headers=headers, data=payload).text.encode(
        "utf8"
    )
    btcPocket = json.loads(response.decode("utf-8"))["balance"]
    payload = {"currency": "usdt"}
    response = requests.request("POST", url, headers=headers, data=payload).text.encode(
        "utf8"
    )
    usdtPocket = json.loads(response.decode("utf-8"))["balance"]


def authenticator(email, password):
    # getting AUTH Key
    url = "https://api.nobitex.ir/auth/login/"
    payload = {"username": email, "password": password, "remember": "yes"}
    files = []
    headers = {}

    response = (
        requests.request("POST", url, headers=headers,
                         data=payload, files=files)
    ).text.encode("utf8")
    global authKey
    authKey = json.loads(response.decode("utf-8"))["key"]
    # print(
    #     f"{credentials.email}:{credentials.passwd} Token {authKey}"
    # )


def indicator(indicators):
    driver.switch_to.frame(
        driver.find_element(
            By.XPATH,
            "/html/body/div/div/main/div/div/div/div[1]/div/div/div[1]/div/iframe",
        )
    )
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[3]/td[2]/div/div[3]/div/span[2]/a[3]').click()
    sleep(2)
    driver.find_element(
        By.XPATH, '//*[@id="header-toolbar-indicators"]').click()
    sleep(2)
    # adding indicators
    for i in indicators:
        driver.find_element(
            By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
        ).clear()
        driver.find_element(
            By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
        ).send_keys(i)
        sleep(0.2)
        driver.find_element(
            By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
        ).click()
        sleep(0.2)
    # close Tab
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]").click()
    sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]").click()


def checkPriceValue():
    # getting Price value
    Pricevalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[1]/td[2]/div/div[3]/div/div/span[4]/span[2]",
    ).text.encode("utf-8")
    Pricevalue = int((Pricevalue.decode("utf-8"))[1:-1])
    return Pricevalue*10


def checkRSIValue():
    # getting RSI value
    RSIvalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[3]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text.encode("utf-8")
    RSIvalue = float((RSIvalue.decode("utf-8"))[1:5])
    return RSIvalue


def checkMACDValue():
    # getting MACD value
    MACDvalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[5]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text.encode("utf-8")
    if MACDvalue.decode("utf-8")[1] == "\u2212":
        MACDvalue = int((MACDvalue.decode("utf-8"))[2:-6]) / -100000
    else:
        MACDvalue = int((MACDvalue.decode("utf-8"))[1:-6]) / 100000
    return MACDvalue


def checkBBValue():
    # getting BB value
    BBvalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[1]/td[2]/div/div[3]/div[2]/div/span[3]/span",
    ).text.encode("utf-8")
    BBvalue2 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[1]/td[2]/div/div[3]/div[2]/div/span[2]/span",
    ).text.encode("utf-8")
    BBvalue = int((BBvalue.decode("utf-8"))[1:-6])
    BBvalue2 = int((BBvalue2.decode("utf-8"))[1:-6])
    return (BBvalue2 - BBvalue)/1000000


def checkTSIValue():
    # getting TSI value
    TSIvalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[7]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text.encode("utf-8")
    if TSIvalue.decode("utf-8")[1] == "\u2212":
        TSIvalue = float((TSIvalue.decode("utf-8"))[2:-4]) * -1
    else:
        TSIvalue = float((TSIvalue.decode("utf-8"))[1:-4])
    return TSIvalue


def checkSMIIOValue():
    # getting SMIIO value
    SMIIOvalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[11]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text.encode("utf-8")
    if SMIIOvalue.decode("utf-8")[1] == "\u2212":
        SMIIOvalue = float((SMIIOvalue.decode("utf-8"))[2:-3]) * -1
    else:
        SMIIOvalue = float((SMIIOvalue.decode("utf-8"))[1:-3])
    return SMIIOvalue


def checkVolumeValue():
    # getting TSI value
    Volumevalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[9]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text
    rgb = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[9]/td[2]/div/div[3]/div/div/span[1]/span",
    ).get_attribute("style")
    if rgb[11] == '8':
        Volumevalue = 'G'+str(Volumevalue)
    else:
        Volumevalue = 'R'+str(Volumevalue)
    return Volumevalue


def checkROCValue():
    # getting TSI value
    ROCvalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[13]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text.encode("utf-8")
    if ROCvalue.decode("utf-8")[1] == "\u2212":
        ROCvalue = float((ROCvalue.decode("utf-8"))[2:-2])
    else:
        ROCvalue = float((ROCvalue.decode("utf-8"))[1:-2])
    return ROCvalue


def checkStochRSIValue():
    # getting TSI value
    StochRSI = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[15]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text.encode("utf-8")
    StochRSI2 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[15]/td[2]/div/div[3]/div/div/span[2]/span",
    ).text.encode("utf-8")
    if StochRSI.decode("utf-8")[1] == "\u2212":
        StochRSI = int((StochRSI.decode("utf-8"))[2:-6])
    else:
        StochRSI = int((StochRSI.decode("utf-8"))[1:-6])
    if StochRSI2.decode("utf-8")[1] == "\u2212":
        StochRSI2 = int((StochRSI2.decode("utf-8"))[2:-6])
    else:
        StochRSI2 = int((StochRSI2.decode("utf-8"))[1:-6])
    return StochRSI, StochRSI2


def buyAction():
    global bought, usdtPocket, btcPocket, confidence, Values
    try:
        accBalance()
    except:
        authenticator(credentials.email, credentials.passwd)
        sleep(15)
        accBalance()
    try:
        rsiValue = checkRSIValue()
        tsiValue = checkTSIValue()
        macdValue = checkMACDValue()
        bbValue = checkBBValue()
        vValue = checkVolumeValue()
        smiioValue = checkSMIIOValue()
        btcData = checkPriceValue()
        ROCValue = checkROCValue()
        srsiValue = checkStochRSIValue()[0]
        srsiValue2 = checkStochRSIValue()[1]
        amount = int(usdtPocket) / int(btcData)
    except:
        # if failed
        sleep(15)
        rsiValue = checkRSIValue()
        tsiValue = checkTSIValue()
        macdValue = checkMACDValue()
        bbValue = checkBBValue()
        vValue = checkVolumeValue()
        smiioValue = checkSMIIOValue()
        btcData = checkPriceValue()
        ROCValue = checkROCValue()
        srsiValue = checkStochRSIValue()[0]
        srsiValue2 = checkStochRSIValue()[1]
        amount = int(usdtPocket) / int(btcData)
    amount = floor(amount * 1000000)/1000000
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
        if float(macdValue) <= Values[4]:
            confidence += 1
        elif float(macdValue) <= Values[4] + Values[14]:
            confidence += 0.5
    if True:
        if float(bbValue) >= Values[6]:
            confidence += 1
        elif float(bbValue) >= Values[6] - Values[16]:
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
    printText = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}, Point:{confidence}/{Values[20]}, BTC:{float(amount*0.9965)}, IRR:{int(btcData)}, RSI:{rsiValue}/{Values[0]}, TSI:{tsiValue}/{Values[2]}, MACD:{float(macdValue)}/{Values[4]}, BB:{float(bbValue)}/{Values[6]}, Volume:{vValue}/{Values[8]*10}, SMIIO:{smiioValue}/{Values[22]}, ROC:{ROCValue}/{Values[24]}, SRSI:{srsiValue} {srsiValue2}/{Values[26]}"
    print(printText)
    if (confidence >= Values[20]) and float(usdtPocket) > 100000 and float(smiioValue) <= Values[22]:
        # Buy Req
        url = "https://api.nobitex.ir/market/orders/add"
        payload = {
            "type": "buy",
            "execution": "limit",
            "srcCurrency": "btc",
            "dstCurrency": "usdt",
            "amount": float(amount),
            "price": int(btcData)
        }
        headers = {"Authorization": "Token " + authKey}
        response = requests.request(
            "POST", url, headers=headers, data=payload
        ).text.encode("utf8")
        print(response.decode("utf8"))
        bought = True
    writeFile("buy", printText.split(', '), "+w", 1)
    sleep(10)


def sellAction():
    global sold, usdtPocket, btcPocket, confidence, Values, printText
    try:
        accBalance()
    except:
        authenticator(credentials.email, credentials.passwd)
        sleep(15)
        accBalance()
    try:
        rsiValue = checkRSIValue()
        tsiValue = checkTSIValue()
        macdValue = checkMACDValue()
        bbValue = checkBBValue()
        vValue = checkVolumeValue()
        smiioValue = checkSMIIOValue()
        btcData = checkPriceValue()
        ROCValue = checkROCValue()
        srsiValue = checkStochRSIValue()[0]
        srsiValue2 = checkStochRSIValue()[1]
        if int(btcData) == 0:
            btcData = checkPriceValue()
        float(btcPocket)/int(btcData)
    except:
        sleep(15)
        rsiValue = checkRSIValue()
        tsiValue = checkTSIValue()
        macdValue = checkMACDValue()
        bbValue = checkBBValue()
        vValue = checkVolumeValue()
        smiioValue = checkSMIIOValue()
        btcData = checkPriceValue()
        ROCValue = checkROCValue()
        srsiValue = checkStochRSIValue()[0]
        srsiValue2 = checkStochRSIValue()[1]
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
        if float(macdValue) >= Values[5]:
            confidence += 1
        elif float(macdValue) >= Values[5] - Values[15]:
            confidence += 0.5
    if True:
        if float(bbValue) >= Values[7]:
            confidence += 1
        elif float(bbValue) >= Values[7] - Values[17]:
            confidence += 0.5
    if True:
        if float(ROCValue) >= Values[25]:
            confidence += 1
    if True:
        if float(srsiValue) >= Values[27]:
            confidence += 1
        elif float(srsiValue2) >= Values[27]:
            confidence += 1
    printText = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}, Point:{confidence}/{Values[21]}, Wallet:{floor(int(float(btcPocket)*int(btcData))*0.9965)}, IRR:{int(btcData)}, RSI:{rsiValue}/{Values[1]}, TSI:{tsiValue}/{Values[3]}, MACD:{float(macdValue)}/{Values[5]}, BB:{float(bbValue)}/{Values[7]}, Volume:{vValue}/{Values[9]*10}, SMIIO:{smiioValue}/{Values[23]}, ROC:{ROCValue}/{Values[25]}, SRSI:{srsiValue} {srsiValue2}/{Values[27]}"
    print(printText)
    if (confidence >= Values[21]) and float(btcPocket) > 0 and float(smiioValue) >= Values[23]:
        url = "https://api.nobitex.ir/market/orders/add"
        payload = {
            "type": "sell",
            "execution": "limit",
            "srcCurrency": "btc",
            "dstCurrency": "usdt",
            "amount": float(btcPocket),
            "price": int(btcData)
        }
        headers = {"Authorization": "Token " + authKey}
        response = requests.request(
            "POST", url, headers=headers, data=payload
        ).text.encode("utf8")
        print(response.decode("utf8"))
        sold = True
    critical("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} ".format(btcData, rsiValue,
                                                               tsiValue, macdValue, bbValue, vValue, smiioValue, ROCValue, srsiValue, srsiValue2))
    writeFile("sell", printText.split(', '), "+w", 1)
    writeFile("btc", str(btcPocket), "+w", 0)
    writeFile("usdt", str(usdtPocket), "+w", 0)
    sleep(10)


# Driver settings
chromedriver = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--log-level=OFF")
driver = webdriver.Chrome("chromedriver", options=chrome_options)
driver.get("https://nobitex.ir/app/exchange/btc-usdt/")

# main launch
signal(SIGINT, signal_handler)
try:
    indicator(['RSI', 'MACD', 'TSI', 'BB', 'volume',
               'SMIIO', 'ROC', 'Stoch RSI', 'PVT'])
except:
    driver.quit()
    exit()

authenticator(credentials.email, credentials.passwd)
sleep(5)
if argv[1] == "sell":
    while True:
        try:
            sellAction()
        except:
            sleep(10)

if argv[1] == "buy":
    system('sudo service apache2 start')
    while True:
        try:
            buyAction()
        except:
            sleep(10)

if argv[1] == "normal":
    system('sudo service apache2 start')
    while True:
        while True:
            if bought == False:
                buyAction()
            else:
                confidence = 0
                bought = False
                break
        while True:
            if sold == False:
                sellAction()
            else:
                confidence = 0
                sold = False
                break
