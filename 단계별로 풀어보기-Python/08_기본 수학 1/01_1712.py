#제목: 손익분기점
#정보: 이익이 발생하는 지점을 찾는 문제

#A: 고정비용 B: 가변비용 (제품 한대당 생산비용)
#C: 책정된 노트북 가격
#손익분기점: 총 비용과 총 판매수입보다 높아지면서 이익이 나는 시점

#A + B*[판매량] = C*[판매량] 이 되는 시점 +1을 구해야 함. 

#손익분기점이 존재하지 않으면 -1 출력

A, B, C = map(int, input().split())
if C-B <= 0:# 분모가 +가 아니라면
    print(-1)
else:
    print(A//(C-B)+1)