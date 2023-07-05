# 제목: 숫자카드
# 설명: 카드의 집합을 만들어 특정 카드가 집합에 있는지 빠르게 찾는 문제

# [메모]
# test_cards 중에 sanguen_cards 내의 정수가 있다면 1, 아니면 0을 append하기


#  code
import sys


def input():  # input 재정의
    return sys.stdin.readline().rstrip()


def bn_search(L, key) -> bool:
    low, high = 0, len(L)-1
    while low <= high:
        mid = (low + high)//2
        if key < L[mid]:
            high = mid - 1
        elif key > L[mid]:
            low = mid + 1
        else:
            return True
    return False


M = int(input())
sanguen_cards = sorted(list(map(int, input().split())))
N = int(input())
test_cards = list(map(int, input().split()))
result = []
for card in test_cards:
    result.append("1" if bn_search(sanguen_cards, card) else "0")

print(" ".join(result))
