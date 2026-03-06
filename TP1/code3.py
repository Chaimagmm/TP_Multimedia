import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cablecar.bmp')
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Add padding with 0 first (black border as base)
padded_image = np.pad(RGB_img, pad_width=((10, 10), (10, 10), (0, 0)), mode='constant', constant_values=0)

# Top border → Green (R=0, G=255, B=0)
padded_image[:10, :, 0] = 0    # R
padded_image[:10, :, 1] = 255  # G
padded_image[:10, :, 2] = 0    # B

# Bottom border → Red (R=255, G=0, B=0)
padded_image[-10:, :, 0] = 255  # R
padded_image[-10:, :, 1] = 0    # G
padded_image[-10:, :, 2] = 0    # B

# Left border → Blue (R=0, G=0, B=255)
padded_image[:, :10, 0] = 0    # R
padded_image[:, :10, 1] = 0    # G
padded_image[:, :10, 2] = 255  # B

# Right border → Magenta (R=255, G=0, B=255)
padded_image[:, -10:, 0] = 255  # R
padded_image[:, -10:, 1] = 0    # G
padded_image[:, -10:, 2] = 255  # B

# Display
figure, plot = plt.subplots(nrows=1, ncols=2)
plot[0].imshow(RGB_img)
plot[0].set_title("l'image originale")
plot[0].axis('off')

plot[1].imshow(padded_image)
plot[1].set_title('apres le padding')
plot[1].axis('off')

plt.show()