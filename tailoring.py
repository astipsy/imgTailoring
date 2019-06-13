import math
import os
from PIL import Image

# 打开图片
pil_img = Image.open('./test.jpg')

# 创建文件夹
if os.path.exists('./img/') == False:
    os.makedirs('./img/')

# 图片裁剪的尺寸
width = 180
height = 180

# 原图尺寸
img_size = pil_img.size

# 计算新图片尺寸
if (img_size[0] - width) > (img_size[1] - height):
    new_size = int(height / img_size[1] * img_size[0])
    # 等比缩放后的尺寸
    resize_arr = (new_size, height)
    coordinate = math.ceil((new_size - width) / 2)
    # 裁剪的数据
    crop_arr = (coordinate, 0, coordinate + width, height)
else:
    new_size = int(width / img_size[0] * img_size[1])
    # 等比缩放后的尺寸
    resize_arr = (width, new_size)
    coordinate = math.ceil((new_size - height) / 2)
    # 裁剪的数据
    crop_arr = (0, coordinate, width, coordinate + height)

# 等比缩放图片 将图片缩放到与需要裁剪的尺寸相近的大小
pil_img = pil_img.resize(resize_arr, Image.ANTIALIAS)
# 裁剪图片
pil_img = pil_img.crop(crop_arr)
# 保存新图片
pil_img.save('./img/crop1.jpg')