def solution(n, m, x, y, queries):
    answer = -1
    rangeX, rangeY = [x, x+1], [y, y+1]
    
    d = [1, -1, 1, -1]
    
    for i in range(len(queries)-1, -1, -1):
        command, dx = queries[i]
        
        if command == 0:
            rangeY[1] += d[command] * dx
            
            if rangeY[0] > 0:
                rangeY[0] += d[command] * dx
                
        elif command == 1:
            rangeY[0] += d[command] * dx
            
            if rangeY[1] < m:
                rangeY[1] += d[command] * dx
        
        elif command == 2:
            rangeX[1] += d[command] * dx
            
            if rangeX[0] > 0:
                rangeX[0] += d[command] * dx
                
        elif command == 3:
            rangeX[0] += d[command] * dx
            
            if rangeX[1] < n:
                rangeX[1] += d[command] * dx
    
        if rangeX[0] < 0:
            rangeX[0] = 0
            
        elif rangeX[0] > n:
            rangeX[0] = n
        
        if rangeX[1] < 0:
            rangeX[0] = 0
            
        elif rangeX[1] > n:
            rangeX[1] = n

        if rangeY[0] < 0:
            rangeY[0] = 0
            
        elif rangeY[0] > m:
            rangeY[0] = m
            
        if rangeY[1] < 0:
            rangeY[1] = 0
            
        elif rangeY[1] > m:
            rangeY[1] = m

        if (rangeX[1] - rangeX[0])*(rangeY[1] - rangeY[0]) <= 0: return 0
            
    a = rangeX[1] - rangeX[0]
    b = rangeY[1] - rangeY[0]
    answer = a * b
    
    return answer