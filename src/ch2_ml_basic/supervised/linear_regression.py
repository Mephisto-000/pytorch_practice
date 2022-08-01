from turtle import color
from matplotlib import projections
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def generate_data(n=50):
    np.random.seed(1)
    x_n = n     # data amount
    x_min = 16
    x_max = 30
    bounded = [x_min, x_max]

    x_age = 17 + 13*np.random.rand(x_n)  # 16~30 age
    x_age = np.sort(np.round(x_age, 2))

    para = [170, 108, 0.2]
    y_tall = para[0] - para[1]*np.exp(-para[2]*x_age) + 5*np.random.rand(x_n)
    y_tall = np.round(y_tall, 2)

    return x_age, y_tall, bounded


def mse_line(x, y, w):
    """
    :param x: age data
    :param y: tall data
    :param w: weights
    """
    y_line = w[0]*x + w[1]
    mse = np.mean((y_line - y)**2)

    return mse


def plot_generate_data(x, y, bounded):
    plt.style.use("ggplot")
    plt.figure(figsize=(5, 5))
    plt.plot(x, y, "o", color="red", markersize=12)
    plt.xlim(bounded[0], bounded[1])
    plt.xlabel("X (age, unit:year)", fontsize=25)
    plt.ylabel("Y (tall, unit:cm)", fontsize=25)
    plt.show()


def plot_mse_3d(ww0, ww1, J):
    plt.figure(figsize=(9.5, 4))
    plt.subplots_adjust(wspace=0.5)

    ax = plt.subplot(1, 2, 1, projection="3d")
    ax.plot_surface(ww0, ww1, J, rstride=10, cstride=10, alpha=0.3, 
                    color="blue", edgecolor="black")
    ax.set_xticks([-20, 20])
    ax.set_yticks([120, 140, 160])
    ax.set_xlabel("$w_{0}$", fontsize=15)
    ax.set_ylabel("$w_{1}$", fontsize=15)
    ax.view_init(20, -60)

    plt.subplot(1, 2, 2)
    cont = plt.contour(ww0, ww1, J, 30, colors="black", 
                        levels=[100, 1000, 10000, 100000])
    cont.clabel(fmt="%d", fontsize=8)
    plt.xlabel("$w_{0}$", fontsize=15)
    plt.ylabel("$w_{1}$", fontsize=15)
    plt.grid()
    plt.show()



def main():
    x, y, bounded = generate_data()
    plot_generate_data(x, y, bounded)

    xn = 100  # 等高線解析度
    w0 = np.linspace(-25, 25, xn)
    w1 = np.linspace(120, 170, xn)
    ww0, ww1 = np.meshgrid(w0, w1)
    J = np.zeros((len(w0), len(w1)))
    for i0 in range(len(w0)):
        for i1 in range(len(w1)):
            J[i1, i0] = mse_line(x, y, (w0[i0], w1[i1]))
    plot_mse_3d(ww0, ww1, J)

    


if __name__ == "__main__":
    main()
