"""
파이토치로 다층 퍼셉트론 구현하기

"""

import torch
import torch.nn as nn

# GPU 사용 가능한 여부 파악 test code

device = "cuda" if torch.cuda.is_available() else "cpu"

# seed
torch.manual_seed(777)

if device =="cuda":
    torch.cuda.manual_seed_all(777)

elif device == "cpu":
    torch.cuda.manual_seed_all(777)
    print("seed")

# 데이터 생성

x = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [[0], [1], [1], [0]]

# 데이터 텐서 변경

x = torch.tensor(x, dtype=torch.float32).to(device)
y = torch.tensor(y, dtype=torch.float32).to(device)

print("x",x)
print("y",y)

"""
다층 퍼셉트콘 설계
"""

model = nn.Sequential(
    nn.Linear(2,10,bias=True),
    nn.Sigmoid(),
    nn.Linear(10,10, bias=True),
    nn.Sigmoid(),
    nn.Linear(10,10, bias=True),
    nn.Sigmoid(),
    nn.Linear(10,1, bias=True),
    nn.Sigmoid()

)

model.to(device)

print(model)

"""
Loss Function BCELoss() 이진 분류에서 사용되는 크로스엔트로피 함수
"""

criterison = torch.nn.BCELoss().to(device)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

"""
학습 코드 작성 하기
"""

for epoch in range(10001):
    optimizer.zero_grad() # 옵티마이저 초기화

    # forward 연산
    output = model(x)

    # loss 계산
    loss = criterison(output, y)
    loss.backward()
    optimizer.step()

    # print show
    if epoch % 100 == 0:
        print(f"epoch >> {epoch} Loss >> {loss.item()}")

"""
다층 퍼셉트론의 예측값 확인
"""

with torch.no_grad():
    output = model(x)
    predicted = (output > 0.5).float()
    acc = (predicted == y).float().mean()
    print("모델의 출력값 output >> " , output.detach().cpu().numpy())
    print("모델의 예측값 predicted >> ", predicted.detach().cpu().numpy())
    print("실제값 >>>>" ,y.cpu().numpy())
    print("정확도 >>>>>", acc.item()*100)

