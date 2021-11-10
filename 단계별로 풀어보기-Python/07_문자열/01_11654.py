#제목: 아스키 코드
#정보: 아스키 코드에 대해 알아보는 문제

N = int(input())
S = str(input())
ans = 0
for i in range(N):
    ans += int(S[i])
print(ans)