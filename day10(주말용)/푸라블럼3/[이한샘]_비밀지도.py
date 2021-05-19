# -*- coding: utf-8 -*-
"""[이한샘] 비밀지도.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HUBVVEFWc-vUyNzy99Kckdqk5qZphq5H
"""

n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]

# ["#####","# # #", "### #", "# ##", "#####"]

def solution(n, arr1, arr2) :
    answer = []
    for i,j in zip(arr1, arr2):
      string = bin(i|j)[2:]
      if len(string) != n :
        string = '0'*(n-len(string))+string
      string = string.replace('0', " ")
      string = string.replace('1', "#")
      answer.append(string)

    return answer