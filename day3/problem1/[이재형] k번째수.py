def solution(array, commands):
    answer = []
    
    for i in range(len(commands)) :
        a = commands
        b = sorted(array[a[i][0]-1 : a[i][1]])[a[i][2]-1]
        answer.append(b)
    
    return answer