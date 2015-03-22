# Architecture

Any complex operation on an image consists of application of a sequence of simpler operations. 
For example, the operation of edge detection consists of the following sequence of operations :

* Noise elimination
* Sharpening - to highlight edges
* Apply a suitable operator

The operation can be represented as a list in python :
```
prewitt_edge_detection = [ noise_elim, sharpen, convolve(prewitt)]
```
Let us call this list as the operation's flow-seq.

Every operation that appears in the flow-seq of an operation accepts an image from the previous operation and outputs a processed image to the following operation. These operations themselves can be defined in the same way. 

However, there are certain operations that cannot be described in this way. They are of one of the following types:

* Atomic operations
* Factory operations - like convolve in the above list.



