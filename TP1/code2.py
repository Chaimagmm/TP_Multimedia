import cv2
import matplotlib.pyplot as plt
import numpy as np
# Read the image with OpenCV
# Read the image
img = cv2.imread('cablecar.bmp')
if img is None:
 print("Erreur : Impossible de charger l'image.")
else:
 print (type(img))
# Converting BGR color to RGB color format
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Display the image using plt
#plt.imshow(RGB_img)
# Show without the axes
#plt.axis('off')
# Put a title
#plt.title('Image')
#plt.show()
# Separate and merge RGB images
B, G, R = cv2.split(img)
RGB_img = cv2.merge([R, G, B])
''' plt.imshow(RGB_img)
plt.axis('off')
plt.title('Image')
plt.show() '''
# création d’images vide de la même forme que l’image d’origine
'''R_img = np.zeros_like(img)
G_img = np.zeros_like(img)
B_img = np.zeros_like(img)'''
# assigner la valeur de chaque canal a la composante correspondante en laissant les autres canaux a 0
'''R_img[:, :, 0] = R # Canal Rouge
G_img[:, :, 1] = G # Canal Vert
B_img[:, :, 2] = B # Canal Bleu
figure, plot = plt.subplots(nrows=1, ncols=3)
plot[0].imshow(R_img)
plot[0].set_title('canal rouge')
plot[1].imshow(G_img)
plot[1].set_title('canal vert')
plot[2].imshow(B_img)
plot[2].set_title('canal bleu')
plt.show()'''
# Ajout d'un padding de 2 pixels de large avec une valeur de 0
padded_image = np.pad(RGB_img, pad_width=((10, 10), (10, 10), (0, 0)), mode='constant', constant_values=0)
figure, plot = plt.subplots(nrows=1, ncols=2)
plot[0].imshow(RGB_img)
plot[0].set_title('l’image originale')
plot[0].axis('off')
plot[1].imshow(padded_image)
plot[1].set_title('apres le padding')
plot[1].axis('off')
plt.show()

