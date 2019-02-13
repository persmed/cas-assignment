import numpy as np
import matplotlib.pyplot as plt


image = np.zeros((5, 5))
image[2, 2] = 1
seg = np.zeros((5, 5))
seg[2, 1] = 0.5
seg[2, 3] = 1

fig = plt.figure()
t = plt.imshow(image, cmap='gray', interpolation=None)
t2 = plt.imshow(seg, cmap='jet', alpha=0.5, interpolation=None)
plt.title("Image")
plt.show()