from tkinter import *
from tkinter import filedialog
import tkinter.messagebox  # 弹窗库
from PIL import Image, ImageDraw, ImageFont, ImageTk
import code
import matplotlib
import matplotlib.pyplot as plt
import cv2
import shutil
import numpy as np
import itertools
from skimage import color
import math
import random
import os
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *

np.set_printoptions(suppress=True)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签

quant = np.array([[16, 11, 10, 16, 24, 40, 51, 61],  # QUANTIZATION TABLE
                  [12, 12, 14, 19, 26, 58, 60, 55],  # required for DCT
                  [14, 13, 16, 24, 40, 57, 69, 56],
                  [14, 17, 22, 29, 51, 87, 80, 62],
                  [18, 22, 37, 56, 68, 109, 103, 77],
                  [24, 35, 55, 64, 81, 104, 113, 92],
                  [49, 64, 78, 87, 103, 121, 120, 101],
                  [72, 92, 95, 98, 112, 100, 103, 99]])


def plus(str):
    return str.zfill(8)


# Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。

def get_key(strr):
    # 获取要隐藏的文件内容
    tmp = strr
    f = open(tmp, "rb")
    str = ""
    s = f.read()
    global text_len
    text_len = len(s)
    for i in range(len(s)):
        # code.interact(local=locals())
        str = str + plus(bin(s[i]).replace('0b', ''))
    # 逐个字节将要隐藏的文件内容转换为二进制，并拼接起来
    # 1.先用ord()函数将s的内容逐个转换为ascii码
    # 2.使用bin()函数将十进制的ascii码转换为二进制
    # 3.由于bin()函数转换二进制后，二进制字符串的前面会有"0b"来表示这个字符串是二进制形式，所以用replace()替换为空
    # 4.又由于ascii码转换二进制后是七位，而正常情况下每个字符由8位二进制组成，所以使用自定义函数plus将其填充为8位
    # print str
    f.closed
    return str


def mod(x, y):
    return x % y;


def toasc(strr):
    return int(strr, 2)


# q转换成第几行第几列
# width行height列
def q_converto_wh(q):
    w = q // 600
    h = q % 600
    return w, h


def swap(a, b):
    return b, a


def randinterval(m, n, count, key):
    # m,n = matrix.shape
    print(m, n)
    interval1 = int(m * n / count) + 1
    interval2 = interval1 - 2
    if interval2 == 0:
        print('载体太小，不能将秘密信息隐藏进去!')
    # print('interval1:', interval1)
    # print('interval2:', interval2)

    # 生成随机序列
    random.seed(key)
    a = [0] * count  # a是list
    for i in range(0, count):
        a[i] = random.random()

    # 初始化
    row = [0] * count
    col = [0] * count

    # 计算row和col
    r = 0
    c = 0
    row[0] = r
    col[0] = c
    for i in range(1, count):
        if a[i] >= 0.5:
            c = c + interval1
        else:
            c = c + interval2
        if c > n:
            k = c % n
            r = r + int((c - k) / n)
            if r > m:
                print('载体太小不能将秘密信息隐藏进去!')
            c = k
            if c == 0:
                c = 1
        row[i] = r
        col[i] = c

    return row, col

# str1为载体图片路径，str2为隐写文件，str3为加密图片保存的路径
def func_LSB_yinxie(infile, textfile, savefile):
    im = Image.open(infile)
    im = im.convert("RGB")



    #获取图片的宽和高
    global width,height
    width = im.size[0]
    print("width:" + str(width)+"\n")
    height = im.size[1]
    print("height:"+str(height)+"\n")
    count = 0
    #获取需要隐藏的信息
    key = get_key(textfile)
    print('key: ',key)
    keylen = len(key)
    print('keylen: ',keylen)


    for h in range(0,height):
        for w in range(0,width):
            pixel = im.getpixel((w,h))
            #code.interact(local=locals())

            a=pixel[0]
            b=pixel[1]
            c=pixel[2]
            if count == keylen:
                break
            #下面的操作是将信息隐藏进去
            #分别将每个像素点的RGB值余2，这样可以去掉最低位的值
            #再从需要隐藏的信息中取出一位，转换为整型
            #两值相加，就把信息隐藏起来了
            a= a-mod(a,2)+int(key[count])
            count+=1
            if count == keylen:
                im.putpixel((w,h),(a,b,c))
                break
            b =b-mod(b,2)+int(key[count])
            count+=1
            if count == keylen:
                im.putpixel((w,h),(a,b,c))
                break
            c= c-mod(c,2)+int(key[count])
            count+=1
            if count == keylen:
                im.putpixel((w,h),(a,b,c))
                break
            if count % 3 == 0:
                im.putpixel((w,h),(a,b,c))
    im.save(savefile)

    #tkinter.messagebox.showinfo('提示','图像隐写已完成,隐写后的图像保存为' + savefile)
