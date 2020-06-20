from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import json
import math
import datetime

# variables
confidence = 0
rialPocket = 0
btcPocket = 0
sold = False
bought = False
Values = [44,56,-0.8,0.2,2,7,6,8,3,2,0.5,0.0,0,7,8,1,0,5,2,4,3.0,4.0]

# functions
def accBalance():
    global rialPocket, btcPocket
    # getting account Money Balance
    url = "https://api.nobitex.ir/users/wallets/balance"
    payload = {"currency": "btc"}
    headers = {"Authorization": "Token " + authKey}
    response = requests.request("POST", url, headers=headers, data=payload).text.encode(
        "utf8"
    )
    btcPocket = json.loads(response.decode("utf-8"))["balance"]
    payload = {"currency": "rls"}
    response = requests.request("POST", url, headers=headers, data=payload).text.encode(
        "utf8"
    )
    rialPocket = json.loads(response.decode("utf-8"))["balance"]
    lenCh = 0
    rpocket = ''
    while lenCh <= int(len(rialPocket)) and str(rialPocket)[lenCh] != '.':
        rpocket += str(rialPocket)[lenCh]
        lenCh += 1
    rialPocket = int(rpocket)

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

def indicator():
    driver.switch_to.frame(
        driver.find_element(
            By.XPATH,
            "/html/body/div/div/main/div/div/div/div[1]/div/div/div[1]/div/iframe",
        )
    )
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[3]/td[2]/div/div[3]/div/span[2]/a[3]').click()
    # adding RSI chart to the Trading View
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="header-toolbar-indicators"]').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("RSI")
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    time.sleep(1)
    # MACD
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).clear()
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("MACD")
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    time.sleep(1)
    # TSI
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).clear()
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("TSI")
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    time.sleep(1)
    # BB
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).clear()
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("BB")
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    time.sleep(1)
    # volume
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).clear()
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("volume")
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    time.sleep(1)
    # smiio
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).clear()
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("smiio")
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]").click()
    time.sleep(1)

def checkPriceValue():
    #getting Price value
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
        MACDvalue = int((MACDvalue.decode("utf-8"))[2:-6])
    else:
        MACDvalue = int((MACDvalue.decode("utf-8"))[1:-6])
    return abs(MACDvalue)

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
    return BBvalue2 - BBvalue

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
        SMIIOvalue = float((SMIIOvalue.decode("utf-8"))[2:-5]) * -1
    else:
        SMIIOvalue = float((SMIIOvalue.decode("utf-8"))[1:-5])
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

def buyAction():
    global bought, rialPocket, btcPocket, confidence, Values
    try:
        accBalance()
        rsiValue = checkRSIValue()
        tsiValue = checkTSIValue()
        macdValue = checkMACDValue()
        bbValue = checkBBValue()
        vValue = checkVolumeValue()
        smiioValue = checkSMIIOValue()
        btcData = checkPriceValue()
        amount = int(rialPocket) / int(btcData)
    except:
        # if failed
        time.sleep(60)
        accBalance()
        rsiValue = checkRSIValue()
        tsiValue = checkTSIValue()
        macdValue = checkMACDValue()
        bbValue = checkBBValue()
        vValue = checkVolumeValue()
        smiioValue = checkSMIIOValue()
        btcData = checkPriceValue()
        amount = int(rialPocket) / int(btcData)
    amount = math.floor(amount * 1000000)/1000000
    # Calculating The Confidence
    confidence = 0
    if True:
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
            if (float(rsiValue) <= Values[0] and float(rsiValue) >= 20):
                confidence += 1
            elif (float(rsiValue) <= Values[0] + Values[12] and float(rsiValue) >= 20):
                confidence += 0.5
        if True:
            if int(macdValue)/100000 >= Values[4]:
                confidence += 1
            elif int(macdValue)/100000 >= Values[4] + Values[14]:
                confidence += 0.5
        if True:
            if float(int(bbValue)/1000000) >= Values[6]:
                confidence += 1
            elif float(int(bbValue)/1000000) >= Values[6] + Values[16]:
                confidence += 0.5
    # Printing RealTime Stats
    print(f"Point:{confidence}/{Values[20]}, Wallet:{rialPocket} BTC={amount}, IRR:{int(btcData)}, RSI:{rsiValue}/{Values[0]}, TSI:{tsiValue}/{Values[2]}, MACD:{int(macdValue)/100000}/{Values[4]}, BB:{int(bbValue)/1000000}/{Values[6]}, Volume:{vValue}/{Values[8]}, SMIIO:{smiioValue}   {datetime.datetime.now().hour}:{datetime.datetime.now().minute}")
    if (confidence >= Values[20]):
        # Buy Req
        url = "https://api.nobitex.ir/market/orders/add"
        payload = {
            "type": "buy",
            "execution": "limit",
            "srcCurrency": "btc",
            "dstCurrency": "rls",
            "amount": float(amount),
            "price": int(btcData)
        }
        headers = {"Authorization": "Token " + authKey}
        response = requests.request(
            "POST", url, headers=headers, data=payload
        ).text.encode("utf8")
        print(response.decode("utf8"))
        print(f"Bought !")
        bought = True
    time.sleep(60)

