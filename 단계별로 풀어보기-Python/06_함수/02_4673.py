#제목: 셀프 넘버
#정보: 함수 d를 정의하여 문제를 해결해 봅시다.

def d(n):
    num = n
    ans = 0
    while num != 0:
        ans += num % 10
        num //= 10
    return ans + n
L = list(range(10000))

for i in L[:]:
    try: L.remove(d(i))
    except: pass

for i in L:
    print(i)