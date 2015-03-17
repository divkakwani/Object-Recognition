"""

Image Processing Module
Author : Divyanshu Kakwani

"""

from PIL import Image, ImageFilter
from pylab import *
import matplotlib.pyplot as plt
from scipy.ndimage import filters

img_name = 'bw.jpg'

class MyImage(object):

    def __init__(self, img_name, mode = 'c', pixel_table = None):
        """
        """
        self._name = img_name
        self._mode = mode
        if pixel_table is not None:
            self._pixel_table = pixel_table
        elif mode == 'g':
            # Load an image, convert it to grayscale and store in an array
            self._pixel_table = array(Image.open(img_name).convert('L'), dtype='int64')
        else:
            # Load the image as it is
            self._pixel_table = array(Image.open(img_name), dtype='int64')

    def display(self):
        """
            Display the image using matplotlib alias plt
        """
        plt.figure()                    # generates a figure
        if self._mode == 'g':
            plt.gray()                  # restricts the colors to graylevel
        plt.imshow(self._pixel_table)   # draws the image on canvas
        
    def show_hist(self):
        """
            Displays the histogram of the image
        """
        hist(self._pixel_table.flatten(), 128)
        plt.show()
        return

    def get_dim(self):
        """
            Returns a tuple of the form (height, width)
        """
        return self._pixel_table.shape

    def blurr(self, mask_size = 3):
        """
            Returns a blurred image with the given intensity
        """
        assert self._mode == 'g'
        coeff = 1.0 / mask_size ** 2
        mask = array([[coeff for j in range(mask_size)] for i in range(mask_size)])
        return MyImage('Blurred', 'g', filters.convolve(self._pixel_table, mask))

    def denoise(self):
        """
            Using median filter
        """
        return MyImage('Denoised', 'g', filters.median_filter(self._pixel_table, 5))

    def x_gradient(self):
        
        mask = array([ [-1, -1, -1],
                       [ 0,  0,  0],            # Prewitt Operator
                       [ 1,  1,  1] ])
        
        convolved_img = MyImage('gx', 'g', filters.convolve(self._pixel_table, mask))
        return convolved_img

    def y_gradient(self):

        mask = array([ [-1, 0, 1],
                       [-1, 0, 1],              # Prewitt Operator
                       [-1, 0, 1] ])
 

        
        convolved_img = MyImage('gx', 'g', filters.convolve(self._pixel_table, mask))
        return convolved_img

    def edge_detect(self):
        
        mag = self.x_gradient()._pixel_table + self.y_gradient()._pixel_table

        # Thresholding
        threshold = 20                      # make thresholds dynamic
        for row in range(mag.shape[0]):
            for col in range(mag.shape[1]):
                if abs(mag[row][col]) > threshold:
                    mag[row][col] = 255
                else:
                    mag[row][col] = 0
        return MyImage('edge', 'g' , mag)
    
    def laplacian(self):
        
        assert self._mode == 'g'
        mask = array([ [0,  1, 0],
                       [1, -4, 1],
                       [0,  1, 0] ])
        convolved_img = MyImage('Laplacian', 'g', filters.convolve(self._pixel_table, mask))
        threshold = 20
        for row in range(convolved_img._pixel_table.shape[0]):
            for col in range(convolved_img._pixel_table.shape[1]):
                if abs(convolved_img._pixel_table[row][col]) > threshold:
                    convolved_img._pixel_table[row][col] = 255
                else:
                    convolved_img._pixel_table[row][col] = 0
        return convolved_img
        """
        return MyImage('Sobel', 'g', filters.sobel(self._pixel_table))
        """


im = MyImage(img_name, 'g')
#im.blurr(10).display()
#im.denoise().blurr().laplacian().display()
#im.denoise().laplacian().display()
im.display()
im.denoise().blurr().laplacian().display()
im.denoise().blurr().edge_detect().display()
plt.show()
