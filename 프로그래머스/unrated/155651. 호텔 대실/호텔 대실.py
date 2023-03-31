from collections import defaultdict

def solution(book_time):
    answer = 0
    
    hotel_time_dict = defaultdict(int)
    
    for checkin, checkout in book_time:
        hour, minute = map(int, checkout.split(':'))
        minute += 10
        if minute >= 60:
            hour += 1
            minute -= 60
        
        if hour < 10:
            hour = '0' + str(hour)
        if minute < 10:
            minute = '0' + str(minute)
            
        
        checkout = str(hour) + ':' + str(minute)
        
        hotel_time_dict[checkin] += 1
        hotel_time_dict[checkout] -= 1
    
    sorted_hotel_time_dict = sorted(hotel_time_dict)
    
    result = 0
    for time in sorted_hotel_time_dict:
        result += hotel_time_dict[time]
        answer = max(answer, result)
    
    return answer