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


def RSI():
    # adding RSI chart to the Trading View
    driver.switch_to.frame(
        driver.find_element(
            By.XPATH,
            "/html/body/div/div/main/div/div/div/div[1]/div/div/div[1]/div/iframe",
        )
    )
    time.sleep(2)
    driver.find_element(
        By.XPATH, '//*[@id="header-toolbar-indicators"]').click()
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
    # getting RSI current value
    RSIvalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[5]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text.encode("utf-8")
    RSIvalue = float((RSIvalue.decode("utf-8"))[1:5])
    print(RSIvalue)
    return RSIvalue


def buyAction(downValue):
    global bought, rialPocket, usdtPocket
    accBalance()
    buy = checkRSIValue()
    usdtData = getPrice()
    print(float(usdtData["latest"]) / 10)
    if buy <= downValue and buy >= 20:
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


def sellAction(upValue):
    global sold, situation, rialPocket, usdtPocket
    accBalance()
    sell = checkRSIValue()
    usdtData = getPrice()
    print(float(usdtData["latest"]) / 10)
    if sell >= upValue:
        if int(usdtData["bestBuy"]) <= 17001:
            situation = "BAD"
            return
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


def sellThread():
    global sold
    while True:
        if sold == False:
            sellAction(57.5)
        else:
            sold = False
            break


def buyThread():
    global bought
    while True:
        if bought == False:
            buyAction(35.5)
        else:
            bought = False
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
while True:
    buyThread()
    sellThread()
driver.close()
