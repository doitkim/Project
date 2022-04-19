import random

check_num = random.randint(1,20)
count = 4

for i in range(1,count+1):
    print(f"기회가 {count}번 남았습니다.")
    input_num = int(input("1-20 사이의 숫자를 맞혀보세요:"))
    if input_num == check_num:
        print(f"축하합니다. {count}번만에 숫자를 맞히셨습니다.")
        break
    elif input_num >= check_num:
        print("Down")
        count -= 1
    elif input_num <= check_num:
        print("Up")
        count -= 1
if count == 0:
    print("아쉽게도 기회를 다 썻습니다.")
        

        