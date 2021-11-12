#제목: 그룹 단어 체커
#정보: 조건에 맞는 문자열을 찾는 문제

def isgroup(S):
    L = []
    prev = ""
    for s in S:
        if prev != s:
            if not s in L:
                L.append(s)
                prev = s
            else:
                return False
    return True

N = int(input())
cnt = 0
for i in range(N):
    S = input()
    if isgroup(S):
        cnt += 1
print(cnt)




