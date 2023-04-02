def solution(n, money):
    answer = 0
    money.sort()
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    
    for m in money:
        for i in range(1, n+1):
            if i >= m:
                dp[i] += dp[i-m]
                
    answer = dp[n] % 1000000007
        
    return answer