def solution(numbers, hand):
    answer = []
    Lhand = 0
    Rhand = 0
    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7 :
          answer.append('L')
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9 :
          answer.append('R')
        else :
          for j in range(len(answer)):
            if answer[j] == 'L':
              Lhand = numbers[j]
            elif answer[j] == 'R':
              Rhand = numbers[j]
          if abs(Lhand - numbers[i]) > abs(Rhand - numbers[i]):
            answer.append('R')
            Rhand = numbers[i]
          elif abs(Lhand - numbers[i]) < abs(Rhand - numbers[i]):
            answer.append('L')
            Lhand = numbers[i]
          else :
            if hand == "left":
              answer.append('L')
              Lhand = numbers[i]
            else :
              answer.append('R')
              Rhand = numbers[i]
          print(answer)
    return ''.join(answer)
    
    # 일부케이스만 풀리고, 절대값 대신 다른 방법을 찾아야될듯
