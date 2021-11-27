#제목: 벌집
#정보: 벌집이 형성되는 규칙에 따라 벌집의 위치를 구하는 문제

N = int(input())
An = 1 
i = 1 # 건너야 하는 room 개수
while N > An:
    An += 6*i
    i += 1
print(i)