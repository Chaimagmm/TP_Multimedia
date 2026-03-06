import cv2
import numpy as np
# Read the image
img = cv2.imread('cablecar.bmp')
if img is None:
 print("Erreur : Impossible de charger l'image.")
else:
 print (type(img))
 # Get the image height and width
 height, width, channels = img.shape
 print (f'height: {height} / width: {width} / channels: {channels}')
 resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
# Save the image
 cv2.imwrite("resized.png", resized_img)
 # Create a window with a title "Image" to display the image
# cv2.imshow("Image", img)
 # Hold the screen until the user closes it.
 #cv2.waitKey(0)
 # Destroy the window
 #cv2.destroyAllWindows()
 # Resize an image
# Convert from BGR to YCrCb color space: Y is the Luminance component, Cb and Cr chrominance components
img_ycrcb = cv2.cvtColor(resized_img, cv2.COLOR_BGR2YCrCb)
cv2.imwrite("ycrcb_random.png", img_ycrcb)
# Convert from BGR to HSV color space
img_hsv = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)
cv2.imwrite("hsv_random.png", img_hsv)
# Convert an RGB image to grayscale
img_gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
# concatenate image Horizontally
images = np.concatenate((cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR), img_ycrcb, img_hsv), axis=1)
cv2.imshow('Gray, YCrCb and HSV images', images)
cv2.waitKey(0)
cv2.destroyAllWindows()