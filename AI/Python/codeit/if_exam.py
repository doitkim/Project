# 상수 정의
INTEREST_RATE = 0.12
APARTMENT_PRICE_2016 = 1100000000

# 변수 정의
year = 1988
bank_balance = 50000000

while year < 2016:
    bank_balance = bank_balance * (1 + INTEREST_RATE)
    year += 1


change = int(bank_balance - APARTMENT_PRICE_2016)

if bank_balance > APARTMENT_PRICE_2016:
    print(f"{change}원 차이로 동일 아저씨 말씀이 맞습니다.")
else:
    print(f"{change}원 차이로 미란 아주머니 말씀이 맞습니다.")