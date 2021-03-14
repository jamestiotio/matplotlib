"""
========================
streamplot([X, Y], U, V)
========================
"""
import matplotlib.pyplot as plt
import numpy as np

# make a stream function:
X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-3, 3, 256))
Z = (1 - X/2. + X**5 + Y**3) * np.exp(-X**2 - Y**2)
Z = Z - Z.min()
# make U and V out of the streamfunction:
V = np.diff(Z[1:, :], axis=1)
U = -np.diff(Z[:, 1:], axis=0)

# plot:
with plt.style.context('cheatsheet_gallery'):
    fig, ax = plt.subplots()
    # contour stream function
    ax.contour(X, Y, Z, colors='C0', alpha=0.5, zorder=1, linewidths=3)
    # plot stream plot
    ax.streamplot(X[1:, 1:], Y[1:, 1:], U, V, color='C1', zorder=2)

plt.show()
