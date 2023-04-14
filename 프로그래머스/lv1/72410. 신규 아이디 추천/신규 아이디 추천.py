def solution(new_id):
    answer = ''
    # 소문자로 바꾸기
    new_id = new_id.lower()
    
    # 알파벳, 숫자, -, _, . 제외한 모든 문자 제거
    possible = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '.']
    tmp = ''
    for char in new_id:
        if char.isalpha() or char in possible:
            tmp += char
    new_id = tmp
    
    # . 압축
    tmp = ''
    cnt = 0
    for char in new_id:
        if char == '.':
            cnt += 1
        else:
            if cnt > 0:
                tmp += '.'
                cnt = 0
            tmp += char
    new_id = tmp
    # 맨 앞,뒤 . 제거
    new_id = new_id.strip('.')
    
    # 빈 문자열 -> a 대입
    if len(new_id) == 0:
        new_id = 'a'
    
    # 15자만 남기기
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.strip('.')
    
    # 7단계
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    answer = new_id
    return answer