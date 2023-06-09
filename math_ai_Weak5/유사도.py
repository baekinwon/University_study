# -*- coding: utf-8 -*-
"""유사도.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12QnvXrYjpE56N1vhap0Kc8Fmbjd3YRYw
"""

# 유클리드 유사도
import numpy as np

def ES(p,q):
    return np.sqrt(np.sum(((p-q)**2)))

# 감성분석 [긍정언어, 중립언어, 부정언어]
p = np.array([2,1,0])
q = np.array([2,2,0])
r = np.array([0,1,3])

print(ES(p,q))
print(ES(q,r))
print(ES(p,r))

# 코사인 유사도
import numpy as np

def CS(p,q):
    n = np.linalg.norm(p) * np.linalg.norm(q) # L2노름 곱한값
    i = np.dot(p,q) # 내적
    q = i/n
    return q

p = np.array([2,1,0])
q = np.array([2,2,0])
r = np.array([0,1,3])

print(CS(p,q))
print(CS(q,r))
print(CS(p,r))

