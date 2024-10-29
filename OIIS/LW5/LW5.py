import cv2
import numpy as np


def shift_image(image, x_shift, y_shift=0):
    rows, cols = image.shape[:2]
    m = np.float32([[1, 0, x_shift], [0, 1, y_shift]])
    return cv2.warpAffine(image, m, (cols, rows))


filename_left = 'i1.jpg'
filename_right = 'i2.jpg'

left_image = cv2.imread(filename_left)  # For left eye
right_image = cv2.imread(filename_right)  # For right eye

# Shift images
right_image_shifted = shift_image(right_image, x_shift=10)

# Take only R channel from left image
left_r = left_image.copy()
left_r[:, :, [1, 2]] = 0

# Take only G and B channels from right image
right_gb = right_image_shifted.copy()
right_gb[:, :, 0] = 0

anaglyph_image = cv2.addWeighted(left_r, 1, right_gb, 1, 0)

cv2.imwrite(f'{filename_right[:-4]}_alanglyph.jpg', anaglyph_image)
cv2.imshow('Anaglyph', anaglyph_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
