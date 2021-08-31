import numpy as np
import time
from joblib import Parallel, delayed,dump, load
import os
np.random.seed(0)
data0 = np.random.random((int(1e7),))
window_size = int(5e5)
slices = [slice(start, start + window_size)
          for start in range(0, data0.size - window_size, int(5e5))]

def slow_mean(data, sl):
    """Simulate a time consuming processing."""
    time.sleep(0.01)
    return data[sl].mean()

def slow_mean_set(data, sl, result_arr, result_str_arr, idx):
    time.sleep(0.01)
    mean_value=data[sl].mean()
    result_arr[idx]=mean_value # lizx: return through array
    result_str_arr[idx]=str(mean_value)
    return mean_value # lizx: return through normal return value

tic = time.time()
results = [slow_mean(data0, sl) for sl in slices]
toc = time.time()
print('\nElapsed time computing the average of couple of slices {:.2f} s'
      .format(toc - tic))

tic = time.time()
results = Parallel(n_jobs=2)(delayed(slow_mean)(data0, sl) for sl in slices)
toc = time.time()
print('\nElapsed time computing the average of couple of slices {:.2f} s'
      .format(toc - tic))

folder = './joblib_memmap'
os.makedirs(folder,exist_ok=True)
data_filename_memmap = os.path.join(folder, 'data0_memmap')
dump(data0, data_filename_memmap)
data = load(data_filename_memmap, mmap_mode='r')
tic = time.time()
results = Parallel(n_jobs=2)(delayed(slow_mean)(data, sl) for sl in slices)
toc = time.time()
print('\nElapsed time computing the average of couple of slices {:.2f} s\n'
      .format(toc - tic))

# lizx: write results back to an array
result_memmap = os.path.join(folder, 'result_memmap')
data = load(data_filename_memmap, mmap_mode='r')
result=np.memmap(result_memmap,dtype=data0.dtype,shape=(len(slices),),mode="w+")
result_str=np.memmap(result_memmap,dtype=np.object,shape=(len(slices),),mode="w+")

tic = time.time()
ret_results = Parallel(n_jobs=2)(delayed(slow_mean_set)(data, sl, result, result_str, idx) for idx , sl in enumerate(slices))
toc = time.time()

print(data)
print(result)
print(result_str)
print(ret_results)
print('\nElapsed time computing the average of couple of slices {:.2f} s\n'
      .format(toc - tic))