#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from pyautogui import press

# variables
rsiValue = []
macdValue = []
tsiValue = []
btcValue = []
bbValue = []
vValue = []
rocValue = []
srsiValue = []
srsiValue2 = []
smiioValue = []
fractalsValue = []
pvtValue = []
i = 0  # day counter


def writeFile(filePath, variableName):  # save data into file
    with open("./"+filePath, "+w") as fileHandle:
        for d in variableName:
            fileHandle.write("%s\n" % d)


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


def checkRSIValue():
    # getting RSI value
    RSIvalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[3]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text.encode("utf-8")
    RSIvalue = float((RSIvalue.decode("utf-8"))[1:5])
    return RSIvalue


def checkPriceValue():
    # getting Price value
    Pricevalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[1]/td[2]/div/div[3]/div/div/span[4]/span[2]",
    ).text.encode("utf-8")
    Pricevalue = int((Pricevalue.decode("utf-8"))[1:-1])
    return Pricevalue


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


def checkSMIIOValue():
    # getting TSI value
    SMIIOvalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[11]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text.encode("utf-8")
    if SMIIOvalue.decode("utf-8")[1] == "\u2212":
        SMIIOvalue = float((SMIIOvalue.decode("utf-8"))[2:-3]) * -1
    else:
        SMIIOvalue = float((SMIIOvalue.decode("utf-8"))[1:-3])
    return SMIIOvalue


def checkFractalsValue():
    # getting Fractals value
    FractalsValueBuy = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[1]/td[2]/div/div[3]/div[3]/div/span[2]/span",
    ).text.encode("utf-8")
    FractalsValueBuy = int((FractalsValueBuy.decode("utf-8"))[1:-6])
    FractalsValueSell = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[1]/td[2]/div/div[3]/div[3]/div/span[1]/span",
    ).text.encode("utf-8")
    FractalsValueSell = int((FractalsValueSell.decode("utf-8"))[1:-6])/10
    return FractalsValueBuy+FractalsValueSell


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
    if StochRSI.decode("utf-8")[1] == "\u2212":
        StochRSI = int((StochRSI.decode("utf-8"))[2:-6])
    else:
        StochRSI = int((StochRSI.decode("utf-8"))[1:-6])
    return StochRSI


def checkStochRSIValue2():
    # getting TSI value
    StochRSI2 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[15]/td[2]/div/div[3]/div/div/span[2]/span",
    ).text.encode("utf-8")
    if StochRSI2.decode("utf-8")[1] == "\u2212":
        StochRSI2 = int((StochRSI2.decode("utf-8"))[2:-6])
    else:
        StochRSI2 = int((StochRSI2.decode("utf-8"))[1:-6])
    return StochRSI2


def checkPVTValue():
    # getting TSI value
    PVTvalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[17]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text.encode("utf-8")
    if PVTvalue.decode("utf-8")[1] == "\u2212":
        PVTvalue = float((PVTvalue.decode("utf-8"))[2:-4])
    else:
        PVTvalue = float((PVTvalue.decode("utf-8"))[1:-4])
    return PVTvalue


def getData(days):
    global i
    for _ in range(days):
        press("left")
        sleep(0.3)
        try:
            btcValue.append(checkPriceValue())
        except:
            sleep(1)
            btcValue.append(checkPriceValue())

        try:
            rsiValue.append(checkRSIValue())
        except:
            sleep(1)
            rsiValue.append(checkRSIValue())

        try:
            bbValue.append(checkBBValue())
        except:
            sleep(1)
            bbValue.append(checkBBValue())

        try:
            macdValue.append(checkMACDValue())
        except:
            sleep(1)
            macdValue.append(checkMACDValue())

        try:
            tsiValue.append(checkTSIValue())
        except:
            sleep(1)
            tsiValue.append(checkTSIValue())
        try:
            vValue.append(checkVolumeValue())
        except:
            sleep(1)
            vValue.append(checkVolumeValue())
        try:
            smiioValue.append(checkSMIIOValue())
        except:
            sleep(1)
            smiioValue.append(checkSMIIOValue())
        # try:
        #     fractalsValue.append(checkFractalsValue())
        # except:
        #     sleep(1)
        #     fractalsValue.append(checkFractalsValue())
        try:
            rocValue.append(checkROCValue())
        except:
            sleep(1)
            rocValue.append(checkROCValue())
        try:
            srsiValue.append(checkStochRSIValue())
        except:
            sleep(1)
            srsiValue.append(checkStochRSIValue())
        try:
            srsiValue2.append(checkStochRSIValue2())
        except:
            sleep(1)
            srsiValue2.append(checkStochRSIValue2())
        try:
            pvtValue.append(checkPVTValue())
        except:
            sleep(1)
            pvtValue.append(checkPVTValue())
        i += 1
        print(f"{i}/{days}", end='\r')


# Driver settings
chromedriver = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome("chromedriver", options=chrome_options)
driver.get("https://nobitex.ir/app/exchange/btc-rls/")
sleep(15)

# run functions
indicator(['RSI', 'MACD', 'TSI', 'BB', 'volume',
           'SMIIO', 'ROC', 'Stoch RSI', 'PVT'])
sleep(5)
getData(4861)  # fetch past x hours
writeFile("datasetRSIval.txt", rsiValue)
writeFile("datasetPrice.txt", btcValue)
writeFile("datasetMACD.txt", macdValue)
writeFile("datasetTSI.txt", tsiValue)
writeFile("datasetBB.txt", bbValue)
writeFile("datasetVolume.txt", vValue)
writeFile("datasetSMIIO.txt", smiioValue)
# writeFile("datasetFractals.txt", fractalsValue)
writeFile("datasetROC.txt", rocValue)
writeFile("datasetSRSI.txt", srsiValue)
writeFile("datasetSRSI2.txt", srsiValue2)
writeFile("datasetPVT.txt", pvtValue)
driver.quit()
