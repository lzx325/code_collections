import numpy as np
import joblib
import timeit
from threadpoolctl import threadpool_limits
import joblib

def multi1(pairs_list):
    return timeit.timeit(lambda : [arr1.dot(arr2) for arr1,arr2 in pairs_list],number=1)

def multi2(pairs_list):
    with threadpool_limits(5):
        return timeit.timeit(lambda : [arr1.dot(arr2) for arr1,arr2 in pairs_list],number=1)
def multi3(pairs_list):
    def fun():
        with joblib.Parallel(n_jobs=5,max_nbytes=1e3) as parallel: # if n_jobs>1, mat1 and mat2 will be converted to np.memmap if their sizes are large enough
            results=parallel(
                joblib.delayed(lambda mat1,mat2: ( mat1.dot(mat2) ) ) (mat1,mat2) for mat1,mat2 in pairs_list
            )
        return results
    return timeit.timeit(fun,number=1)

def multi4(pairs_list):
    with threadpool_limits(1): # simulate the fact that the low-level library can only use 1 thread
        return timeit.timeit(lambda : [arr1.dot(arr2) for arr1,arr2 in pairs_list],number=1)

def multi5(pairs_list):
    def fun():
        def inner_fun(mat1,mat2):
            with threadpool_limits(1):
                return mat1.dot(mat2)
        with joblib.parallel_backend(backend="loky"):
            with joblib.Parallel(n_jobs=5,max_nbytes=1e3) as parallel: 
                    results=parallel(
                        joblib.delayed(inner_fun ) (mat1,mat2) for mat1,mat2 in pairs_list
                    )
            return results
    return timeit.timeit(fun,number=1)

def multi6(pairs_list):
    def fun():
        def inner_fun(mat1,mat2):
            with threadpool_limits(1):
                return mat1.dot(mat2)
        with joblib.parallel_backend(backend="threading"): # lizx: use threading backend is also fine because the numpy internal releases GIL
            with joblib.Parallel(n_jobs=5,max_nbytes=1e3) as parallel: 
                    results=parallel(
                        joblib.delayed(inner_fun ) (mat1,mat2) for mat1,mat2 in pairs_list
                    )
            return results
    return timeit.timeit(fun,number=1)

def multi7(pairs_list): # This function will fail because multiprocessing cannot pickle inner functions
    def fun():
        def inner_fun(mat1,mat2):
            with threadpool_limits(1):
                return mat1.dot(mat2)
        with joblib.parallel_backend(backend="multiprocessing"): 
            with joblib.Parallel(n_jobs=5,max_nbytes=1e3) as parallel: 
                    results=parallel(
                        joblib.delayed(inner_fun ) (mat1,mat2) for mat1,mat2 in pairs_list
                    )
            return results
    return timeit.timeit(fun,number=1)

if __name__=="__main__":
    timeit.template="""
def inner(_it, _timer{init}):
    {setup}
    _t0 = _timer()
    for _i in _it:
        retval = {stmt}
    _t1 = _timer()
    return _t1 - _t0, retval
    """
    size=15000
    n_pairs=5
    pairs_list=list()
    print("creating matrices")
    for _ in range(n_pairs):
        arr1=np.random.rand(size,size)
        arr2=np.random.rand(size,size)    
        pairs_list.append((arr1,arr2))
    
    print("computing multiplications")
    time,result=multi7(pairs_list)
    print(f"Time Elapsed: {time}")

    print("computing mean")
    print([res.mean() for res in result])