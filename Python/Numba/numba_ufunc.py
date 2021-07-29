from numba import vectorize, guvectorize, float64
import numpy as np
@vectorize([float64(float64,float64)])
def f(x,y):
    return x+y

@vectorize(["float64(float64,float64)"]) # lizx: using the string form is more convenient
def f2(x,y):
    return x+y

def simulate_emax_np(static_utilities,draws):
    utilities=static_utilities + draws
    max_utilities=utilities.max(axis=1)
    emax=max_utilities.mean()
    return emax

def main1():
    arr1=np.random.rand(10,5)
    arr2=np.random.rand(10,1)
    print(f2(arr1,arr2))

@guvectorize(
    ["float64[:], float64[:,:], float64[:]"],
    "(n_choices),(n_draws,n_choices)->()",
    nopython=True
)
def simulate_emax_numba(static_utilities,draws,emax):
    n_draws,n_choices=draws.shape
    emax_=0
    for i in range(n_draws):
        max_utility = 0
        for j in range(n_choices):
            utility = static_utilities[j] + draws[i, j]

            if utility > max_utility or j == 0:
                max_utility = utility

        emax_ += max_utility

    emax[0] = emax_ / n_draws # lizx: emax is a single pointer to the return value, use [0] to dereference

if __name__=="__main__":
    n_draws=1000
    np.random.seed(42)
    static_utilities = np.random.randn(10,5,4)
    draws=np.random.randn(10,1,n_draws,4)
    print(simulate_emax_numba(static_utilities,draws).shape)