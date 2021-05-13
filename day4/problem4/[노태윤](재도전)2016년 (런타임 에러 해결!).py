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

# ==========================================================

# 재도전

def solution(a, b):
    
    # 날짜 dict
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

    # 요일 dict
    days = {
        1:'FRI',
        2:'SAT',
        3:'SUN',
        4:'MON',
        5:'TUE',
        6:'WED',
        0:'THU'
    }

    # 총 일 수 구하기
    total_days = sum(list(calender.values())[1:a]) + b
    
    # 7로 나누고 남은 거 담기
    answer = days[total_days%7]
        
    return answer

# 틀렸던 이유!
    # 아무 생각 없이 1,2,3,4,5,6,7 로 씀
    # 7로 나눴을 때 remainder 가 0 인 게 'THU' 인데 7 : 'THU' 로 표기했었음 ㅎㄷㄷ
    # 좀 더 신중해지자
