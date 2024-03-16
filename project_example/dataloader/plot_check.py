import matplotlib.pyplot as plt


# 顯示圖像
def plot_image(image):
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()
