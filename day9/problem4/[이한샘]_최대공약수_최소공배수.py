# -*- coding: utf-8 -*-
"""[이한샘] 최대공약수 최소공배수.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RloXNM7HBrNf1GRXTWUoTz_HhCyCCoPi
"""

def solution(n, m) :
  a, b = n,m  
  while b!=0 :
      temp = a%b
      a = b
      b = temp
  gcd = a
  lcm = int(n*m/gcd) 
  return [gcd,lcm]