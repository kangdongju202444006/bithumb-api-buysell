class KeyManager:
    def __init__(self):
        #여러 계정 입력시 순차적으로 작동
        self.accessKey = [
            '빗썸 api키',
            '빗썸 api키',
            '빗썸 api키'
        ]
        self.secretKey = [
            '빗썸 api키',
            '빗썸 api키',
            '빗썸 api키'
        ]

    def indexkey(self, i):
        return self.accessKey[i], self.secretKey[i]

    def lenaccount(self):
        return len(self.accessKey)