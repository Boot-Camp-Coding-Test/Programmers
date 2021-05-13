import calendar
def solution(a, b):
    result = calendar.weekday(2016,a,b)
    week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    answer = week[result+1]
    return answer
