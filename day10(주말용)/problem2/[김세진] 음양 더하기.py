def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True: #true면 그대로
            absolutes[i] = absolutes[i]*1
        elif signs[i] == False: #false면 음수로
            absolutes[i] = absolutes[i]*(-1)
        answer += absolutes[i]
    return answer
