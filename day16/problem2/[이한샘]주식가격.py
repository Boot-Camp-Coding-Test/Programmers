# -*- coding: utf-8 -*-
"""[이한샘]주식가격.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-TkY_wd3mn2RkxuWL6lT0gLnVR2ggByA
"""

def solution(prices):
    answer = []
    for i in range(len(prices)):
      count = 0
      for j in range(i+1, len(prices)):
        count+= 1
        if prices[i] > prices[j]:
          break
      answer.append(count)
    return answer

prices = [1, 2, 3, 2, 3]

solution(prices)