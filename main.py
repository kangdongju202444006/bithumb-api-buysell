import schedule
import time
from api import send_data_to_api
from price import nameprice
from account import balance
import os
import time
import json
import account_json
account_json.accountjson()
# keys.py에서 key 함수 가져오기
from keys import KeyManager 

apiUrl = 'https://api.bithumb.com'


keys = KeyManager()
lenkey = keys.lenaccount()

for i in range(lenkey):
    accessKey, secretKey = keys.indexkey(i)
    accessKey = str(accessKey)
    secretKey = str(secretKey)

    filename = f'account_{i+1}.json'
    with open(filename, 'r') as f:
        coins = json.load(f)

    print(coins)

    for i in range(len(coins)):
        inname = coins[i]
        inname=str(inname)
        #inname="USDT"
        #price 파일 호출
        print(coins[i])
        price = nameprice(coins[i]) #name의 가격
        print(price)

        data_to_send=[]
        # 전송할 데이터 정의 (딕셔너리 형태)
        #bid ask
        #limit,price 시장가매수 ,market 시장가 매도
        
        send_data_to_api(dict(market=f"KRW-{inname}", side="bid", price=5200, ord_type="price"),accessKey,secretKey) 
        time.sleep(1)

        #account 파일 호출
        target_currency = balance(inname,accessKey,secretKey) #name의 잔액
        print(target_currency)
        send_data_to_api(dict(market=f"KRW-{inname}", side="ask", volume=target_currency, ord_type="market"),accessKey,secretKey)