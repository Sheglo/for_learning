import numpy as np
from skimage import io, transform
import matplotlib.pyplot as plt

# Загрузите исходное изображение
image = io.imread('162883910918461889.jpg')
output_shape = (image.shape[0] // 2, image.shape[1] // 2)
resized_image = transform.resize(image, output_shape, anti_aliasing=True)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('оригинал')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(resized_image)
plt.title('уменьшенное')
plt.axis('off')

# Покажите оба изображения
plt.tight_layout()
plt.show()
