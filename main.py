# -*- coding=utf-8 -*-
from PIL import Image
import argparse


class Pic2str:
    def __init__(self, img_file, w, h):
        """
        初始化
        :param img_file: 输入图片路径
        :param w: 宽度
        :param h: 高度
        """
        self.img_file = img_file
        self.width = w
        self.height = h
        self.ascii_char = list("B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
        self.im = self.open_file()

    def open_file(self):
        """
        根据 width 和 height 打开图片
        :return: im 对象
        """
        im = Image.open(self.img_file)
        # 输出低质量图片
        im = im.resize((self.width, self.height), Image.NEAREST)
        return im

    def pic2char(self, r, g, b, alpha=256):
        """
        根据像素深度转为字符
        :param r: r
        :param g: g
        :param b: b
        :param alpha: 透明度
        :return: 按灰度转换后的字符
        """
        # 透明返回空字符
        if alpha == 0:
            return ' '

        char_length = len(self.ascii_char)
        # RGB 转为灰度值，灰度值范围：0-255
        gray = int(0.216 * r + 0.715 * g + 0.0722 * b)
        # 灰度值到下标映射
        unit = (256.0 + 1) / char_length
        return self.ascii_char[int(gray / unit)]

    def get_res(self):
        """
        获取结果
        :return: 结果字符串
        """
        string = ""
        for i in range(self.height):
            for j in range(self.width):
                string += self.pic2char(*self.im.getpixel((j, i)))
            string += "\n"
        # print(string)
        return string


if __name__ == '__main__':
    # 参数解析
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    # 输出文件路径
    parser.add_argument('-o', '--output')
    parser.add_argument('--width', type=int, default=80)
    parser.add_argument('--height', type=int, default=80)
    args = parser.parse_args()

    img = args.file
    width = args.width
    height = args.height
    output = args.output

    # 获取结果字串
    p2s = Pic2str(img, width, height)
    res = p2s.get_res()

    # 判断是否输出到文件
    if output:
        with open(output, 'w') as f:
            f.write(res)
    else:
        with open('output.txt', 'w') as f:
            f.write(res)