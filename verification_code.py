import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter


class VerCode(object):
    def __init__(self):
        # 字体的位置
        self.font_path = 'tahomabd.ttf'
        # 验证码位数
        self.number = 4
        # 验证码图片宽、高
        self.size = (100, 30)
        # 宽和高
        self.width, self.height = self.size
        # 背景颜色，默认为白色
        self.bgcolor = (255, 255, 255)
        # 字体颜色，默认为蓝色
        self.fontcolor = (0, 0, 255)
        # 干扰线颜色。默认为红色
        self.linecolor = (255, 0, 0)
        # 是否加入干扰线
        self.draw_line = True
        # 加入干扰线条数的上下限
        self.line_number = 20
        # 大小写字母
        self.source = list(string.ascii_letters)
        # 创建图片
        self.image = Image.new('RGBA', (self.width, self.height), self.bgcolor)

    """随机生成字符串"""
    def gene_text(self):
        # 验证码种加入数字
        for index in range(10):
            self.source.append(str(index))
        code_str = ''.join(random.sample(self.source, self.number))
        return code_str

    """用来绘制干扰线"""
    def gene_line(self, draw, width, height):
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill=self.linecolor)

    """生成验证码"""
    def gene_code(self):
        # 验证码的字体
        font = ImageFont.truetype(self.font_path, 25)
        # 创建画笔
        draw = ImageDraw.Draw(self.image)
        # 生成字符串
        text = self.gene_text()
        print(text)
        font_width, font_height = font.getsize(text)
        # 填充字符串
        draw.text(((self.width - font_width) / self.number, (self.height - font_height) / self.number),
                  text, font=font, fill=self.fontcolor)
        if self.draw_line:
            for i in range(self.line_number):
                self.gene_line(draw, self.width, self.height)

    def effect(self):
        # 创建扭曲
        self.image = self.image.transform((self.width + 20, self.height + 10),
                                          Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0), Image.BILINEAR)
        # 滤镜，边界加强
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        # 保存验证码图片
        self.image.save('validateCodePic.png')
        # self.image.show()


if __name__ == "__main__":
    # 进行封装
    vco = VerCode()
    vco.gene_code()
    vco.effect()
