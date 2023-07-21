T = int(input())
for tc in range(T):
    record = list(input().split())
    animal = set()
    END = 'what does the fox say?'

    while True:
        s = input()
        if s == END:
            break
        
        sound = s.split()[-1]
        animal.add(sound)

    ans = []

    for r in record:
        if r not in animal:
            ans.append(r)

    print(*ans)