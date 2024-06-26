import matplotlib.pyplot as plt
import numpy as np


class MandelbrotSet:
    def __init__(self, f, h: int, w: int, max_iters: int):
        self._height = h
        self._width = w
        self.max_iters = max_iters
        self.f = f
        self.ms = None

    def get_mandelbrot_set(self, x_min, y_min, x_max, y_max):
        ys, xs = np.ogrid[
            y_min : y_max : self._height * 1j, x_min : x_max : self._width * 1j
        ]
        c = xs + ys * 1j  # type: ignore
        z = c
        mandelbrot_set = self.max_iters + np.zeros(c.shape, dtype=int)

        for n_iter in range(self.max_iters):
            z = self.f(z, c)
            diverge = abs(z) >= 4
            div_now = diverge & (mandelbrot_set == self.max_iters)
            mandelbrot_set[div_now] = n_iter
            z[div_now] = 2
        self.ms = mandelbrot_set

    def display_mandelbrot_set(
        self,
        cmap="twilight_shifted",
        extent=(-2, 0.8, -1.4, 1.4),
        x_min=-2.0,
        y_min=-1.4,
        x_max=0.8,
        y_max=1.4,
    ):
        self.get_mandelbrot_set(x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max)

        plt.imshow(self.ms, cmap=cmap, extent=extent)  # type: ignore
        plt.axis(False)
        plt.title("Mandelbrot Set")
        plt.colorbar(label="Iteration count")
        plt.xlabel("Re(c)")
        plt.ylabel("Im(c)")
        plt.tight_layout()
        plt.show()