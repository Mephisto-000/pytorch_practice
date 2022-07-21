import torch


def make_tensor(gpu=False):
    device = "cpu"
    if gpu:
        device = "cuda:0"

    ones_tensor = torch.ones(5).to(device=device)  # five dimension, one axis, elements are all one.
    print("tensor of ones_tensor : \n", ones_tensor)
    print()
    zeros_tensor = torch.zeros(5).to(device=device)  # five dimension, one axis, elements are all zero.
    print("tensor of zeros_tensor : \n", zeros_tensor)
    print()
    multi_axis_tensor = torch.tensor([[2.5, 2.1],
                                      [3.0, 1.5],
                                      [55, 4.5]]).to(device=device)

    print("multi_axis_tensor : \n", multi_axis_tensor, "\n")
    print("multi_axis_tensor's shape : ", multi_axis_tensor.shape)
    print("Check multi_axis_tensor's (3, 1) element : ", multi_axis_tensor[2, 0])
    print("Check the multi_axis_tensor's second row elements : ", multi_axis_tensor[1, :])
    print("Check the multi_axis_tensor's first column elements : ", multi_axis_tensor[:, 0])
    print()
    ones_tensor_4by3 = torch.ones(4, 3).to(device=device)
    print("4 by 3 tensor and all elements are one : \n", ones_tensor_4by3)
    print()


def tensor_dtype(gpu=False):
    """
    1. torch.float or torch.float32
    2. torch.double or torch.float64
    3. torch.half or torch.float16
    4. torch.int8
    5. torch.unit8
    6. torch.short or torch.int16
    7. torch.int or torch.int32
    8. torch.long or torch.int64
    9. torch.bool

    """
    device = "cpu"
    if gpu:
        device = "cuda:0"

    test_ones_tensor = torch.ones(2, 3, dtype=torch.half).to(device=device)
    print("Define torch.float16 tensor : \n", test_ones_tensor)
    print("Check tensor type : ", test_ones_tensor.dtype)
    print()


if __name__ == "__main__":
    print("Check if GPU could be call : ", torch.cuda.is_available())
    print("GPU id : ", torch.cuda.current_device())
    print("GPU name : ", torch.cuda.get_device_name(0))
    print("===========================")
    make_tensor(gpu=False)  # Using GPU : gpu=True
    tensor_dtype(gpu=False)

