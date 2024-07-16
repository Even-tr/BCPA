import numpy as np
import pandas as pd

N = 1_000    
DIM = 3    
TAU = 320

P_L = np.array([1,2,3.0])
P_R = np.array([2,3,4.0])

P_R/= P_R.sum()
P_L/= P_L.sum()

M = np.random.normal(loc = 200, scale= 50, size=2*N)

assert len(P_L) == DIM
assert len(P_R) == DIM

TRUE_PARAMTERS = [TAU, P_L, P_R]
def make_data_multinomial_change_point(paramters=TRUE_PARAMTERS, dim=DIM, n=N, m=M):
    tau, p_l, p_r = paramters
    res = np.zeros(shape=[n, dim])
    for i in range(tau):
        res[i] =  np.random.multinomial(n=m[i], pvals=p_l, size=1)

    for i in range(tau, n):
        res[i] = np.random.multinomial(n=m[i], pvals=p_r, size=1)
    return res


