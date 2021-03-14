"""
=======================
imshow(Z, [cmap=], ...)
=======================
"""

import matplotlib.pyplot as plt
import numpy as np

# make data
X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-3, 3, 256))
Z = (1 - X/2. + X**5 + Y**3) * np.exp(-X**2 - Y**2)
Z = Z - Z.min()
Z = Z[::16, ::16]

# plot
with plt.style.context('cheatsheet_gallery'):
    fig, ax = plt.subplots()

    ax.imshow(Z, extent=[0, 8, 0, 8], interpolation="nearest",
              cmap=plt.get_cmap('Oranges'), vmin=0, vmax=1.6)

    ax.set_xlim(0, 8), ax.set_xticks([])
    ax.set_ylim(0, 8), ax.set_yticks([])
    plt.show()
