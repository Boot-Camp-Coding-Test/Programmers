# -*- coding: utf-8 -*-
"""[김기현] 문자열 내림차순으로 배치하기.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EEzXK4SrkfPxcvlzcsVfzyvDoCo1kKJ9
"""

def solution(n):
    s = sorted(n, reverse = True)
    answer = ''.join(s)
    return answer

n = "Zbcdefg"
solution(n)

