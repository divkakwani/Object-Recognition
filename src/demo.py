
from PIL import Image
from numpy import array
from scipy.ndimage import filters

########### filters definition ################

prewitt = array([[-1, 0, 1],
                 [-1, 0, 1],
                 [-1, 0, 1]])


laplace = array([[0,  1, 0],
                 [1, -4, 1],
                 [0,  1, 0]])
                 


sobel = array([[-1, -2, -1],
               [ 0,  0,  0],
               [ 1,  2,  1]])
               

avg = array([[ 1/9.,  1/9.,  1/9.],
             [ 1/9.,  1/9.,  1/9.],
             [ 1/9.,  1/9.,  1/9.]])
                
                 
########### atomic operations definition ##########

def view(image):
    image.show()
    return
    

########## factory procedures #############

def f_repr(form):
    # fixme: what if type(image) == form
    if form == 'array':
        return lambda image : array(image)
    else:
        return lambda array : Image.fromarray(array)
        
 
    
def f_convolve(kernel):
    return lambda array : filters.convolve(array, kernel)



###########     flow-seq defintions     ###########

prewitt_edge_detection = [ f_repr('array'),
                           #noise_elim,
                           f_convolve(avg), 
                           f_convolve(sobel),
                           f_repr('image'),
                         ]
    

################ util functions ###########
    
def perform_op(image, definition):
    
    final_im = reduce(lambda x, y: y(x), definition, image)
    return final_im

######### client's code ###############

im = Image.open('/home/divyanshu/test.jpg').convert('L')
#im = perform_op(im, prewitt_edge_detection)
im.save('/home/divyanshu/op.jpg')


    
