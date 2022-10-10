from envtest import smooth_image
from envtest import rand_array
from scipy import misc
import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc
import matplotlib.pyplot as plt

shape = (3, 3)

image = misc.ascent()
sigma = 5
smoothed_image = smooth_image(image,sigma)

f = plt.figure()
f.add_subplot(1,2,1)
plt.imshow(image)
f.add_subplot(1,2,2)
plt.imshow(smoothed_image)
plt.show(block=True)

print(rand_array(shape))


def smooth_image(a,sigma=1):
    return gaussian_filter(a,sigma=sigma)