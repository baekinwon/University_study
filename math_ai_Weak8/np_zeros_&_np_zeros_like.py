# -*- coding: utf-8 -*-
"""np.zeros & np.zeros_like.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1piLzGCXNmKHrTkxguRSqttwhyPQJLnYz
"""

import numpy as np

a = np.zeros([2,3,3])

a

b = np.zeros((2,3,3))

a = np.zeros_like((2,3,3,10))
b = np.zeros_like(a)

b

a = np.zeros_like([2,3,3,10])
b = np.zeros_like(a)

b