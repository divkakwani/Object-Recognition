
from PIL import Image


class MyImage(object):

    def __init__(self):
        pass
    

    def open(self, filename):
        im = Image.open(filename)
        self.image_array = array(im, dtype='int64')

    
    def apply(kernel):
        self.image_array = filters.convolve(self.image_array, kernel)
    
    
    
    def save(filepath):
        Image.fromarray(self.image_array).save(filepath)
        
        
    


    
    


