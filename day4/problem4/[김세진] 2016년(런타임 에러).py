import calendar
def solution(a, b):
    result = calendar.weekday(2016,a,b)
    week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    answer = week[result+1]
    return answer

# 런타임 에러로 테스트케이스 3,4를 통과하지 못함... 정확도 85.7
