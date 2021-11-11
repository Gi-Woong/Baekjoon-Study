#제목: 크로아티아 알파벳
#정보: 크로아티아 알파벳의 개수를 세는 문제

S = input()
ans = 0
cro_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for letter in cro_alphabet:
    S = S.replace(letter, "*")
print(len(S))