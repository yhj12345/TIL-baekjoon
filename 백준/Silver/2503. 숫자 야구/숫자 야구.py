N = int(input())
arr = [list(input().split()) for _ in range(N)]

promisingNums = []

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and i !=k:
                newNum = 100*i + 10*j + k
                promisingNums.append(str(newNum))

for callNumber, strike, ball in arr:
    newPromisingNums = []
    
    for promisingNum in promisingNums:
        nowStrike = 0
        nowBall = 0

        for i in range(3):
            if callNumber[i] == promisingNum[i]:
                nowStrike += 1

        for i in range(3):
            for j in range(3):
                if (i !=j and callNumber[i] == promisingNum[j]):
                    nowBall += 1
        
        if strike == str(nowStrike) and ball == str(nowBall):
            newPromisingNums.append(promisingNum)
    
    promisingNums = newPromisingNums

print(len(promisingNums))