#제목: 한수
#정보: X가 한수인지 판별하는 함수를 정의하여 문제를 해결해 봅시다.

def ishansu(n):
    num = n
    L = []
    while n != 0:
        L.append(n % 10)
        n //= 10
    L.reverse()
    #각 자리 수가 1개 이하인 경우
    #어쨋든 등차수열(?)이므로 True 반환
    if len(L) <= 1:
        return True
    #각 자리 수가 2개 이상인 경우
    d = L[1] - L[0] #공차
    for i in range(len(L)):
        Ai = L[0] + i*d #일반항
        #일반항의 계산결과가 실제와 다르면 False 반환
        if Ai != L[i]:
            return False
    return True
#main
num = int(input())
ans = 0
for i in range(1,num+1):
    if ishansu(i):
        ans += 1
print(ans)
