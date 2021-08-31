import numpy as np
from joblib import Parallel, delayed
def is_memmap(obj):
    if isinstance(obj, np.memmap):
        return True, obj.flags.writeable
    else:
        return False
def try_modify(obj):
    obj[0]=100
if __name__=="__main__":
    arr_list=[
        np.ones((100,)),
        np.ones((10000,)),
        np.ones((1000000,)),
    ]
    # lizx: when loky is used, the non-memmap arrays is modifiable but their changes is not updated in the global arr_list. This is because they are done on a dumpped copy
    # lizx: when loky is used the memmap arrays is not writeable and will generate error
    # lizx: when threading is used, the arrays are neither memmap-ed or dumped. Modification is in-place
    result=Parallel(n_jobs=2, max_nbytes=1e6,backend="threading")(
        delayed(try_modify)(arr)
        for arr in arr_list)
    print(result)
    print(arr_list)



