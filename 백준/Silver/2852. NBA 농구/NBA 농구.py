N = int(input())
who_win = 0
now = 0
team1_score = 0
team2_score = 0

win_team1_time = 0
win_team2_time = 0

for i in range(N):
    team, time = input().split()

    minute, second = time.split(':')
    next = int(minute) * 60 + int(second)

    if team == '1':
        team1_score += 1
    else:
        team2_score += 1

    if who_win == 0:
        if team1_score > team2_score:
            who_win = 1
        else:
            who_win = 2
        now = next

    elif who_win == 1:
        if team1_score == team2_score:
            who_win = 0
        
        win_team1_time += next - now
        now = next
    
    else:
        if team1_score == team2_score:
            who_win = 0
        
        win_team2_time += next - now
        now = next

last = 60 * 48 
if who_win == 1:
    win_team1_time += last - now
elif who_win == 2:
    win_team2_time += last - now
    
a, b = divmod(win_team1_time, 60)
c, d = divmod(win_team2_time, 60)

if a < 10:
    a = '0' + str(a)
else:
    a = str(a)
if b < 10:
    b = '0' + str(b)
else:
    b = str(b)
if c < 10:
    c = '0' + str(c)
else:
    c = str(c)
if d < 10:
    d = '0' + str(d)
else:
    d = str(d)

result1 = a + ':' + b
result2 = c + ':' + d
print(result1)
print(result2)