#제목: 달팽이는 올라가고 싶다
#정보: 달팽이의 움직임을 계산하는 문제

#A: 낮에 달팽이가 올라갈 수 있는 길이
#B: 밤에 달팽이가 미끄러지는 길이
#V: 나무막대 높이

import math
A, B, V = map(int, input().split())
day = math.ceil((V - A)/(A - B)) + 1
print(day)
