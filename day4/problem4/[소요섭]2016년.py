def solution(a,b):
    days_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weeks = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    days = sum(days_of_month[:a-1])+b 
    answer = weeks[(days % 7)-1]
    return answer
