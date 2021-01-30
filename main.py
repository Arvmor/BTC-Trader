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
rialPocket = 0
usdtPocket = 0
coinPocket = 0
baseCoinBalance = 0
usdtPrice = 0
bought = False
sold = False
authKey = credentials.token

# functions


def signal_handler(signal, frame):
    exit(0)


def accBalance():
    global usdtPocket, coinPocket, rialPocket
    # getting account Money Balance
    url = "https://api.nobitex.ir/users/wallets/balance"
    payload = {"currency": argv[1][:3]}
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
    payload = {"currency": "rls"}
    response = requests.request("POST", url, headers=headers, data=payload).text.encode(
        "utf8"
    )
    rialPocket = Decimal(json.loads(response.decode("utf-8"))["balance"])
    print(f"$ {usdtPocket} \t BTC {coinPocket} \t Rial {rialPocket}")
    usdtPocket = float(argv[2])


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


def buyCoinDollar(limit=2.5):
    global bought, usdtPrice
    bought = False
    headers = {"Authorization": "Token " + authKey}
    accBalance()
    while True:
        # getting sell/buy last order price
        response = requests.request("POST", "https://api.nobitex.ir/v2/orderbook", data={'symbol': argv[1].upper()})
        bid = float(json.loads(response.text.encode("utf-8"))['bids'][0][0])
        response = requests.request("POST", "https://api.nobitex.ir/v2/orderbook", data={'symbol': argv[1][:3].upper()+"IRT"})
        ask = float(json.loads(response.text.encode("utf-8"))['asks'][0][0])
        response = requests.request("POST", "https://api.nobitex.ir/v2/orderbook", data={'symbol': "USDTIRT"})
        usdtPrice = float(json.loads(response.text.encode("utf-8"))['bids'][0][0])
        difference = floor(100-((100*ask)/usdtPrice)/bid * 100)/100
        print(f' {difference}/{limit}% {datetime.datetime.now().hour}:{datetime.datetime.now().minute}', end="\r")
        
        if difference > limit and usdtPocket >= 11:
            # if profitabel
            print(f'Placing Buy order {difference}/{limit}% {datetime.datetime.now().hour}:{datetime.datetime.now().minute}\n')
            amount = usdtPocket / bid
            
            # place order
            payload = {
                "type": "buy",
                "execution": "limit",
                "srcCurrency": argv[1][:3],
                "dstCurrency": argv[1][3:],
                "amount": str(amount),
                "price": bid}
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
                
                if difference < limit:
                    payload = {
                        "order": orderId,
                        "status": "canceled"}
                    requests.request("POST", "https://api.nobitex.ir/market/orders/update-status", headers=headers, data=payload).text.encode("utf8")                  
                    print("not profitable")
                    return


def sellCoinRial():
    global sold
    sold = False
    headers = {"Authorization": "Token " + authKey}
    accBalance()

    # getting sell/buy last order price
    response = requests.request("POST", "https://api.nobitex.ir/v2/orderbook", data={'symbol': argv[1][:3].upper()+"IRT"})
    ask = float(json.loads(response.text.encode("utf-8"))['asks'][0][0])

    #set order
    payload = {
        "type": "sell",
        "execution": "limit",
        "srcCurrency": argv[1][:3],
        "dstCurrency": 'rls',
        "amount": str(coinPocket-baseCoinBalance),
        "price": ask}
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
            print('Sold ! done \n')
            sold = True
            return


def exchangeToDollar(limit=0.5):
    global sold, bought
    headers = {"Authorization": "Token " + authKey}
    accBalance()

    # Get USDT price
    response = requests.request("POST", "https://api.nobitex.ir/v2/orderbook", data={'symbol': "USDTIRT"})
    latestUsdtPrice = float(json.loads(response.text.encode("utf-8"))['bids'][0][0])
    print(latestUsdtPrice, usdtPrice)
    amount = rialPocket / Decimal(usdtPrice)
    
    # If the latest usdt price is same as the old one or lower, place the order
    
    # place order
    payload = {
        "type": "buy",
        "execution": "limit",
        "srcCurrency": "usdt",
        "dstCurrency": "rls",
        "amount": str(amount),
        "price": latestUsdtPrice}
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
            bought = False
            sold = False
            print('Bought ! done \n')
            return

# main launch
signal(SIGINT, signal_handler)
# authenticator(credentials.email, credentials.passwd)

# getting account base Coin Balance
url = "https://api.nobitex.ir/users/wallets/balance"
payload = {"currency": argv[1][:3]}
headers = {"Authorization": "Token " + authKey}
response = requests.request("POST", url, headers=headers, data=payload).text.encode(
    "utf8"
)
baseCoinBalance = Decimal(json.loads(response.decode("utf-8"))["balance"])

while True:
    # try:
    if bought == False:
        buyCoinDollar(0.6)
    elif sold == False:
        sellCoinRial()
    else:
        exchangeToDollar()
    sleep(2)
    # except Exception as excep:
    #     print(excep)
