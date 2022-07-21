import numpy as np
import matplotlib.pyplot as plt


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
    plt.plot(x, y, "--o", color="red", markersize=12)
    plt.xlim(bounded[0], bounded[1])
    plt.xlabel("X (age, unit:year)", fontsize=25)
    plt.ylabel("Y (tall, unit:cm)", fontsize=25)
    plt.show()


def main():
    x, y, bounded = generate_data()
    plot_generate_data(x, y, bounded)


if __name__ == "__main__":
    main()
