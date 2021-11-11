#제목: 문자열 반복
#정보: 각 문자를 반복하여 출력하는 문제

inp = int(input())
for i in range(inp):
    R, S = input().split()
    ans = ""
    for s in str(S):
        ans += s*int(R)
    print(ans)