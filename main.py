from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests
import json
from math import floor
from sys import argv, exit
from logging import basicConfig, CRITICAL, critical
import datetime
import credentials # library containing your login credentials

if argv[1] != "sell" and argv[1] != "buy" and argv[1] != "hybrid":
    print("""
    Please use 'sell' or 'buy' or 'hybrid' arguments
    Example:
    python3 main.py sell
    """)
    exit()
print(
    argv[1]
)
basicConfig(level=CRITICAL, filename='log.txt', filemode='a', format='%(message)s')
# variables
confidence = 0
rialPocket = 0
btcPocket = 0
sold = False
bought = False
Values = [44,56,-0.8,0.4,-1,7,9,8,2,1,0.5,0.3,1,8,9,3,3,4,2,2,3.5,4.0,0,0]

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
    print(
        f"{credentials.email}:{credentials.passwd} Token {authKey}"
    )

def indicator():
    driver.switch_to.frame(
        driver.find_element(
            By.XPATH,
            "/html/body/div/div/main/div/div/div/div[1]/div/div/div[1]/div/iframe",
        )
    )
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[3]/td[2]/div/div[3]/div/span[2]/a[3]').click()
    # adding RSI chart to the Trading View
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="header-toolbar-indicators"]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("RSI")
    sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    sleep(1)
    # MACD
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).clear()
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("MACD")
    sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    sleep(1)
    # TSI
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).clear()
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("TSI")
    sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    sleep(1)
    # BB
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).clear()
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("BB")
    sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    sleep(1)
    # volume
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).clear()
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("volume")
    sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    sleep(1)
    # smiio
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).clear()
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("smiio")
    sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]").click()
    sleep(1)

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
        sleep(60)
        accBalance()
        rsiValue = checkRSIValue()
        tsiValue = checkTSIValue()
        macdValue = checkMACDValue()
        bbValue = checkBBValue()
        vValue = checkVolumeValue()
        smiioValue = checkSMIIOValue()
        btcData = checkPriceValue()
        amount = int(rialPocket) / int(btcData)
    amount = floor(amount * 1000000)/1000000
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
    # Printing RealTime Stats
    print(f"Point:{confidence}/{Values[20]}, Wallet:{rialPocket} BTC={int(amount*0.9965)}, IRR:{int(btcData)}, RSI:{rsiValue}/{Values[0]}, TSI:{tsiValue}/{Values[2]}, MACD:{float(macdValue)}/{Values[4]}, BB:{float(bbValue)}/{Values[6]}, Volume:{vValue}/{Values[8]*10}, SMIIO:{smiioValue}/{Values[22]}   {datetime.datetime.now().hour}:{datetime.datetime.now().minute}")
    if (confidence >= Values[20]) and float(rialPocket) > 100000 and float(smiioValue) <= Values[22]:
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
    sleep(25)

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
        float(btcPocket)/int(btcData)
    except:
        sleep(60)
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
            if float(macdValue) >= Values[5]:
                confidence += 1
            elif float(macdValue) >= Values[5] - Values[15]:
                confidence += 0.5
        if True:
            if float(bbValue) >= Values[7]:
                confidence += 1
            elif float(bbValue) >= Values[7] - Values[17]:
                confidence += 0.5
    print(f"Point:{confidence}/{Values[21]}, Wallet:{floor(int(float(btcPocket)*int(btcData))*0.9965)} BTC={btcPocket}, IRR:{int(btcData)}, RSI:{rsiValue}/{Values[1]}, TSI:{tsiValue}/{Values[3]}, MACD:{float(macdValue)}/{Values[5]}, BB:{float(bbValue)}/{Values[7]}, Volume:{vValue}/{Values[9]*10}, SMIIO:{smiioValue}/{Values[23]}   {datetime.datetime.now().hour}:{datetime.datetime.now().minute}")
    if (confidence >= Values[21]) and float(btcPocket) > 0 and float(smiioValue) >= Values[23]:
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
    critical("{0} {1} {2} {3} {4} {5} {6} ".format(btcData,rsiValue,tsiValue,macdValue,bbValue, vValue, smiioValue))
    sleep(25)

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
authenticator(credentials.email, credentials.passwd)
try:
    indicator()
except:
    driver.close()
    exit()
sleep(5)
if argv[1] == "sell":
    while True:
        sellAction()

if argv[1] == "buy":
    while True:
        buyAction()

if argv[1] == "hybrid":
    while True:
        buyThread()
        sellThread()