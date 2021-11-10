#제목: 알파벳 찾기
#정보: 한 단어에서 각 알파벳이 처음 등장하는 위치를 찾는 문제

string = str(input())
L = []
#아스키코드 a-z까지의 숫자
for i in range(97, 123):
    letter = chr(i)
    if letter in string:
        L.append(string.index(letter))
    else:
        L.append(-1)
print(" ".join(map(str, L)))