# le为所要提取的信息的长度，str1为加密载体图片的路径，str2为提取文件的保存路径
def func_LSB_tiqu(le, str1, str2):
    a = ""
    b = ""
    im = Image.open(str1)
    im = im.convert("RGB")
    # lenth = le*8
    lenth = le
    width = im.size[0]
    height = im.size[1]
    count = 0
    for h in range(0, height):
        for w in range(0, width):
            # 获得(w,h)点像素的值
            pixel = im.getpixel((w, h))
            # 此处余3，依次从R、G、B三个颜色通道获得最低位的隐藏信息
            if count % 3 == 0:
                count += 1
                b = b + str((mod(int(pixel[0]), 2)))
                if count == lenth:
                    break
            if count % 3 == 1:
                count += 1
                b = b + str((mod(int(pixel[1]), 2)))
                if count == lenth:
                    break
            if count % 3 == 2:
                count += 1
                b = b + str((mod(int(pixel[2]), 2)))
                if count == lenth:
                    break
        if count == lenth:
            break

    print(b)
    tiqu = str2+'/LSB_recover.txt'

    with open(tiqu, "wb") as f:
        for i in range(0, len(b), 8):
            # 以每8位为一组二进制，转换为十进制
            stra = toasc(b[i:i + 8])
            # stra = b[i:i+8]
            # 将转换后的十进制数视为ascii码，再转换为字符串写入到文件中
            stra = chr(stra)
            sb = bytes(stra, encoding="utf8")
            # print(sb)
            # f.write(chr(stra))
            f.write(sb)
            stra = ""
    f.closed


def DCT_yinxie(infile,textfie,outfile):
    #tkinter.messagebox.showinfo('提示', '请选择要进行DCT隐写的图像')
    #Fpath = filedialog.askopenfilename()
    #shutil.copy(Fpath, './')

    #original_image_file = Fpath.split('/')[-1]
    # original_image_file是DCT_origin.bmp
    y = cv2.imread(infile, 0)

    row, col = y.shape
    row = int(row / 8)
    col = int(col / 8)

    y1 = y.astype(np.float32)
    Y = cv2.dct(y1)

    #tkinter.messagebox.showinfo('提示', '请选择要隐藏的信息(请选择txt文件)')
    #txtpath = filedialog.askopenfilename()
    #shutil.copy(txtpath, './')
    #tmp = txtpath.split('/')[-1]
    # tmp是hideInfo_DCT.txt

    msg = get_key(textfie)

    count = len(msg)
    print('count: ', count)
    k1, k2 = randinterval(row, col, count, 12)

    for i in range(0, count):
        k1[i] = (k1[i] - 1) * 8 + 1
        k2[i] = (k2[i] - 1) * 8 + 1

    # 信息嵌入
    temp = 0
    H = 1
    for i in range(0, count):
        if msg[i] == '0':
            if Y[k1[i] + 4, k2[i] + 1] > Y[k1[i] + 3, k2[i] + 2]:
                Y[k1[i] + 4, k2[i] + 1], Y[k1[i] + 3, k2[i] + 2] = swap(Y[k1[i] + 4, k2[i] + 1],
                                                                        Y[k1[i] + 3, k2[i] + 2])
        else:
            if Y[k1[i] + 4, k2[i] + 1] < Y[k1[i] + 3, k2[i] + 2]:
                Y[k1[i] + 4, k2[i] + 1], Y[k1[i] + 3, k2[i] + 2] = swap(Y[k1[i] + 4, k2[i] + 1],
                                                                        Y[k1[i] + 3, k2[i] + 2])

        if Y[k1[i] + 4, k2[i] + 1] > Y[k1[i] + 3, k2[i] + 2]:
            Y[k1[i] + 3, k2[i] + 2] = Y[k1[i] + 3, k2[i] + 2] - H  # 将小系数调整更小
        else:
            Y[k1[i] + 4, k2[i] + 1] = Y[k1[i] + 4, k2[i] + 1] - H

    y2 = cv2.idct(Y)

    global dct_encoded_image_file
    dct_encoded_image_file = outfile

    cv2.imwrite(dct_encoded_image_file, y2)

    old = cv2.imread(infile)
    new = cv2.imread(dct_encoded_image_file)

    #tkinter.messagebox.showinfo('提示', '图像隐写已完成,隐写后的图像保存为' + dct_encoded_image_file)
