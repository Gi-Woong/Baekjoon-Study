#제목: ACM 호텔
#정보: 호텔 방 번호의 규칙을 찾아 출력하는 문제

#H: 호텔 층 수
#W: 호텔 층당 호 수
#N: 손님의 번째

repeat = int(input())
for i in range(repeat):
    H, W, N = map(int, input().split())
    if N%H == 0: 
        floor = H
        ho = N//H
    else:
        floor = N%H
        ho = N//H+1
    print(f"{floor}{str(ho).zfill(2)}")