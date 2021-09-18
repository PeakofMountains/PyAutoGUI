from PIL import Image
import os
Image_PATH = "images/"
GIF_PATH = "gifs/"


def changeFormat():
    # 图片文件夹列表
    fileList = os.listdir(Image_PATH)
    for imgname in fileList:
        im = Image.open(Image_PATH+imgname)
        # 将jpg格式和png格式的图片转为gif格式，才能作为表情添加到微信
        im.save(GIF_PATH+imgname.replace("jpg", "gif"))
        im.save(GIF_PATH+imgname.replace("png", "gif"))


# changeFormat()
