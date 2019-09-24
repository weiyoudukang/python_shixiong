# coding=utf-8
"""
国庆马上到了,做一个合成头像的小程序.

:作者:
    0o唯有杜康o0 -- 来源于公众号【师兄带你学Python】
:使用方法:
    1. 玩家通过交互界面输入自己头像的图片地址
    2. 玩家选择合成模版1(五星红旗)、2(70周年)、3(国庆快乐)
    3. 查看你的合成头像吧
"""
import os
import time
from PIL import Image


def combine_image(image, background_image):
    """
    合成两张图片

    :参数:
        * image                   待合成图片
        * backgroup_image         底图
        * combine_type            合成方式[lower_right|middle]
    :返回值:
        合成图片名称
    """
    result_image_name = "%s.jpg" % time.time()
    background_image = Image.open(background_image)
    image = Image.open(image)
    background_image.convert("L")
    background_image = background_image.convert("RGBA")
    image = image.resize((2000, 2000))
    r, g, b, a = background_image.split()
    image.paste(background_image, (0, 0), mask=a)
    image.show()
    image.save(result_image_name)
    return result_image_name


def main():
    print("#" * 60)
    print(__doc__)
    print("#" * 60)
    image = input(">>> 请输入您的头像地址: ").strip()
    while not os.path.exists(image):
        print("地址输错了吧,找不到啊~")
        image = input(">>> 请重新输入您的头像地址: ").strip()
    background_image_index = input(">>> 请选择合成模版编号: ").strip()
    while background_image_index not in ("1", "2", "3"):
        print("只能输入1-3的数字哦~")
        background_image_index = input(">>> 请选择合成模版编号: ").strip()
    background_image = "%s/%s.png" % (os.path.dirname(__file__), background_image_index)
    result_image_name = combine_image(image, background_image)
    print("合成头像保存到这里啦: %s/%s" % (os.path.dirname(__file__), result_image_name))


if __name__ == '__main__':
    main()
