from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui

# variables
rsival = []
macdval = []
usdtval = []


def MACD():
    # adding RSI chart to the Trading View
    time.sleep(2)
    driver.find_element(
        By.XPATH, '//*[@id="header-toolbar-indicators"]').click()
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
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[3]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text.encode("utf-8")
    RSIvalue = float((RSIvalue.decode("utf-8"))[1:5])
    return RSIvalue


def checkPriceValue():
    # getting RSI current value
    Pricevalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[1]/td[2]/div/div[3]/div/div/span[4]/span[2]",
    ).text.encode("utf-8")
    Pricevalue = int((Pricevalue.decode("utf-8"))[1:5])*10
    return Pricevalue


# def checkMACDValue():
#     # getting RSI current value
#     RSIvalue = driver.find_element(
#         By.XPATH,
#         "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[5]/td[2]/div/div[3]/div/div/span[1]/span",
#     ).text.encode("utf-8")
#     RSIvalue = float((RSIvalue.decode("utf-8"))[1:5])
#     print(RSIvalue)
#     return RSIvalue


def getDatas(days):
    for day in range(days):
        pyautogui.press('left')
        time.sleep(0.3)
        usdtval.append(checkPriceValue())
        rsival.append(checkRSIValue())


# Driver settings
chromedriver = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome("chromedriver", options=chrome_options)
driver.get("https://nobitex.ir/app/exchange/usdt-rls/")
time.sleep(15)

# run functions
RSI()
MACD()
time.sleep(5)
getDatas(2000)

with open('datasetRSIval.txt', '+w') as filehandle:
    for rval in rsival:
        filehandle.write('%s\n' % rval)

with open('datasetPrice.txt', '+w') as fhandle:
    for usv in usdtval:
        fhandle.write('%s\n' % usv)
