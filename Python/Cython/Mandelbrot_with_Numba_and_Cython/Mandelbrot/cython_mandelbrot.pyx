# distutils: extra_compile_args = -fopenmp
# distutils: extra_link_args = -fopenmp

cimport cython
cimport cython.parallel
cdef int mandel_nogil(float x, float y , int max_iters) nogil:
    cdef:
        int i=0
        float complex c=x+y*1.0j
        # float complex c= complex(x,y)
        float complex z= 0.0j
    for i in range(max_iters):
        z=z*z+c
        if (z.real*z.real+z.imag*z.imag)>=4:
            return i

    return 255

cdef int mandel_gil(float x, float y , int max_iters):
    cdef:
        int i=0
        float complex c=x+y*1.0j
        # float complex c= complex(x,y)
        float complex z= 0.0j
    for i in range(max_iters):
        z=z*z+c
        if (z.real*z.real+z.imag*z.imag)>=4:
            return i

    return 255


cpdef unsigned char[:,:] create_fractal_sequential_gil(
    float min_x, 
    float max_x,
    float min_y,
    float max_y,
    unsigned char[:,:] image,
    int iters
):
    print("with gil")
    cdef:
        size_t height=image.shape[0]
        size_t width=image.shape[1]
        float real=0.0
        float imag=0.0
        unsigned char color=0
        float pixel_size_x = (max_x - min_x) / width
        float pixel_size_y = (max_y - min_y) / height
        size_t x=0,y=0
    for x in range(width):
        real =min_x+x*pixel_size_x
        for y in range(height):
            imag=min_y+y*pixel_size_y
            color = mandel_gil(real,imag,iters)
            image[y,x]=color
    return image

cpdef unsigned char[:,:] create_fractal_sequential_nogil(
    float min_x, 
    float max_x,
    float min_y,
    float max_y,
    unsigned char[:,:] image,
    int iters
):
    print("without gil")
    cdef:
        size_t height=image.shape[0]
        size_t width=image.shape[1]
        float real=0.0
        float imag=0.0
        unsigned char color=0
        float pixel_size_x = (max_x - min_x) / width
        float pixel_size_y = (max_y - min_y) / height
        size_t x=0,y=0
    with nogil:
        for x in range(width):
            real =min_x+x*pixel_size_x
            for y in range(height):
                imag=min_y+y*pixel_size_y
                color = mandel_nogil(real,imag,iters)
                image[y,x]=color
        return image

cpdef unsigned char[:,:] create_fractal_parallel(
    float min_x, 
    float max_x,
    float min_y,
    float max_y,
    unsigned char[:,:] image,
    int iters
):
    cdef:
        size_t height=image.shape[0]
        size_t width=image.shape[1]
        float real=0.0
        float imag=0.0
        unsigned char color=0
        float pixel_size_x = (max_x - min_x) / width
        float pixel_size_y = (max_y - min_y) / height
        size_t x=0,y=0
    for x in cython.parallel.prange(width,nogil=True,schedule="dynamic"): # lizx: it seems that using dynamic here will be better than numba's default parallelization
    # for x in range(width):
        real =min_x+x*pixel_size_x
        for y in range(height):
            imag=min_y+y*pixel_size_y
            color = mandel_nogil(real,imag,iters)
            image[y,x]=color
    return image


