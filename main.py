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

# variables
confidence = 0
usdtPocket = 0
coinPocket = 0
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
    coinPocket = float(json.loads(response.decode("utf-8"))["balance"])
    payload = {"currency": "usdt"}
    response = requests.request("POST", url, headers=headers, data=payload).text.encode(
        "utf8"
    )
    usdtPocket = float(json.loads(response.decode("utf-8"))["balance"])


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


def newMethod(market, limit):
    # getting wallet balance
    bought = False
    sold = False
    headers = {"Authorization": "Token " + authKey}
    accBalance()
    # getting sell/buy last order price
    response = requests.request(
        "POST", "https://api.nobitex.ir/v2/orderbook", data={'symbol': market.upper()})
    sell = float(json.loads(response.text.encode("utf-8"))['bids'][0][0])
    buy = float(json.loads(response.text.encode("utf-8"))['asks'][0][0])
    difference = floor(abs(100-(buy*100)/sell) * 100)/100
    print(f' {difference}/{limit}% {datetime.datetime.now().hour}:{datetime.datetime.now().minute}', end="\r")
    if difference > limit:
        # if profitabel
        myBuy = buy + 0.01
        amount = usdtPocket / myBuy
        print(
            f'{difference}/{limit}% {datetime.datetime.now().hour}:{datetime.datetime.now().minute}')
        # place order
        payload = {
            "type": "buy",
            "execution": "limit",
            "srcCurrency": market[:3],
            "dstCurrency": market[3:],
            "amount": str(amount),
            "price": myBuy
        }
        response = requests.request(
            "POST", "https://api.nobitex.ir/market/orders/add", headers=headers, data=payload)
        orderId = int(json.loads(
            response.text.encode("utf-8"))['order']['id'])
        while not bought:
            # get placed order status
            payload = {"id": orderId}
            response = requests.request(
                "POST", "https://api.nobitex.ir/market/orders/status", headers=headers, data=payload)
            status = json.loads(response.text.encode(
                "utf-8"))['order']['status']
            if status == 'Done':
                bought = True
                break
            sleep(1)
            # if someone placed cheaper order switch to that price
            response = requests.request(
                "POST", "https://api.nobitex.ir/v2/orderbook", data={'symbol': market.upper()})
            sell = float(json.loads(
                response.text.encode("utf-8"))['bids'][0][0])
            buy = float(json.loads(
                response.text.encode("utf-8"))['asks'][0][0])
            difference = floor(abs(100-(buy*100)/sell) * 100)/100
            if buy > myBuy or difference < limit:
                payload = {
                    "order": orderId,
                    "status": "canceled"}
                requests.request("POST", "https://api.nobitex.ir/market/orders/update-status",
                                 headers=headers, data=payload).text.encode("utf8")
                # if it doesn't worth it any more cancel it
                if difference < limit:
                    return
                myBuy = buy + 0.01
                amount = usdtPocket / myBuy
                payload = {
                    "type": "buy",
                    "execution": "limit",
                    "srcCurrency": market[:3],
                    "dstCurrency": market[3:],
                    "amount": str(amount),
                    "price": myBuy}
                response = requests.request(
                    "POST", "https://api.nobitex.ir/market/orders/add", headers=headers, data=payload)
                orderId = int(json.loads(
                    response.text.encode("utf-8"))['order']['id'])
        # send a sell order
        response = requests.request(
            "POST", "https://api.nobitex.ir/v2/orderbook", data={'symbol': market.upper()})
        sell = float(json.loads(
            response.text.encode("utf-8"))['bids'][0][0])
        mySell = sell - 0.01
        payload = {
            "type": "sell",
            "execution": "limit",
            "srcCurrency": market[:3],
            "dstCurrency": market[3:],
            "amount": str(amount),
            "price": mySell
        }
        response = requests.request(
            "POST", "https://api.nobitex.ir/market/orders/add", headers=headers, data=payload)
        orderId = int(json.loads(
            response.text.encode("utf-8"))['order']['id'])
        while not sold:
            # get placed order status
            payload = {"id": orderId}
            response = requests.request(
                "POST", "https://api.nobitex.ir/market/orders/status", headers=headers, data=payload)
            status = json.loads(response.text.encode(
                "utf-8"))['order']['status']
            if status == 'Done':
                sold = True
                break
            sleep(1)
            # if someone placed cheaper order switch to that price
            response = requests.request(
                "POST", "https://api.nobitex.ir/v2/orderbook", data={'symbol': market.upper()})
            sell = float(json.loads(
                response.text.encode("utf-8"))['bids'][0][0])
            buy = float(json.loads(
                response.text.encode("utf-8"))['asks'][0][0])
            difference = floor(abs(100-(buy*100)/sell) * 100)/100
            if sell < mySell:
                # if it doesn't worth it any more cancel it
                if difference < limit:
                    return
                payload = {
                    "order": orderId,
                    "status": "canceled"}
                requests.request("POST", "https://api.nobitex.ir/market/orders/update-status",
                                 headers=headers, data=payload).text.encode("utf8")
                mySell = sell - 0.01
                payload = {
                    "type": "sell",
                    "execution": "limit",
                    "srcCurrency": market[:3],
                    "dstCurrency": market[3:],
                    "amount": str(coinPocket),
                    "price": mySell}
                response = requests.request(
                    "POST", "https://api.nobitex.ir/market/orders/add", headers=headers, data=payload)
                orderId = int(json.loads(
                    response.text.encode("utf-8"))['order']['id'])


# main launch
signal(SIGINT, signal_handler)
authenticator(credentials.email, credentials.passwd)
if argv[1] == "new":
    while True:
        try:
            newMethod(argv[2], 0.7)
            sleep(2)
        except:
            sleep(10)
