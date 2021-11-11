#제목: 다이얼
#정보: 규칙에 따라 문자에 대응하는 수를 출력하는 문제

S = input()
t = 0
for s in S:
    chrnum = ord(s)
    if chrnum > 64 and chrnum < 80: #A~O
        t += (ord(s)-65)//3+3
    elif chrnum < 84: #PQRS
        t += 8
    elif chrnum < 87:#TUV
        t += 9
    elif chrnum < 91:#WXYZ
        t += 10
print(t)