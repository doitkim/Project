# # 자리수 합 리턴
# def sum_digit(num):
#     total = 0
#     str_num = str(num)
    
#     for digit in str_num:
#         total += int(digit)

#     return total


# # sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# digit_total = 0
# for i in range(1, 1001):
#     digit_total += sum_digit(i)

# print(digit_total)

# def mask_security_number(security_number):
#     return security_number[:-4] + '****'


# # 테스트
# print(mask_security_number("880720-1234567"))
# print(mask_security_number("8807201234567"))
# print(mask_security_number("930124-7654321"))
# print(mask_security_number("9301247654321"))
# print(mask_security_number("761214-2357111"))
# print(mask_security_number("7612142357111"))

def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    # for문에서 나왔다면 모든 쌍이 일치
    return True


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
