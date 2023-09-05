T = int(input())

for i in range(T):
    N = int(input())
    quarter, mod = N // 25, N % 25
    dime, mod = mod // 10, mod % 10
    nickel, penny = mod // 5, mod % 5
    print(quarter, dime, nickel, penny)
