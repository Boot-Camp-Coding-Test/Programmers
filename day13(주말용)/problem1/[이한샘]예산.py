# -*- coding: utf-8 -*-
"""[이한샘]예산.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/120FOncjS7SuUrOvjw6eG1WUCHWIS5Rro
"""

def solution(d, budget):
    d_sum = sum(d)
    if d_sum > budget :
       while d_sum > budget :
          max_num = max(d)
          d_sum = d_sum-max_num
          d.remove(max_num)
    return len(d)