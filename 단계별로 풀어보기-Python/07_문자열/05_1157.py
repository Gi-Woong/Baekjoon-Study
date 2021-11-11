#제목: 단어 공부
#정보: 주어진 단어에서 가장 많이 사용된 알파벳을 출력하는 문제

S = str(input()).upper()
Sletters = list(set(S))
Scount = list(map(lambda x: S.count(x), Sletters))
Smax = max(Scount)
if Scount.count(Smax) > 1:
    print("?")
else:
    print(Sletters[Scount.index(Smax)])
    