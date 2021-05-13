# 9,13 런타임 에러

def solution(a, b):

    calender = {
        0:0,
        1:31,
        2:29,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    }

    days = {
        1:'FRI',
        2:'SAT',
        3:'SUN',
        4:'MON',
        5:'TUE',
        6:'WED',
        7:'THU'
    }

    total_days = sum(list(calender.values())[1:a]) + b
    answer = days[total_days%7]
        
    return answer
