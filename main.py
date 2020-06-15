from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import json
import math

# variables
confident = 0
rialPocket = 0
usdtPocket = 0
sold = False
bought = False

# functions
def accBalance():
    global rialPocket, usdtPocket
    # getting AUTH Key
    url = "https://api.nobitex.ir/users/wallets/balance"
    payload = {"currency": "usdt"}
    headers = {"Authorization": "Token " + authKey}
    response = requests.request("POST", url, headers=headers, data=payload).text.encode(
        "utf8"
    )
    usdtPocket = json.loads(response.decode("utf-8"))["balance"]
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
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]").click()
    time.sleep(1)

def checkPriceValue():
    #getting Price value
    Pricevalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[1]/td[2]/div/div[3]/div/div/span[4]/span[2]",
    ).text.encode("utf-8")
    Pricevalue = int((Pricevalue.decode("utf-8"))[1:6])
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
    RSIvalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[7]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text.encode("utf-8")
    if RSIvalue.decode("utf-8")[1] == "\u2212":
        RSIvalue = float((RSIvalue.decode("utf-8"))[2:-4]) * -1
    else:
        RSIvalue = float((RSIvalue.decode("utf-8"))[1:-4])
    return RSIvalue

def buyAction(b1v, b2v, b3v, b4v):
    global bought, rialPocket, usdtPocket, confident
    try:
        accBalance()
        rsiValue = checkRSIValue()
        tsiValue = checkTSIValue()
        macdValue = checkMACDValue()
        bbValue = checkBBValue()
        usdtData = checkPriceValue()
    except:
        time.sleep(60)
        accBalance()
        rsiValue = checkRSIValue()
        tsiValue = checkTSIValue()
        macdValue = checkMACDValue()
        bbValue = checkBBValue()
        usdtData = checkPriceValue()
    amount = int(rialPocket) / int(usdtData)
    amount = math.floor(amount * 100)/100.0
    # Calculating The Confidence
    confident = 0
    if True:
        if True:
            if float(tsiValue) <= b2v:
                confident += 1
            elif float(tsiValue) <= b2v + 0.2:
                confident += 0.5
        if True:
            if (float(rsiValue) <= b1v and float(rsiValue) >= 20):
                confident += 1
            elif (float(rsiValue) <= b1v + 5 and float(rsiValue) >= 20):
                confident += 0.5
        if True:
            if int(macdValue)/10 >= b3v:
                confident += 1
            elif int(macdValue)/10 >= b3v + 9:
                confident += 0.5
        if True:
            if float(int(bbValue)/100) >= b4v:
                confident += 1
            elif float(int(bbValue)/100) >= b4v + 2:
                confident += 0.5
    # Printing RealTime Stats
    print(f"Balance:{rialPocket} usdt={amount}, usd:{int(usdtData)}, RSI:{rsiValue}, TSI:{tsiValue}, MACD:{macdValue}, BB:{bbValue}")
    if (confident >= 3):
        # Buy Req
        url = "https://api.nobitex.ir/market/orders/add"
        payload = {
            "type": "buy",
            "execution": "limit",
            "srcCurrency": "usdt",
            "dstCurrency": "rls",
            "amount": float(amount),
            "price": int(usdtData)
        }
        headers = {"Authorization": "Token " + authKey}
        response = requests.request(
            "POST", url, headers=headers, data=payload
        ).text.encode("utf8")
        print(response.decode("utf8"))
        print(f"Bought !")
        bought = True
    time.sleep(60)

def sellAction(s1v, s2v, s3v, s4v):
    global sold, rialPocket, usdtPocket, confident
    try:
        accBalance()
        rsiValue = checkRSIValue()
        tsiValue = checkTSIValue()
        macdValue = checkMACDValue()
        bbValue = checkBBValue()
        usdtData = checkPriceValue()
    except:
        time.sleep(60)
        accBalance()
        rsiValue = checkRSIValue()
        tsiValue = checkTSIValue()
        macdValue = checkMACDValue()
        bbValue = checkBBValue()
        usdtData = checkPriceValue()
    # Calculating The Confidence
    confident = 0
    if True:
        if True:
            if float(tsiValue) >= s2v:
                confident += 1
            elif float(tsiValue) >= s2v - 0.3:
                confident += 0.5
        if True:
            if float(rsiValue) >= s1v:
                confident += 1
            elif float(rsiValue) >= s1v - 9:
                confident += 0.5
        if True:
            if int(macdValue)/10 >= s3v:
                confident += 1
            elif int(macdValue)/10 >= s3v - 5:
                confident += 0.5
        if True:
            if float(int(bbValue)/100) >= s4v:
                confident += 1
            elif float(int(bbValue)/100) >= s4v - 8:
                confident += 0.5
    print(f"Balance:{rialPocket}, usd:{int(usdtData)}, RSI:{rsiValue}, TSI:{tsiValue}, MACD:{macdValue}, BB:{bbValue}")
    if (confident >= 3.5):
        url = "https://api.nobitex.ir/market/orders/add"
        payload = {
            "type": "sell",
            "execution": "limit",
            "srcCurrency": "usdt",
            "dstCurrency": "rls",
            "amount": float(usdtPocket),
            "price": int(usdtData)
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
    global bought, confident
    while True:
        if bought == False:
            buyAction(31, -0.0, 7, 2)
        else:
            confident = 0
            bought = False
            break

def sellThread():
    global sold, confident
    while True:
        if sold == False:
            sellAction(70, 0.3, 8, 7)
        else:
            confident = 0
            sold = False
            break

# Driver settings
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--log-level=OFF")
driver = webdriver.Chrome("chromedriver", options=chrome_options)
driver.get("https://nobitex.ir/app/exchange/usdt-rls/")

# main launch
authenticator("email", "passwd")
indicator()
time.sleep(5)
while True:
    buyThread()
    sellThread()
driver.close()
