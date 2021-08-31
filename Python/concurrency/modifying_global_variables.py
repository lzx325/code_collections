from joblib import Parallel, delayed
import numpy as np
shared_set = set()
shared_array=np.zeros((5,))
def collect(x):
   shared_set.add(x)
   shared_array[x]=10
# lizx: use threading will modify the global variables, but using loky and multiprocessing will not
Parallel(n_jobs=2,backend="threading",require="sharedmem")(
    delayed(collect)(i) for i in range(5)
)
print(sorted(shared_set))
print(shared_array)
