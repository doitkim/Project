import numbers


numbers = [19,13,2,5,3,11,7,17]

new_list = sorted(numbers, reverse=True) # 기존리스트 영향 없이 설정
print(new_list)
numbers.sort() # 기존 리스트를 정렬
print(numbers)