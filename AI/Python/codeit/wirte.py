# with open('C:/Users/user/Desktop/대구AI스쿨/Project/AI/Python/codeit/write_file.txt', 'a') as f:
#     f.write("hello world!\n")
#     f.write("file creat and write")

# with open('C:/Users/user/Desktop/대구AI스쿨/Project/AI/Python/codeit/vocabulary.txt', 'a') as f:
#     while 1 :
#         input_eng= input("영어 단어를 입력하세요: ")
#         if input_eng == 'q':
#             break
#         f.write(input_eng + ':')
#         input_eng= input("한국어 뜻을 입력하세요: ")
#         if input_eng == 'q':
#             break
#         f.write(input_eng +"\n")
      
# count = 0
# with open('C:/Users/user/Desktop/대구AI스쿨/Project/AI/Python/codeit/vocabulary.txt', 'r') as f:
#     for read_file in f:
#         quiz_word = read_file.strip()
#         quiz_ws = quiz_word.split(":")
#         answer_word = input(f"{quiz_ws[1]}: ")
#         if quiz_ws[0] == answer_word:
#             print("맞았습니다.")
#             count +=1
#         else:
#             print(f"아쉽습니다. 정답은 {quiz_ws[0]}입니다.")
# print(f"맞은 갯수는 {count}개 입니다.")

# count = 0
# with open('C:/Users/user/Desktop/대구AI스쿨/Project/AI/Python/codeit/vocabulary.txt', 'r') as f:
#     for read_file in f:
#         ws = read_file.strip()
#         wss = ws.split(":")
#         quiz_word = {f'{wss[1]}' : f'{wss[0]}'}
#         print(quiz_word['원숭이'])
        
import random

# 사전 만들기
vocab = {}
with open('C:/Users/user/Desktop/대구AI스쿨/Project/AI/Python/codeit/vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip()
        data = data.split(":")
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word

# 목록 가져오기
keys = list(vocab.keys())

# 문제 내기
while True:
    # 랜덤한 문제 받아오기
    index = random.randint(0, len(keys) - 1)
    english_word = keys[index]
    korean_word = vocab[english_word]
    
    # 유저 입력값 받기
    guess = input("{}: ".format(korean_word))
    
    # 프로그램 끝내기
    if guess == 'q':
        break
    
    # 정답 확인하기
    if guess == english_word:
        print("정답입니다!\n")
    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))