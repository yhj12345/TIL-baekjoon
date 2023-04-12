from collections import deque
import copy

def solution(game_board, table):
    answer = -1
    N = len(game_board)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    
    def find_block_table(si, sj):
        q = deque()
        q.append((si, sj))
        tmp = [(si, sj)]
        
        while q:
            ti, tj = q.popleft()
            for k in range(4):
                ni = ti + di[k]
                nj = tj + dj[k]
                
                if 0 > ni or ni >= N or 0 > nj or nj >= N:
                    continue
                if table_visited[ni][nj] == 0 and table[ni][nj] == 1:
                    q.append((ni, nj))
                    tmp.append((ni, nj))
                    table_visited[ni][nj] = 1
        return tmp
    
    def find_board_empty(si, sj):
        q = deque()
        q.append((si, sj))
        tmp = [(si, sj)]
        
        while q:
            ti, tj = q.popleft()
            for k in range(4):
                ni = ti + di[k]
                nj = tj + dj[k]
                
                if 0 > ni or ni >= N or 0 > nj or nj >= N:
                    continue
                if board_visited[ni][nj] == 0 and game_board[ni][nj] == 0:
                    q.append((ni, nj))
                    tmp.append((ni, nj))
                    board_visited[ni][nj] = 1
        return tmp
    
    def match_block():
        for i in range(len(table_block)):
            a = table_block[i]
            for j in range(len(board_empty)):
                b = board_empty[j]
                if len(a) != len(b):
                    continue

                x = a[0][0] - b[0][0]
                y = a[0][1] - b[0][1]
                tmp = 1

                for k in range(1, len(a)):
                    if a[k][0] - b[k][0] == x and a[k][1] - b[k][1] == y:
                        tmp += 1
                    else:
                        break
                if tmp == len(a):
                    if table[a[0][0]][a[0][1]] == 1 and game_board[b[0][0]][b[0][1]] == 0:
                        for x, y in a:
                            table[x][y] = 0
                        for x, y in b:
                            game_board[x][y] = 1
                    
    
    table_visited = [[0 for _ in range(N)] for _ in range(N)]
    board_visited = [[0 for _ in range(N)] for _ in range(N)]
    table_block = []
    board_empty = []
    copy_board = copy.deepcopy(game_board)
    
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0 and board_visited[i][j] == 0:
                board_visited[i][j] = 1
                empty = find_board_empty(i, j)
                board_empty.append(empty)
            
            if table[i][j] == 1 and table_visited[i][j] == 0:
                table_visited[i][j] = 1
                block = find_block_table(i, j)
                table_block.append(block)
    
    match_block()
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = table[N-1-j][i]
    table = arr
    
    table_visited = [[0 for _ in range(N)] for _ in range(N)]
    board_visited = [[0 for _ in range(N)] for _ in range(N)]
    table_block = []
    board_empty = []
    
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0 and board_visited[i][j] == 0:
                board_visited[i][j] = 1
                empty = find_board_empty(i, j)
                board_empty.append(empty)
            
            if table[i][j] == 1 and table_visited[i][j] == 0:
                table_visited[i][j] = 1
                block = find_block_table(i, j)
                table_block.append(block)
    
    match_block()
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = table[N-1-j][i]
    table = arr
    
    table_visited = [[0 for _ in range(N)] for _ in range(N)]
    board_visited = [[0 for _ in range(N)] for _ in range(N)]
    table_block = []
    board_empty = []
    
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0 and board_visited[i][j] == 0:
                board_visited[i][j] = 1
                empty = find_board_empty(i, j)
                board_empty.append(empty)
            
            if table[i][j] == 1 and table_visited[i][j] == 0:
                table_visited[i][j] = 1
                block = find_block_table(i, j)
                table_block.append(block)
    
    match_block()
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = table[N-1-j][i]
    table = arr
    
    table_visited = [[0 for _ in range(N)] for _ in range(N)]
    board_visited = [[0 for _ in range(N)] for _ in range(N)]
    table_block = []
    board_empty = []
    
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0 and board_visited[i][j] == 0:
                board_visited[i][j] = 1
                empty = find_board_empty(i, j)
                board_empty.append(empty)
            
            if table[i][j] == 1 and table_visited[i][j] == 0:
                table_visited[i][j] = 1
                block = find_block_table(i, j)
                table_block.append(block)
    
    match_block()
    
    result = 0
    for i in range(N):
        for j in range(N):
            if copy_board[i][j] != game_board[i][j]:
                result += 1
                
    answer = result
    return answer