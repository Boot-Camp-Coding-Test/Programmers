import datetime

def solution(a, b):
    week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = datetime.datetime(2016, a, b).weekday()

    return week[day]