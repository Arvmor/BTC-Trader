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
from decimal import Decimal
import credentials  # library containing your login credentials

# variables
confidence = 0
usdtPocket = 0
coinPocket = 0
baseCoinBalance = 0
bought = False
myBuy = 0
authKey = credentials.token

# functions


def signal_handler(signal, frame):
    exit(0)


def accBalance():
    global usdtPocket, coinPocket
    # getting account Money Balance
    url = "https://api.nobitex.ir/users/wallets/balance"
    payload = {"currency": argv[2][:3]}
    headers = {"Authorization": "Token " + authKey}
    response = requests.request("POST", url, headers=headers, data=payload).text.encode(
        "utf8"
    )
    coinPocket = Decimal(json.loads(response.decode("utf-8"))["balance"])
    payload = {"currency": "usdt"}
    response = requests.request("POST", url, headers=headers, data=payload).text.encode(
        "utf8"
    )
    usdtPocket = Decimal(json.loads(response.decode("utf-8"))["balance"])
    print(usdtPocket, coinPocket)
    usdtPocket = float(argv[3])


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


def newMethodBuy(market, limit):
    global bought, myBuy
    bought = False
    headers = {"Authorization": "Token " + authKey}
    accBalance()
    while True:
        # getting sell/buy last order price
        response = requests.request("POST", "https://api.nobitex.ir/v2/orderbook", data={'symbol': market.upper()})
        sell = float(json.loads(response.text.encode("utf-8"))['bids'][0][0])
        buy = float(json.loads(response.text.encode("utf-8"))['asks'][0][0])
        difference = floor(abs(100-(buy*100)/sell) * 100)/100
        print(f' {difference}/{limit}% {datetime.datetime.now().hour}:{datetime.datetime.now().minute}', end="\r")
        
        if difference > limit and usdtPocket >= 11:
            # if profitabel
            if argv[1] == "small":
                myBuy = buy + (10**-(int(len(str(buy - int(buy))))-2))
            else:
                myBuy = buy + 0.01
            amount = usdtPocket / myBuy
            print(f'Place order {difference}/{limit}% {datetime.datetime.now().hour}:{datetime.datetime.now().minute}\n')
            
            # place order
            payload = {
                "type": "buy",
                "execution": "limit",
                "srcCurrency": market[:3],
                "dstCurrency": market[3:],
                "amount": str(amount),
                "price": myBuy}
            response = requests.request("POST", "https://api.nobitex.ir/market/orders/add", headers=headers, data=payload)
            orderId = int(json.loads(response.text.encode("utf-8"))['order']['id'])
            print(response.text.encode("utf-8"))
            while True:
                # get placed order status
                sleep(1)
                payload = {"id": orderId}
                response = requests.request("POST", "https://api.nobitex.ir/market/orders/status", headers=headers, data=payload)
                status = (json.loads(response.text.encode("utf-8"))['order']['status']).upper()
                print(status)
                
                if status == 'DONE':
                    bought = True
                    print('Bought ! done \n')
                    return
                
                # if the order got completed but not 100%
                elif float(json.loads(response.text.encode("utf-8"))['order']['matchedAmount']) > 0:
                    payload = {
                        "order": orderId,
                        "status": "canceled"}
                    requests.request("POST", "https://api.nobitex.ir/market/orders/update-status", headers=headers, data=payload).text.encode("utf8")
                    bought = True
                    print('Bought ! done \n')
                    return

                # if someone placed cheaper order switch to that price
                response = requests.request("POST", "https://api.nobitex.ir/v2/orderbook", data={'symbol': market.upper()})
                sell = float(json.loads(response.text.encode("utf-8"))['bids'][0][0])
                buy = float(json.loads(response.text.encode("utf-8"))['asks'][0][0])
                difference = floor(abs(100-(buy*100)/sell) * 100)/100
                
                if buy > myBuy or difference < limit:
                    payload = {
                        "order": orderId,
                        "status": "canceled"}
                    requests.request("POST", "https://api.nobitex.ir/market/orders/update-status", headers=headers, data=payload).text.encode("utf8")
                    
                    # if it doesn't worth it any more cancel it
                    if difference < limit:                    
                        print("not profitable")
                        return
                    
                    # set another order with higher price
                    if argv[1] == "small":
                        myBuy = buy + (10**-(int(len(str(buy - int(buy))))-2))
                    else:
                        myBuy = buy + 0.01
                    amount = usdtPocket / myBuy
                    payload = {
                        "type": "buy",
                        "execution": "limit",
                        "srcCurrency": market[:3],
                        "dstCurrency": market[3:],
                        "amount": str(amount),
                        "price": myBuy}
                    response = requests.request("POST", "https://api.nobitex.ir/market/orders/add", headers=headers, data=payload)
                    orderId = int(json.loads(response.text.encode("utf-8"))['order']['id'])
                    print(response.text.encode("utf-8"))


