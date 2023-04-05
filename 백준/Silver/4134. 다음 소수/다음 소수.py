T = int(input())

for tc in range(T):
    n = int(input())

    if n <= 1:
        n = 2

    while True:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                n += 1
                break
        
        else:
            print(n)
            break