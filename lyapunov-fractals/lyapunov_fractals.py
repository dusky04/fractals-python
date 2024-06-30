import numpy as np
import matplotlib.pyplot as plt
from math import log

class LyapunovFractals:
    def __init__(self, seq,N, width:int = 500, height :int= 500):
        self._seq = seq
        self.N = N
        self.width = width
        self.height = height
        self.lf = None

    def select(self, a, b, i):
        return a if self._seq[i%len(self._seq)] == "A" else b

    def lyapunov(self, a, b, x0):
        lmb = 0.0
        x = x0
        for i in range(self.N):
            r = self.select(a, b, i)
            x = r * x * (1 - x)
            lmb += log(abs(r * (1 - 2 * x)))
        return lmb / self.N
    
    def get_lyapunov_fractal(self, x_min, x_max, y_min, y_max,x0 = 0.5):
        x = np.linspace(x_min,x_max,  self.width)
        y = np.linspace(y_min,y_max,  self.height)
        lf = np.zeros((len(x), len(y)))

        for i in range(len(x)):
            for j in range(len(y)):
                lf[i, j] = self.lyapunov(x[i], x[j], x0)
        self.lf = lf

    def show_lyapunov_fractal(self, cmap = "cubehelix", x_min=1, x_max=4, y_min=1, y_max=4):
        self.get_lyapunov_fractal(x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max)

        plt.figure(figsize=(8, 8))
        plt.imshow(self.lf, cmap=cmap) # type: ignore
        plt.tight_layout()
        plt.axis("off")
        plt.show()
        plt.close()

    def save_lyapunov_fractal(self, fname, cmap = "cubehelix"):
        plt.imsave(fname, arr=self.lf,cmap=cmap) # type: ignore
        print(f"Saving the image as {fname}")

