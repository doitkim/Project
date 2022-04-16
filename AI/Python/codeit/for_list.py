# my_list = [2,3,5,7,11]

# for number in my_list:
#     print(number)

# i =0

# for i in range(0,101,2): 
#     print(i)

# numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# # 인덱스와 원소 출력
# i=0
# for number in numbers:
#     index = numbers.index(number)
#     print(str(index) + " " + str(number))
#     i += 1

# for i in range(len(numbers)):
#     print(i, numbers[i])

# i = 0
# for i in range(0,11):
#     ze = 2**i
#     print(f"2^{i}={ze}")

# i=0

# for i in range(1,10):
#     j=0
#     for j in range(1,10):
#         mul = i * j
#         print(f"{i} * {j} = {mul}")
#         j += 1
#     i += 1

# for a in range(1, 400):
#     for b in range(1, 400):
#         c = 400 - a - b
#         if a * a + b * b == c * c and a < b < c:
#             print(a * b * c)
            

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers) // 2):
    # 인덱스 left와 대칭인 인덱스 right 계산    
    right = len(numbers) - left - 1

    # 위치 바꾸기
    numbers[right], numbers[left] = numbers[left], numbers[right]

print("뒤집어진 리스트: " + str(numbers))