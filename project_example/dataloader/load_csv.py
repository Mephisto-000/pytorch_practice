import csv
import numpy as np


def load_mnist_csv(f_csv, num_imgs):
    """
    讀取 csv 檔案，並輸出 numpy 資料型態圖片與標籤資料

    :param f_csv: csv 檔案名稱
    :param num_imgs: 讀取的張數
    :return: 標籤, 圖片資料
    """
    with open(f_csv, 'r') as f:
        data = np.empty((num_imgs, 28, 28), dtype=np.uint8)
        labels = np.empty(num_imgs, dtype=np.uint8)
        reader = csv.reader(f)

        for i, row in enumerate(reader):
            if i >= num_imgs:
                break  # 只讀取前 num_images 個圖像
            labels[i] = int(row[0])  # 第一個元素是標籤
            data[i] = np.array(row[1:], dtype=np.uint8).reshape(28, 28)  # 剩下的是圖像數據

    return labels, data
