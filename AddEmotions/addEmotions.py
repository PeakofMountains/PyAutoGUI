from pngTogif import changeFormat
import pyautogui
import time


pyautogui.FAILSAFE = False
time.sleep(5)
# 需求分析
# 1. 程序执行后弹出弹窗模块：给出程序说明，操作说明，版权说明

# 2. 文件转格式模块：读取当前目录images文件夹

# 3. 提示框模块，让用户发送一个图片，点击图片获取图片中心坐标

# 4. gif图片发送模块：将gifs文件夹中图片依次进行一下操作，复制到剪切板，点击输入框，粘贴，发送

# 5. 添加表情模块，鼠标移动到之前获取的图片的坐标位置，右键，移动，点击添加到表情区域

# 6. 重复4操作

# 7. 提示用户操作完成
