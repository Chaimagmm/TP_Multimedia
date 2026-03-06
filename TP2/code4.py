import cv2
from matplotlib import image
import numpy as np
# Read the image
img = cv2.imread('cablecar.bmp')
if img is None:
    print("Erreur : Impossible de charger l'image.")
else:
# Get the image height and width
    height, width, _ = img.shape
# Définir la taille des blocs
block_size = int(width/3)

bloc1 = img[0:height, 0:block_size]
bloc2 = img[0:height, block_size:2*block_size]
bloc3 = img[0:height, 2*block_size:width]

# convertir bloc2 en gris
gray_bloc2 = cv2.cvtColor(bloc2, cv2.COLOR_BGR2GRAY)
# binariser
_, bloc2_binarise = cv2.threshold(gray_bloc2, 0, 255, cv2.THRESH_OTSU)
bloc2_final = cv2.cvtColor(bloc2_binarise, cv2.COLOR_GRAY2BGR)
resultat = np.hstack([bloc1, bloc2_final, bloc3])
cv2.imshow("Resultat", resultat)
cv2.waitKey(0)
cv2.destroyAllWindows()