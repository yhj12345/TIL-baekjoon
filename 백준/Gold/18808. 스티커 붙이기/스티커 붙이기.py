def check():
    for k in range(r):
        for l in range(c):
            if sticker[k][l] == 1 and arr[i+k][j+l] == 1:
                return False
                  
    return True

def rotate_90(array):
    a = len(array)
    b = len(array[0])
    rotate_arr = [[0 for _ in range(a)] for _ in range(b)]

    for i in range(b):
        for j in range(a):
            rotate_arr[i][j] = array[a-j-1][i]
    return rotate_arr

N, M, K = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]

    for _ in range(4):    
        r = len(sticker)
        c = len(sticker[0])
        isPossible = False

        for i in range(N-r+1):
            for j in range(M-c+1):
                isPossible = check()

                if isPossible:
                    for k in range(r):
                        for l in range(c):
                            if sticker[k][l] == 1:
                                arr[i+k][j+l] = 1
                    break
                
            if isPossible:
                break
        
        if isPossible:
            break
            
        sticker = rotate_90(sticker)

        
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            ans += 1
print(ans)
