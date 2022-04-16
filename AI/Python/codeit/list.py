#리스트 (list)

import numbers


numbers =  [2,3,5,7,11,13]
names =["윤수", "혜린", "태호", "영훈"]

# 리스트 슬라이싱(list slicing)
new_list = numbers[:3]
print(numbers[3:])
print(new_list)

numbers[0] = numbers[1] + numbers[2]

print(numbers[0])