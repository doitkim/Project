import random 
i =  0
n = 0

def generate_numbers(n):
  
    num = []
    for i in range(n):
        num.append(random.randint(1,46))
        i += 1
    return num

def draw_winning_numbers():
    num = []
    bonus =[]
    for i in range(6):
        num.append(random.randint(1,46))
        i += 1    
    bonus.append(random.randint(1,46))
    for i in range(6):
        if num[i]  == bonus:
            return draw_winning_numbers()
        elif num[i-1] == num[i]:
            return draw_winning_numbers()
        
    return sorted(num) + bonus

def count_matching_numbers(numbers, winning_numbers):
    same_numbers = list(set(numbers).intersection(winning_numbers[:-1]))
    return len(same_numbers)

def check(numbers, winning_numbers):
    matching_count = count_matching_numbers(numbers, winning_numbers)
    if matching_count == 6:
        # print("1등 : 1,000,000,000")
        return 1000000000
    elif matching_count == 5:
        same_numbers = list(set(numbers).intersection(winning_numbers[6]))
        if same_numbers == 1:
            # print("2등 : 50,000,000")
            return 50000000
        else:
            # print("3등 : 1,000,000")
            return 1000000
    elif matching_count == 4:
        # print("4등 : 50,000")
        return 50000
    elif matching_count == 3:
        # print("5등 : 5,000")
        return 5000
    else:
        # print("아쉽게도 당첨이 되지 않았습니다.")
        return 0
numbers =  generate_numbers(6)
winning_numbers = draw_winning_numbers()

print(f"{numbers}\n{winning_numbers}")
check(numbers, winning_numbers)






   

# 테스트
# print(check(numbers, winning_numbers))
