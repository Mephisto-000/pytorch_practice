from logging import critical
import os
from pickletools import optimize
import torch
import matplotlib.pyplot as plt
from torch import nn
from torch.utils.data import DataLoader, random_split
from torchmetrics import Accuracy
from torchvision import transforms
from torchvision.datasets import MNIST
from torchinfo import summary


def parameters_setting():
    PATH_DATASETS = os.path.join(os.getcwd(), "mnist_data")
    os.makedirs(PATH_DATASETS, exist_ok=True)
    BATCH_SIZE = 1024
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("cuda" if torch.cuda.is_available() else "cpu")

    return BATCH_SIZE, PATH_DATASETS, device


def data_prepare(data_path):
    training_data = MNIST(data_path, 
                          train=True, download=True, 
                          transform=transforms.ToTensor())
    testing_data = MNIST(data_path, 
                         train=False, download=True, 
                         transform=transforms.ToTensor())
    
    print("Dimension of Training data and Testing data : \n", 
            training_data.data.shape, testing_data.data.shape)
    
    return training_data, testing_data


def check_data_number(data_set, target_index):
    print(f"MNIST's data number 0~{target_index} : ", data_set.targets[:target_index])


def check_data_number_img_v1(data_set, target_index):
    print(f"{target_index}'s Image : \n", data_set.data[target_index])


def check_data_number_img_v2(data_set, target_index):
    img = data_set.data[target_index]
    plt.imshow(img.reshape(28, 28), cmap="gray")
    plt.axis("off")
    plt.show()


def check_data_number_01img(data_set, target_index):
    data = data_set.data[target_index].clone()
    data[data>0] = 1
    data = data.numpy()

    text_img = []
    for i in range(data.shape[0]):
        text_img.append("".join(data[i].astype(str)))
    
    print(f"{target_index}'s 01 image : \n", text_img)


def model_build(device):
    model = nn.Sequential(nn.Flatten(), 
                          nn.Linear(28*28, 256), 
                          nn.Dropout(0.2), 
                          nn.Linear(256, 10)).to(device)
    return model


def model_training(model, train_set, device, epochs, lr):
    train_loader = DataLoader(train_set, batch_size=600)
    optimizer = torch.optim.Adadelta(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()
    model.train()
    loss_list = []
    for epoch in range(1, epochs + 1):
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

            if batch_idx % 10 == 0:
                loss_list.append(loss.item())
                batch = batch_idx*len(data)
                data_count = len(train_loader.dataset)
                percentage = (100. * batch_idx / len(train_loader))
                print(f"Epoch {epoch}: [{batch:5d} / {data_count}] ({percentage:.0f} %)" + 
                      f"  Loss: {loss.item():.6f}")
    
    return model, loss_list


def plot_training_loss(loss_list):
    plt.style.use("ggplot")
    plt.plot(loss_list, "red")
    plt.title("Training Loss", fontsize=25)
    plt.show()


def model_testing(model, test_set, device, batch_size):
    test_loader = DataLoader(test_set, shuffle=False, batch_size=batch_size)
    model.eval()
    criterion = nn.CrossEntropyLoss()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)

            test_loss += criterion(output, target).item()

            pred = output.argmax(dim=1, keepdim=True)

            correct += pred.eq(target.view_as(pred)).sum().item()
    
    test_loss /= len(test_loader.dataset)

    data_count = len(test_loader.dataset)
    percentage = 100. * correct / data_count
    print(f"Average Loss: {test_loss:.4f}, Accuracy: {correct}/{data_count}" + 
          f" ({percentage:.0f}%)\n")
    
    return model


def main():
    os.system("clear")
    batch_size, data_path, device = parameters_setting()
    train_set, test_set = data_prepare(data_path)
    # check_data_number(train_set, 10)
    # check_data_number_img_v1(train_set, 0)
    # check_data_number_img_v2(train_set, 0)
    # check_data_number_01img(train_set, 1)

    model = model_build(device)
    model, loss_list = model_training(model, train_set, device, epochs=5, lr=0.1)
    # plot_training_loss(loss_list)

    model = model_testing(model, test_set, device, batch_size=batch_size)
    summary(model, (60000, 28, 28))
    













if __name__ == "__main__":
    main()
