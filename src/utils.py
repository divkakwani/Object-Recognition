

from numpy import array


def a_view(image):
	# atomic operation
    image.show()
    return
    

def f_repr(form):
    # fixme: what if type(image) == form
    if form == 'array':
        return lambda image : array(image)
    else:
        return lambda array : Image.fromarray(array)
        
        
        
def perform_op(image, definition):
    final_im = reduce(lambda x, y: y(x), definition, image)
    return final_im


