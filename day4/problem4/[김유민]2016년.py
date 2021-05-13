def solution(a, b):
    months = {m: 30 if (m%2==0) else 31 for m in range(1, 8)}
    months.update({m: 31 if (m%2==0) else 30 for m in range(8, 13)})
    months[2] = 29

    days_list = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    num_days = 0
    for i in range(1, a) :
        num_days += months[i]
        
    num_days += (b-1)
    print(months)
    return days_list[num_days%7]
