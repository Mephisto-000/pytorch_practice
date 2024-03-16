import os
import converter, load_csv, plot_check


pre_path = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
train_set_path = os.path.join(pre_path, "MNIST_ORG", "train-images.idx3-ubyte")
train_set_lab_path = os.path.join(pre_path, "MNIST_ORG", "train-labels.idx1-ubyte")



if __name__ == '__main__':

    print(train_set_path)
    print(os.path.exists(train_set_path))

    # converter.convert(train_set_path, train_set_lab_path,
    #     "mnist_train.csv", 60000)

    labs, data = load_csv.load_mnist_csv(f_csv="mnist_train.csv", num_imgs=60000)

    print(data.shape)

    plot_check.plot_image(data[0])

    # f_name = 'mnist_train.csv'
    # labs, data = converter.load_mnist_csv(f_name, 10)
    # print(len(data))
    # print(type(data[0]))
    # print(data.shape)
    # print(labs)
    # converter.plot_image(data[0])


