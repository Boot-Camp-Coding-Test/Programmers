def solution(a, b):
    mon=[31,29,31,30,31,30,31,31,30,31,30]
    day=['FRI','SAT','SUN','MON','TUE','WED','THU']
    res = (sum(mon[:a-1])+b)%7 
    return day[res-1]
