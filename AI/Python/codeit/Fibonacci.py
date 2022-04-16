from os import TMP_MAX


pre_num = 0 
num = 1

i = 1

while i <= 50:
    print(num)
    tmp = pre_num
    pre_num = num
    num = pre_num + tmp
    i += 1