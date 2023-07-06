# 제목: 행렬 덧셈
# 설명: 행렬을 2차원 배열로 만들어 더하는 문제

# code
import sys


def input():  # input 재정의
    return sys.stdin.readline().rstrip().split()


N, M = map(int, input())

mat1 = []
for i in range(N):
    mat1.append(map(int, input()))
result = ""
for i in range(N):
    mat2 = map(int, input())
    line = [str(m1 + m2) for m1, m2 in zip(mat1[i], mat2)]
    result += " ".join(line) + "\n"

print(result)