def sellAction():
    global sold, rialPocket, btcPocket, confidence, Values
    try:
        accBalance()
        rsiValue = checkRSIValue()
        tsiValue = checkTSIValue()
        macdValue = checkMACDValue()
        bbValue = checkBBValue()
        vValue = checkVolumeValue()
        smiioValue = checkSMIIOValue()
        btcData = checkPriceValue()
        if int(btcData) == 0:
            btcData = checkPriceValue()
    except:
        time.sleep(60)
        accBalance()
        rsiValue = checkRSIValue()
        tsiValue = checkTSIValue()
        macdValue = checkMACDValue()
        bbValue = checkBBValue()
        vValue = checkVolumeValue()
        smiioValue = checkSMIIOValue()
        btcData = checkPriceValue()
    # Calculating The Confidence
    confidence = 0
    if True:
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
            if int(macdValue)/100000 >= Values[5]:
                confidence += 1
            elif int(macdValue)/100000 >= Values[5] - Values[15]:
                confidence += 0.5
        if True:
            if float(int(bbValue)/1000000) >= Values[7]:
                confidence += 1
            elif float(int(bbValue)/1000000) >= Values[7] - Values[17]:
                confidence += 0.5
    print(f"Point:{confidence}/{Values[21]}, Wallet:{int(float(btcPocket)*int(btcData))} BTC={btcPocket}, IRR:{int(btcData)}, RSI:{rsiValue}/{Values[1]}, TSI:{tsiValue}/{Values[3]}, MACD:{int(macdValue)/100000}/{Values[5]}, BB:{int(bbValue)/1000000}/{Values[7]}, Volume:{vValue}/{Values[9]}, SMIIO:{smiioValue}   {datetime.datetime.now().hour}:{datetime.datetime.now().minute}")
    if (confidence >= Values[21]):
        url = "https://api.nobitex.ir/market/orders/add"
        payload = {
            "type": "sell",
            "execution": "limit",
            "srcCurrency": "btc",
            "dstCurrency": "rls",
            "amount": float(btcPocket),
            "price": int(btcData)
        }
        headers = {"Authorization": "Token " + authKey}
        response = requests.request(
            "POST", url, headers=headers, data=payload
        ).text.encode("utf8")
        print(response.decode("utf8"))
        print(f"Sold !")
        sold = True
    time.sleep(60)

def buyThread():
    global bought, confidence
    while True:
        if bought == False:
            buyAction()
        else:
            confidence = 0
            bought = False
            break

def sellThread():
    global sold, confidence
    while True:
        if sold == False:
            sellAction()
        else:
            confidence = 0
            sold = False
            break

# Driver settings
chromedriver = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--log-level=OFF")
driver = webdriver.Chrome("chromedriver", options=chrome_options)
driver.get("https://nobitex.ir/app/exchange/btc-rls/")

# main launch
authenticator("email", "passwd")
indicator()
time.sleep(5)
while True:
    buyThread()
    sellThread()
driver.close()
