def myself(name, age, nationality="한국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1, "미국")  # 옵셔널 파라미터를 제공하는 경우
print()
myself("코드잇", 1)  # 옵셔널 파라미터를 제공하지 않는 경우


# # 다음 두 줄은 같습니다
# x = x + 1
# x += 1

# # 다음 두 줄은 같습니다
# x = x + 2
# x += 2

# # 다음 두 줄은 같습니다
# x = x * 2
# x *= 2

# # 다음 두 줄은 같습니다
# x = x - 3
# x -= 3
