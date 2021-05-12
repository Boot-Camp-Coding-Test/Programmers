def solution(array, commands):
  answer = []
  for i in range(len(commands)) :
    x = sorted(array[commands[i][0]-1 : commands[i][1]])[commands[i][2]-1]
    answer.append(x)
  return answer
