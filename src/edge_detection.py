

import filters

prewitt_edge_detection = [ f_repr('array'),
                           noise_elim,
                           sharpen, 
                           filters.f_convolve(filters.sobel),
                           f_repr('image'),
                           a_view ]

