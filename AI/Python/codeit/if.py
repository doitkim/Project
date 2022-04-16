# def print_grade(midterm_score, final_score):
#     total = midterm_score + final_score
#     if total >= 90:
#         print("A")
#     elif 80 <= total <90:
#         print("B")
#     elif 70 <= total <80:
#         print("C")
#     elif 60 <= total <70:    
#         print("D")
#     else:
#         print("F")


# # 테스트
# print_grade(40, 45)
# print_grade(20, 35)
# print_grade(30, 32)
# print_grade(50, 45)


# i = 1
# while i < 100:
#     if i % 8 == 0 and i % 12 != 0:
#         print(i)
#     i += 1

# i=0
# sum = 0

# while i < 1000:
#     if i % 2 == 0 or i % 3 == 0:
#         sum +=i
#     i += 1
# print(sum)

i = 1
n = 120
count = 0

while i <= 120:
    if n % i == 0:
        print(i)
        count += 1
    i += 1
print(f"정수 {n}의 약수는 총 {count}개 입니다.")
    