from timeit import default_timer as timer
from joblib import parallel
import matplotlib.pyplot as plt
import numpy as np
from numba import jit
import numba
import pandas as pd

@jit(numba.uint8(numba.float64,numba.float64,numba.int64),nopython=True)
def mandel(x,y,max_iters):
    i = 0
    c= complex(x,y)
    z=0.0j
    for i in range(max_iters):
        z=z*z+c
        if (z.real*z.real+z.imag*z.imag)>=4:
            return i
        
    return 255

@jit(numba.uint8[:,:](numba.float64,numba.float64,numba.float64,numba.float64,numba.uint8[:,:],numba.int64),nopython=False,nogil=False)
def create_fractal_sequential_gil(min_x,max_x,min_y,max_y,image,iters):
    height=image.shape[0]
    width=image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            color = mandel(real, imag, iters)
            image[y, x] = color
    
    return image

@jit(numba.uint8[:,:](numba.float64,numba.float64,numba.float64,numba.float64,numba.uint8[:,:],numba.int64),nopython=False,nogil=True)
def create_fractal_sequential_nogil(min_x,max_x,min_y,max_y,image,iters):
    height=image.shape[0]
    width=image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            color = mandel(real, imag, iters)
            image[y, x] = color
    
    return image

@jit(numba.uint8[:,:](numba.float64,numba.float64,numba.float64,numba.float64,numba.uint8[:,:],numba.int64),nopython=False,parallel=True)
def create_fractal_parallel(min_x,max_x,min_y,max_y,image,iters):
    height=image.shape[0]
    width=image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    for x in numba.prange(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            color = mandel(real, imag, iters)
            image[y, x] = color
    
    return image


