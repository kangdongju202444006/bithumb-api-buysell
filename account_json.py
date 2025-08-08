import schedule
import time
from api import send_data_to_api
from price import nameprice

from account import balance
import jwt
import uuid
import time
import requests
import json
# keys.py에서 key 함수 가져오기
from keys import KeyManager 

def accountjson():

    accessKey = '발급받은 API KEY'
    secretKey = '발급받은 SECRET KEY'
    apiUrl = 'https://api.bithumb.com'



    keys = KeyManager()
    lenkey = keys.lenaccount()

    # 제외할 코인 리스트 (예시: 'BTC', 'ETH'를 제외)
    exclude_coins = ['KRW', 'P', 'BOBA', 'SSG','IPX']

    for i in range(lenkey):
        accessKey, secretKey = keys.indexkey(i)
        accessKey = str(accessKey)
        secretKey = str(secretKey)

        payload = {
            'access_key': accessKey,
            'nonce': str(uuid.uuid4()),
            'timestamp': round(time.time() * 1000)
        }
        jwt_token = jwt.encode(payload, secretKey)
        authorization_token = 'Bearer {}'.format(jwt_token)
        headers = {
            'Authorization': authorization_token
        }

        try:
            response = requests.get(apiUrl + '/v1/accounts', headers=headers)
            if response.status_code == 200:
                account_data = response.json()
                
                # 필터링 조건 추가
                coin_symbols = [
                    coin["currency"] 
                    for coin in account_data 
                    if coin["currency"] not in exclude_coins  # ← 필터링 조건
                ]
                
                filename = f'account_{i+1}.json'
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(coin_symbols, f, ensure_ascii=False, indent=4)
                    
                print(f"{filename} 파일에 코인명 저장 완료")
        except Exception as err:
            print(f"계정 {i+1} 오류 발생: {err}")

    print("모든 계정 정보가 각각의 파일에 저장되었습니다. (특정 코인 제외)")


if __name__ == "__main__":
    accountjson()
    print("JSON 파일 생성 완료")