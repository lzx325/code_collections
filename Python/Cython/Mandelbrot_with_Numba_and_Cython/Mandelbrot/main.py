import numba
import numpy as np
import timeit
from timeit import default_timer as timer
import pandas as pd
import cython_mandelbrot as cm
import numba_mandelbrot as nm
import matplotlib.pyplot as plt
import joblib
import tempfile
import os

def main1():
    library="cm"
    image = np.zeros((10000 * 2, 15000 * 2), dtype=np.uint8)
    s = timer()
    if library=="nm":
        nm.create_fractal_parallel(-2.0, 1.0, -1.0, 1.0, image, 20)
    elif library=="cm":
        cm.create_fractal_parallel(-2.0, 1.0, -1.0, 1.0, image, 20)
    # print(cm.mandel(-1.74,-0.532,20))
    e = timer()
    print(e - s)
    fig,ax=plt.subplots()
    ax.imshow(image)
    fig.savefig(f"plot--{library}.jpg")
def main2():
    library="cm"
    image_list=[np.zeros((10000 * 2, 15000 * 2), dtype=np.uint8) for _ in range(3)]
    base_coord_range=(-2.0, 1.0, -1.0, 1.0)
    coord_range_list=[
        [c*mul for c in base_coord_range] for mul in [1,2,4]
    ]
    memmap_list=list()
    for i in range(len(image_list)):
        temp_folder = tempfile.mkdtemp()
        filename = os.path.join(temp_folder, f'joblib_test_{i}.mmap')
        if os.path.exists(filename): os.unlink(filename)
        _ = joblib.dump(image_list[i], filename)
        mmap = joblib.load(filename, mmap_mode='r+')
        memmap_list.append(mmap)
    s=timer()
    if library=="nm":
        with joblib.parallel_backend(backend="threading"): # lizx: try threading and loky
            with joblib.Parallel(n_jobs=len(image_list)) as parallel:
                parallel(
                    [joblib.delayed(nm.create_fractal_sequential_nogil)(*(coord_range_list[i]), memmap_list[i], 20) for i in range(len(memmap_list))]
                )

    elif library=="cm":
        with joblib.parallel_backend(backend="threading"):
            with joblib.Parallel(n_jobs=len(image_list)) as parallel:
                parallel(
                    [joblib.delayed(cm.create_fractal_sequential_nogil)(*(coord_range_list[i]), memmap_list[i], 20) for i in range(len(memmap_list))]
                )
    e=timer()
    print(e - s)

    # fig,ax=plt.subplots()
    # for i in range(len(memmap_list)):
    #     ax.imshow(memmap_list[i])
    #     fig.savefig(f"plot--{library}--mmap_{i}.jpg")
if __name__=="__main__":
    main1()