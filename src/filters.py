
from scipy.ndimage.filters import convolve
from numpy import array


# Handle variable size kernels

prewitt = array([[-1, 0, 1],
                 [-1, 0, 1],
                 [-1, 0, 1]])


laplace = array([[0,  1, 0],
                 [1, -4, 1],
                 [0,  1, 0]])
                 


sobel = array([[-1, -2, -1],
               [ 0,  0,  0],
               [ 1,  2,  1]])
               

avg = array([[ 0  ,  1/5,  0  ],
             [ 1/5,  1/5,  1/5],
             [ 0  ,  1/5,  0  ]])
                

