import cv2
import numpy as np
from scipy import ndimage
from skimage.feature import peak_local_max
from skimage.segmentation import watershed

image_files = ['img4.jpg']  # , 'img2.jpg', 'img1.jpg']
threshold = 120
min_distance = 50

for index, image in enumerate([cv2.imread(path) for path in image_files]):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)[1]

    distance_map = ndimage.distance_transform_edt(thresh)

    image_max = ndimage.maximum_filter(distance_map, size=50, mode='constant')

    coordinates = peak_local_max(image_max, min_distance=min_distance)
    # for coord in coordinates:
    #     cv2.drawMarker(image, coord, color=(255, 255, 255))

    markers = np.zeros_like(image_max, dtype=int)
    for i, coord in enumerate(coordinates):
        markers[coord[0], coord[1]] = i + 1

    labels = watershed(-image_max, markers, mask=thresh)

    for label in np.unique(labels):
        mask = np.zeros(gray.shape, dtype="uint8")
        mask[labels == label] = 255

        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]
        c = max(contours, key=cv2.contourArea)

        color = list(np.random.random(size=3) * 256)
        cv2.drawContours(image, [c], -1, color, 4)

    cv2.imshow(f'{index}_segmented', image)
    cv2.imwrite(f'{index}_segmented.png', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
