# my_dictionary = {
#     5: 25,
#     2: 4,
#     3: 9
#     }

# print(type(my_dictionary))
# print(my_dictionary[3])

# my_dictionary[9] = 81
# print(my_dictionary)

# # 1. 단어장 만들기
# vocab = {
#     'sanitizer': '살균제',
#     'ambition': '야망',
#     'conscience': '양심',
#     'civilization': '문명'
# }
# print(vocab)


# # 2. 새로운 단어들 추가
# vocab['privilege'] = '특권'
# vocab['principle'] = '원칙'
# print(vocab)

# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(dict):
    new_dict = {}  # 새로운 사전
    
    # dict의 key와 value를 뒤집어서 new_dict에 저장
    i = 0
    while i < len(vocab):
        for key, value in vocab.items():
            new_dict[value] =key
            i += 1   
    return new_dict  # 변환한 새로운 사전 리턴


# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))