def newMethodSell(market, limit):
    global bought
    headers = {"Authorization": "Token " + authKey}
    accBalance()
    # getting sell/buy last order price
    response = requests.request("POST", "https://api.nobitex.ir/v2/orderbook", data={'symbol': market.upper()})
    sell = float(json.loads(response.text.encode("utf-8"))['bids'][0][0])
    if Decimal(((sell/myBuy)-1)*100) < limit:
        mySell = myBuy * float(1+limit/100)
    else:
        if argv[1] == "small":
            mySell = sell - (10**-(int(len(str(sell - int(sell))))-2))
        else:
            mySell = sell - 0.01
    #set order
    payload = {
        "type": "sell",
        "execution": "limit",
        "srcCurrency": market[:3],
        "dstCurrency": market[3:],
        "amount": str(coinPocket-baseCoinBalance),
        "price": mySell}
    response = requests.request("POST", "https://api.nobitex.ir/market/orders/add", headers=headers, data=payload)
    orderId = int(json.loads(response.text.encode("utf-8"))['order']['id'])
    print(response.text.encode("utf-8"))
    while True:
        # get placed order status
        sleep(1)
        payload = {"id": orderId}
        response = requests.request("POST", "https://api.nobitex.ir/market/orders/status", headers=headers, data=payload)
        status = (json.loads(response.text.encode("utf-8"))['order']['status']).upper()
        print(status)

        if status == 'DONE' or float(json.loads(response.text.encode("utf-8"))['order']['matchedAmount']) > 0:
            bought = False
            print('Sold ! done \n')
            return

        # if someone placed cheaper order switch to that price
        response = requests.request("POST", "https://api.nobitex.ir/v2/orderbook", data={'symbol': market.upper()})
        sell = float(json.loads(response.text.encode("utf-8"))['bids'][0][0])
        
        if sell < mySell and Decimal(((sell/myBuy)-1)*100) > limit:
            # cancel current order
            payload = {
                "order": orderId,
                "status": "canceled"}
            requests.request("POST", "https://api.nobitex.ir/market/orders/update-status", headers=headers, data=payload).text.encode("utf8")
            
            if Decimal(((sell/myBuy)-1)*100) < limit:
                mySell = myBuy * float(1+limit/100)
            else:
                if argv[1] == "small":
                    mySell = sell - (10**-(int(len(str(sell - int(sell))))-2))
                else:
                    mySell = sell - 0.01
            
            #set order
            payload = {
                "type": "sell",
                "execution": "limit",
                "srcCurrency": market[:3],
                "dstCurrency": market[3:],
                "amount": str(coinPocket-baseCoinBalance),
                "price": mySell}
            response = requests.request("POST", "https://api.nobitex.ir/market/orders/add", headers=headers, data=payload)
            orderId = int(json.loads(response.text.encode("utf-8"))['order']['id'])
            print(response.text.encode("utf-8"))


# main launch
signal(SIGINT, signal_handler)
# authenticator(credentials.email, credentials.passwd)

# getting account base Coin Balance
url = "https://api.nobitex.ir/users/wallets/balance"
payload = {"currency": argv[2][:3]}
headers = {"Authorization": "Token " + authKey}
response = requests.request("POST", url, headers=headers, data=payload).text.encode(
    "utf8"
)
baseCoinBalance = Decimal(json.loads(response.decode("utf-8"))["balance"])

while True:
    try:
        if bought == False:
            newMethodBuy(argv[2], 0.31)
        else:
            newMethodSell(argv[2], 0.31)
        sleep(2)
    except Exception as excep:
        print(excep)
