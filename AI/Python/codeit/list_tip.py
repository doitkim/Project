# # value가 some_list의 요소인지 확인
# def in_list(some_list, value):
#     i = 0
#     while i < len(some_list):
#         # some_list에서 value를 찾으면 True를 리턴
#         if some_list[i] == value:
#             return True
#         i = i + 1

#     # 만약 some_list에서 value를 발견하지 못했으면 False를 리턴
#     return False

# # 테스트
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
# print(in_list(primes, 7))
# print(in_list(primes, 12))


# print(7 in primes)
# print(12 in primes)


# print(7 not in primes)
# print(12 not in primes)

# # 세 번의 시험을 보는 수업
# grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

# # 첫 번째 학생의 성적
# print(grades[0])

# # 세 번째 학생의 성적
# print(grades[2])

# # 첫 번째 학생의 첫 번째 시험 성적
# print(grades[0][0])

# # 세 번째 학생의 두 번째 시험 성적
# print(grades[2][1])

# # 첫 번째 시험의 평균
# print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)


numbers = [5, 3, 7, 1]
numbers.sort()
print(numbers)

numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)

members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))

fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)

