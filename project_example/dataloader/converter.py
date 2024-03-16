def convert(img_f, label_f, out_f, n_imgs):
    """
    將二進位檔案資料轉換並儲存成 csv 檔案

    :param img_f: 二進位圖片資料檔案路徑
    :param label_f: 二進位圖片標籤檔案路徑
    :param out_f: 欲儲存的 csv 檔案名稱
    :param n_imgs: 圖片張數
    :return: None
    """
    # 打開圖像文件為二進制讀取模式
    f = open(img_f, "rb")
    # 打開輸出文件為寫入模式
    o = open(out_f, "w")
    # 打開標籤文件為二進制讀取模式
    lbl = open(label_f, "rb")

    # 跳過圖像文件和標籤文件的文件頭部分
    f.read(16) # 圖像文件頭
    lbl.read(8)  # 標籤文件頭
    images = []  # 初始化圖像列表

    # 讀取n個圖像和對應的標籤
    for i in range(n_imgs):
        # 讀取一個標籤，並將其ASCII值轉換為整數，存入image列表
        image = [ord(lbl.read(1))]
        # 讀取一個圖像（28x28像素），並將每個像素的ASCII值轉換為整數，追加到image列表
        for j in range(28*28):
            image.append(ord(f.read(1)))
        # 將轉換後的圖像（包含標籤和像素值）加入到images列表中
        images.append(image)

    # 將所有圖像和標籤寫入到CSV文件中，每個圖像一行
    for image in images:
        # 將每個圖像轉換為逗號分隔的字串，然後寫入文件
        o.write(",".join(str(pix) for pix in image)+"\n")
    # 關閉所有打開的文件
    f.close()
    o.close()
    lbl.close()