def DCT_tiqu(lent, infile, oufile):


    # print('le: ',le)
    count = int(lent)
    print('count: ',count)

    #tkinter.messagebox.showinfo('提示','请选择要进行DCT提取的图像')
    #Fpath=filedialog.askopenfilename()
    #dct_encoded_image_file = Fpath.split('/')[-1]

    dct_img = cv2.imread(infile,0)
    print(dct_img)
    y=dct_img
    y1 = y.astype(np.float32)
    Y = cv2.dct(y1)
    row,col = y.shape
    row = int(row/8)
    col = int(col/8)
    # count = 448
    k1,k2 = randinterval(row,col,count,12)
    for i in range(0,count):
        k1[i] = (k1[i]-1)*8+1
        k2[i] = (k2[i]-1)*8+1


    #准备提取并回写信息
    str2 = oufile+'/DCT_recover.txt'
    b = ""

    for i in range(0,count):
        if Y[k1[i]+4,k2[i]+1] < Y[k1[i]+3,k2[i]+2]:
            b=b+str('0')
            # print('msg[i]: ',0)
        else:
            b=b+str('1')
            # print('msg[i]: ',1)

    print(b)


    #tkinter.messagebox.showinfo('提示','请选择将提取信息保存的位置')
    #tiqu=filedialog.askdirectory()
    tiqu = oufile+'/DCT_hidden_text.txt'

    str2 = tiqu
    with open(str2,"wb") as f:
        for i in range(0, len(b), 8):
            #以每8位为一组二进制，转换为十进制
            stra = toasc(b[i:i+8])
            #stra = b[i:i+8]
            #将转换后的十进制数视为ascii码，再转换为字符串写入到文件中
            stra = chr(stra)
            sb = bytes(stra, encoding = "utf8")
            f.write(sb)
            stra =""
    f.closed

    #tkinter.messagebox.showinfo('提示','隐藏信息已提取,请查看DCT_hidden_text.txt')
# 图像降级改进
def Image1_yinxie(infile,logofile,outfile):
    #tkinter.messagebox.showinfo('提示', '请选择载体图像')
    #Fpath = filedialog.askopenfilename()

    #shutil.copy(Fpath, './')

    #beiyinxie_image = Fpath.split('/')[-1]

    #tkinter.messagebox.showinfo('提示', '请选择要隐写的图像')
    #Fpath = filedialog.askopenfilename()
    #shutil.copy(Fpath, './')
    #mark_image = Fpath.split('/')[-1]

    img = np.array(Image.open(infile))
    mark = np.array(Image.open(logofile))
    rows, cols, dims = mark.shape

    for i in range(0, dims):
        for j in range(0, rows * 2):
            for k in range(0, cols * 2):
                img[j, k, i] = img[j, k, i] & 252

    for i in range(0, dims):
        for j in range(0, rows):
            for k in range(0, cols):
                img[2 * j, 2 * k, i] = img[2 * j, 2 * k, i] + (mark[j, k, i] & 192) // 64
                img[2 * j, 2 * k + 1, i] = img[2 * j, 2 * k + 1, i] + (mark[j, k, i] & 48) // 16
                img[2 * j + 1, 2 * k, i] = img[2 * j + 1, 2 * k, i] + (mark[j, k, i] & 12) // 4
                img[2 * j + 1, 2 * k + 1, i] = img[2 * j + 1, 2 * k + 1, i] + (mark[j, k, i] & 3)
            # print(2*j+1,2*k+1)
    img = Image.fromarray(img)
    global new_image
    new_image = outfile

    img.save(new_image)

    #tkinter.messagebox.showinfo('提示', '图像隐写已完成,隐写后的图像保存为' + new_image)


def Image1_tiqu(infile,oufile):
    #tkinter.messagebox.showinfo('提示', '请选择要进行提取图片水印的图像')
    #Fpath = filedialog.askopenfilename()
    new_image = infile

    #tkinter.messagebox.showinfo('提示', '请选择将提取信息保存的位置')
    #tiqu = filedialog.askdirectory()

    #print(tiqu)
    tiqu = oufile + '/mark_get1.' + new_image[-3:]
    print(tiqu)

    imgwmark = np.array(Image.open(new_image))
    result = imgwmark
    rows, cols, dims = imgwmark.shape
    rows = rows // 2
    cols = cols // 2
    for i in range(0, dims):
        for j in range(0, rows * 2):
            for k in range(0, cols * 2):
                imgwmark[j, k, i] = imgwmark[j, k, i] & 3

    for i in range(0, dims):
        for j in range(0, rows):
            for k in range(0, cols):
                result[j, k, i] = imgwmark[2 * j, 2 * k, i] * 64 + imgwmark[2 * j, 2 * k + 1, i] * 16
                +imgwmark[2 * j + 1, 2 * k, i] * 4 + imgwmark[2 * j + 1, 2 * k + 1, i]
    mark_get = Image.fromarray(result)
    mark_get.save(tiqu)

    #tkinter.messagebox.showinfo('提示', '水印图片已提取,请查看mark_get1.' + new_image[-3:])


