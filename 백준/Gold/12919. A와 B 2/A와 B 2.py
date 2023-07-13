def dfs(word):
    global result
    if word == S:
        result = 1
        
    if len(word) <= len(S):
        return
    

    if word[0] == 'B':
        tmp = word[1:]
        tmp = tmp[::-1]
        dfs(tmp)
    
    if word[-1] == 'A':
        tmp = word[:-1]
        dfs(tmp)

S = input()
T = input()
result = 0
dfs(T)

print(result)