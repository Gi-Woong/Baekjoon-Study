#제목: 정수 N개의 합
#정보: 함수를 구현해 봅시다. (이 문제는 C, C++, Python, Java, Go만 지원합니다. 그 외의 언어를 사용하신다면 이 문제를 무시해 주세요.)

def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans
