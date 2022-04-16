# greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]

# i = 0
# while i < len(greetings):
#     print(greetings[i])
#     i += 1


# # 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5 / 9


# temperature_list = [40, 15, 32, 64, -4, 11]
# print(f"화씨 온도 리스트: {temperature_list}")  # 화씨 온도 출력

# # 리스트의 값들을 화씨에서 섭씨로 변환하는 코드
# i = 0
# while i < len(temperature_list):
#     temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
#     i += 1
# print(f"섭씨 온도 리스트: {temperature_list}")  # 섭씨 온도 출력

prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]

def krw_to_usd(krw):
    return krw / 1000

def usd_to_jpy(usd):
    return usd / 8 * 1000

print(f"한국화폐: {str(prices)}")

i = 0
while i < len(prices):
    prices[i] = krw_to_usd(prices[i])
    i += 1
    
print(f"미국화폐: {str(prices)}")

i = 0
while i < len(prices):
    prices[i] = usd_to_jpy(prices[i])
    i +=1

print(f"일본화폐: {str(prices)}")