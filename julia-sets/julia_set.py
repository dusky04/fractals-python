import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np


class JuliaSet:
    def __init__(self, f, c, height, width, max_iters=100):
        self._height = height
        self._width = width
        self.max_iters = max_iters
        self.js = None
        self.f = f
        self.c = c

    def get_julia_set(self, x_min=-1.8, x_max=1.8, y_min=-1.8, y_max=1.8):
        x = np.linspace(x_min, x_max, self._width)
        y = np.linspace(y_min, y_max, self._height)
        xs, ys = np.meshgrid(x, y)

        z = xs + ys * 1j

        julia_set = self.max_iters + np.zeros(z.shape)

        for i in range(self.max_iters):
            z = self.f(z, self.c)
            diverged = np.abs(z) >= 2
            div_now = diverged & (julia_set == self.max_iters)
            julia_set[div_now] = i
            z[div_now] = 2

        self.js = julia_set

    def show_julia_set(
        self,
        cmap="hot",
        x_min=-1.8,
        x_max=1.8,
        y_min=-1.8,
        y_max=1.8,
        extent=(-2, 2, -2, 2),
    ):
        self.get_julia_set(x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max)

        plt.figure(figsize=(8, 8))
        plt.imshow(self.js, cmap=cmap, extent=extent)  # type: ignore
        plt.tight_layout()
        plt.axis("off")
        plt.show()
        plt.close()

    def save_julia_set(self, fname, cmap="hot"):
        if list(self.js) == None:  # type: ignore
            self.get_julia_set()
        plt.imsave(fname=fname, arr=self.js, cmap=cmap)  # type: ignore
        print(f"Saving the image as {fname}")