from collections import defaultdict

alpah_dict = defaultdict(int)
name = input()
for n in name:
    alpah_dict[n] += 1

cnt = 0
flag = False
for alpah in alpah_dict:
    if alpah_dict[alpah] % 2 != 0:
        cnt += 1

    if cnt >= 2:
        flag = True
        break

if flag:
    print("I'm Sorry Hansoo")

else:
    ans = ''
    a = ''
    tmp = sorted(alpah_dict)
    for t in tmp:
        if alpah_dict[t] % 2 == 0:
            for i in range(alpah_dict[t] // 2):
                ans += t
        else:
            for i in range(alpah_dict[t] // 2):
                ans += t
            a = t
    
    tmp = ans[::-1]
    if a != '':
        ans += a
        ans += tmp
    else:
        ans += tmp
    print(ans)