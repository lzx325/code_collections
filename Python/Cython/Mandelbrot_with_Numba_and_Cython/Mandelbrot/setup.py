from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules=cythonize('cython_mandelbrot.pyx',compiler_directives={'language_level' : "3"}))