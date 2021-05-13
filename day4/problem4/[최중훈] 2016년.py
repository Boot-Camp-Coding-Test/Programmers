def solution(a, b):
    months_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for i in range(len(months_days)):
        if a == i + 1:
            sum_days = sum(months_days[:i+1]) - months_days[i] + b
            if sum_days % 7 == 1: answer = "FRI"
            if sum_days % 7 == 2: answer = "SAT"
            if sum_days % 7 == 3: answer = "SUN"
            if sum_days % 7 == 4: answer = "MON"
            if sum_days % 7 == 5: answer = "TUE"
            if sum_days % 7 == 6: answer = "WED"
            if sum_days % 7 == 0: answer = "THU"

    return answer
