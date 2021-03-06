#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-12-27
@author: ymy
Copyright ymyjohnny@gmail.com
'''
#创建图片，字体右对齐

from PIL import Image, ImageFont, ImageDraw

font_path = "/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-MI.ttf"
font = ImageFont.truetype(font_path, 20)

def draw_text(line, width, height=10000):
    im = Image.new("1", (width, height))
    draw = ImageDraw.Draw(im)
    #real_width = width-len(line)*2
    real_width = width  -   int(draw.textsize(line, font=font)[0])
    #print real_width
    draw.rectangle((0, 0, width, height), fill=255)
    draw.text((real_width, 0), line, fill=0, font=font)
    #定义字体高度 需要*1.2是为了给行留间距，+1是int以后会去除小数点，需要预留
    real_height = int(draw.textsize(line, font=font)[1] * 1.2) + 1
    
    #切图
    return im.crop((0, 0, width, real_height))

def main():
    im = draw_text('abc333333', 640)
    im.save('test-text.jpg')

if __name__ == '__main__': main()