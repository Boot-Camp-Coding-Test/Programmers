import numpy as np
def solution(answers):
    a = len(answers)
    num1 = [1,2,3,4,5]*8
    num2 = [2,1,2,3,2,4,2,5]*5
    num3 = [3,3,1,1,2,2,4,4,5,5]*4
    res1 = 0
    res2 = 0
    res3 = 0
    if a > 40:
      moc = a//40
      nam = a%40
      num1 = num1 * moc
      num2 = num2 * moc
      num3 = num3 * moc
      for i in range(nam):
        num1.append(num1[i])
        num2.append(num2[i])
        num3.append(num3[i])
    else :
      num1 = num1[:a]
      num2 = num2[:a]
      num3 = num3[:a]
    num1 = np.array(num1) - np.array(answers)
    num2 = np.array(num2) - np.array(answers)
    num3 = np.array(num3) - np.array(answers)
    for i in num1:
      if i == 0:
        res1+=1
    for i in num2:
      if i == 0:
        res2+=1
    for i in num3:
      if i == 0:
        res3+=1

    if res1 > res2 and res1 > res3:
      answer = [1]
    elif res2 > res1 and res2 > res3:
      answer = [2]
    elif res3 > res1 and res3 > res3:
      answer = [3]
    elif res1 == res2 and res2 > res3:
      answer = [1,2]
    elif res1 == res3 and res3 > res2:
      answer = [2,3]
    elif res1 == res3 and res1 > res2:
      answer = [1,3]
    else:
      answer = [1,2,3]
    return answer
