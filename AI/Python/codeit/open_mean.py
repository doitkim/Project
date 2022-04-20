line_mean = 0

# with open('C:/Users/user/Desktop/대구AI스쿨/Project/AI/Python/codeit/chicken.txt','rt', encoding='UTF8') as f:
#     for line in f:
#         line_s = line.strip()
#         line_sp = line_s.split(':')
#         line_mean += int(line_sp[1])
       
# print(line_mean / 31)

with open('C:/Users/user/Desktop/대구AI스쿨/Project/AI/Python/codeit/chicken.txt','rt', encoding='UTF8') as f:
    total_revenue = 0
    total_days = 0
    
    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1])  # 그날의 매출

        total_revenue += revenue
        total_days += 1

    print(total_revenue / total_days)