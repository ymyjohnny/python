#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-12-27
@author: ymy
Copyright ymyjohnny@gmail.com
'''

from PIL import Image, ImageFont, ImageDraw

font_path = "/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-MI.ttf"
font = ImageFont.truetype(font_path, 20)

def getlines(draw, text, width):
    while text:
        for i in xrange(1, len(text) + 1):
            if text[i - 1] == "\n": break
            rect = draw.textsize(text[:i], font=font)
            if rect[0] > width: i -= 1; break
        yield text[:i]
        text = text[i:].rstrip('\r\n')

def render_img(content, width=640):
    #生成空白图片
    img = Image.new("1", (width, 10000))
    draw = ImageDraw.Draw(img)
    #用白色填满
    draw.rectangle((0, 0, width, 10000), fill=255)

    start_point = 0
    for line in getlines(draw, content.replace("\t", "    "), width):
        draw.text((0, start_point), line, fill=0, font=font)
        start_point += draw.textsize(line, font=font)[1] * 1.2

    return img.crop((0, 0, width, int(start_point) + 1))

def main():
    im = render_img('abc\ndef\ng')
    im.save('test-text1.png', "png")

if __name__ == '__main__': main()