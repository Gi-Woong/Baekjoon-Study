#제목: 분수찾기
#정보: 분수의 순서에서 규칙을 찾는 문제

X = int(input())

floor = 0
hap = 0
#floor(층) 찾기
while X > hap:
    floor += 1
    hap += floor

#hap(합)에서 floor(층)수를 빼서 이전 층까지의 합과 X의 차 구하기
onnum = X - (hap - floor)

#floor(층)이 짝수면 순행출력, 홀수면 역행출력
if floor % 2 == 0:
    #순행 출력
    print(f"{onnum}/{floor+1-onnum}")
else:
    #역행 출력
    print(f"{floor+1-onnum}/{onnum}")
