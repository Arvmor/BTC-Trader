from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import threading
import time
import requests
import os
import json

# variables
rialPocket = 0
usdtPocket = 0
sold = False
bought = False
situation = ""

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

def getPrice():
    # getting USDT stats
    url = "https://api.nobitex.ir/market/stats"
    payload = {"srcCurrency": "usdt", "dstCurrency": "rls"}
    headers = {}
    response = (
        requests.request("POST", url, headers=headers, data=payload)
    ).text.encode("utf8")
    return json.loads(response.decode("utf-8"))["stats"]["usdt-rls"]

def MACD():
    # adding MACD chart to the Trading View
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="header-toolbar-indicators"]').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("MACD")
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]").click()
    time.sleep(1)

def TSI():
    # adding TSI chart to the Trading View
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="header-toolbar-indicators"]').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("TSI")
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]").click()
    time.sleep(1)

def BB():
    # adding BBS chart to the Trading View
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="header-toolbar-indicators"]').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("bb")
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]").click()
    time.sleep(1)

def RSI():
    # adding RSI chart to the Trading View
    driver.switch_to.frame(
        driver.find_element(
            By.XPATH,
            "/html/body/div/div/main/div/div/div/div[1]/div/div/div[1]/div/iframe",
        )
    )
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
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]").click()
    time.sleep(1)

def checkRSIValue():
    # getting RSI value
    RSIvalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[3]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text.encode("utf-8")
    RSIvalue = float((RSIvalue.decode("utf-8"))[1:5])
    return RSIvalue

# def checkPriceValue():
    # getting Price value
    # Pricevalue = driver.find_element(
    #     By.XPATH,
    #     "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[1]/td[2]/div/div[3]/div/div/span[4]/span[2]",
    # ).text.encode("utf-8")
    # Pricevalue = int((Pricevalue.decode("utf-8"))[1:5]) * 10
    # return Pricevalue

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
    global bought, rialPocket, usdtPocket
    accBalance()
    rsiValue = checkRSIValue()
    tsiValue = checkTSIValue()
    macdValue = checkMACDValue()
    bbValue = checkBBValue()
    usdtData = getPrice()
    print(f"usd:{usdtData["latest"]}, RSI:{rsiValue}, TSI:{tsiValue}, MACD:{macdValue}, BB:{bbValue}")
    if (float(rsiValue) <= b1v and float(tsiValue) <= b2v and int(macdValue)/10 >= b3v and float(int(bbValue)/100) >= b4v):
        url = "https://api.nobitex.ir/market/orders/add"
        payload = {
            "type": "buy",
            "execution": "limit",
            "srcCurrency": "usdt",
            "dstCurrency": "rls",
            "amount": float(rialPocket) // float(usdtData["latest"]),
            "price": float(usdtData["latest"])
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
    global sold, rialPocket, usdtPocket
    accBalance()
    rsiValue = checkRSIValue()
    tsiValue = checkTSIValue()
    macdValue = checkMACDValue()
    bbValue = checkBBValue()
    usdtData = getPrice()
    print(f"usd:{usdtData["latest"]}, RSI:{rsiValue}, TSI:{tsiValue}, MACD:{macdValue}, BB:{bbValue}")
    if (float(rsiValue) >= s1v and float(tsiValue) >= s2v and int(macdValue)/10 >= s3v and float(int(bbValue)/100) >= s4v):
        url = "https://api.nobitex.ir/market/orders/add"
        payload = {
            "type": "sell",
            "execution": "limit",
            "srcCurrency": "usdt",
            "dstCurrency": "rls",
            "amount": usdtPocket,
            "price": float(usdtData["latest"])
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
    global bought
    while True:
        if bought == False:
            buyAction(47, -0.1, 7, 6)
        else:
            bought = False
            break

def sellThread():
    global sold
    while True:
        if sold == False:
            sellAction(70, 0.6, 8, 6)
        else:
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
driver.get("https://nobitex.ir/app/exchange/usdt-rls/")

# main launch
authenticator(email, password)
RSI()
MACD()
TSI()
BB()
time.sleep(5)
while True:
    buyThread()
    sellThread()
driver.close()