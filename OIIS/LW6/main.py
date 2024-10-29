import cv2


def image_resize(image, height, inter=cv2.INTER_AREA):
    (h_, w_) = image.shape[:2]

    r = height / float(h_)
    dim = (int(w_ * r), height)

    return cv2.resize(image, dim, interpolation=inter)


filenames = ['image1.jpg', 'image3.jpg', 'image2.jpg', 'image4.jpg']
cascade = 'haarcascade_frontalface_default.xml'

for filename in filenames:
    img = cv2.imread(filename)
    img = image_resize(img, height=800)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    haar_cascade = cv2.CascadeClassifier(cascade)

    faces_rect = haar_cascade.detectMultiScale(gray_img, 1.016, 42)

    for (x, y, w, h) in faces_rect:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Detected faces', img)
    cv2.waitKey(0)
