guaca.pngimport numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('guaca.png',0)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

from PIL import Image
from pylab import *
im = array(Image.open('guaca.png'))
imshow(im)
print ('Please click 3 points')
x = ginput(3)
print ('you clicked:',x)
show()
