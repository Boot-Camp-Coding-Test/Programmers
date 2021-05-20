# -*- coding: utf-8 -*-
"""[이한샘]소수만들기.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AN6erOq-9peNLJ4k3_SkJG2NXJo638N0
"""

import itertools 

def solution(nums):
    temp = list(itertools.combinations(nums, 3))
    result = []
    for t in temp :
      sum_temp = sum(t)
      result.append(sum_temp)
      for i in range(2, int(sum_temp**0.5)+1):
        if sum_temp%i == 0 :
          result.remove(sum_temp)
          break
  
    return len(result)