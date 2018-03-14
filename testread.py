# -*- coding:utf-8 -*-
import numpy as np

a = np.ones(10)
b = np.zeros(10)

c = np.vstack((a,b))
d = np.zeros(10)
c = np.vstack((c,d))
e = np.delete(c,0,0)
print(e)