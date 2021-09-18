'''
# 1. 此软件用于微信批量添加表情包，为作者PeakofMountains开发，只用于学习，不可用于商用
# 3. 使用前请电脑端登录微信
# 4. 请将此文件放置在和图片文件夹同一目录下
# 5. image1.png是在文件传输助手里你自己头像的截图
# 6. 添加的过程中如果出现添加失败是因为微信对表情的单次添加数量有限制，重新运行一遍程序应该可以解决
# 7. 目录里的gifs这个文件夹会在代码执行的时候自行创建，也可以自己手动建立
'''
from PIL import Image
import os
import pyautogui
import time
import re
IMAGE_PATH = "images/"
GIF_PATH = "gifs/"


time.sleep(5)
pyautogui.FAILSAFE = False


def changeFormat():
    '''
    图片格式转换处理函数
    '''
    # 图片文件夹列表
    fileList = os.listdir(IMAGE_PATH)
    if(os.path.exists('gifs') == 0):
        os.mkdir('gifs')
    for imgname in fileList:
        im = Image.open(IMAGE_PATH+imgname)
        # 将jpg格式和png格式的图片转为gif格式，才能作为表情添加到微信
        if(re.search('jpg', imgname) != None):
            im.save(GIF_PATH+imgname.replace("jpg", "gif"))
        if(re.search('png', imgname) != None):
            im.save(GIF_PATH+imgname.replace("png", "gif"))


def sendAndSave():
    '''
    添加表情模块，匹配头像，移动鼠标，操作鼠标右键点击，匹配添加到表情菜单，点击添加到表情区域
    '''
    for i in range(5):
        image1 = pyautogui.locateAllOnScreen('image1.png')
        for i in image1:
            x, y = pyautogui.center(i)
            pyautogui.click(x-33, y, button='right')
            time.sleep(0.2)
            # image2 = pyautogui.locateAllOnScreen('image2.png')
            # z, r = pyautogui.center(image2)
            pyautogui.click(x-35, y+2)
        pyautogui.scroll(1000)
        time.sleep(1)


def main():
    '''
    主流程控制程序
    '''
    # 1. 文件转格式模块：读取当前目录images文件夹
    changeFormat()
    pyautogui.alert(
        text='图片格式转换完成！请在15秒内将gifs文件夹下的所有gif图片发送到微信\n\n', title='进度')
    # 2. 用户发送gif图片
    time.sleep(20)
    sendAndSave()
    # 3. 完成提醒
    pyautogui.alert(text='\t\t\t\t完成！\n\n', title='提示')


main()
