import sys
import os

# import unicode
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMessageBox, QFileDialog
from PySide6.QtUiTools import QUiLoader
from controllor.CompressPicture import compressPic
from controllor.CompressPicture import compressPicWH
from controllor.ImageCut import *
# import requests
from controllor.relog import wlog
from controllor.watermarkAdd import addWaterMark
# from lib.share import SI
from controllor.waterLib import *
class Win_watermark_LSB_tiqu:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('imageWatermark_LSB_tiqu.ui')
        self.ui.imageSelectBtn.clicked.connect(self.loadImage)
        #self.ui.imageSelectBtn_2.clicked.connect(self.loadImage_text)
        self.ui.compressBtn.clicked.connect(self.compressImage)
        self.ui.outfileRoadBtn.clicked.connect(self.selectOutfileRoad)
        #self.ui.watermarkBtn.clicked.connect(self.viewwatermark)

    def loadImage(self):
        fname, _ = QFileDialog.getOpenFileName(self.ui, '打开文件', '.', '图像文件(*.jpg *.png *.bmp)')
        self.ui.fileRoadSelect.setText(fname)

        fname.encode('utf-8')
        #self.ui.label.setScaledContents(True);
        # self.ui.label.setPixmap(QPixmap(fname.encode('utf-8')))
        return fname

    def loadImage_text(self):
        fname, _ = QFileDialog.getOpenFileName(self.ui, '打开文件', '.', '文本文件(*.txt)')
        self.ui.fileRoadSelect_2.setText(fname)

        fname.encode('utf-8')
        #self.ui.label.setScaledContents(True);
        # self.ui.label.setPixmap(QPixmap(fname.encode('utf-8')))
        return fname

    def selectOutfileRoad(self):
        directory = QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        self.ui.outfileRoadText.setText(directory)
    # 压缩图片响应函数
    def compressImage(self):
        infileName = self.ui.fileRoadSelect.text()
        #textfileName = self.ui.fileRoadSelect_2.text()
        outfileName = self.ui.outfileRoadText.text()
        print(infileName)
        print(outfileName)
        #compresslevel = self.getCompressResolution()


        #s2 = compresslevel.split("*")[0]
        #3 = compresslevel.split("*")[-1]
        # outfile =
        road = self.ui.outfileRoadText.text()
        if (len(road) == 0 or len(infileName) == 0):
            self.msg2()
        else:
            lens = int(self.ui.lineEdit.text())
            wlog(infileName, outfileName, "LSB文字水印提取")
            func_LSB_tiqu(lens,infileName,outfileName)

        #func_LSB_yinxie(infileName,textfileName,outfileName)
            self.msg1()

    # 获取输出文件名
    def outfileName(self):
        infileRoad = self.ui.fileRoadSelect.text()
        import datetime
        # 获取系统时间
        now = datetime.datetime.now()
        # 去掉空格和.
        s = str(now).replace(" ","")
        s1 = s.replace(".",":")
        s1 = s1.replace(":","")
        s1 = s1.replace("-", "")

        # print("当前系统日期和时间是: ")

        # print(s1)
        # 获取输入图片名
        outfileName = infileRoad.split("/")[-1]
        # 拼接成输出文件名
        s2 = outfileName.split(".")[0]
        s3 = outfileName.split(".")[-1]
        s4 = s2+s1+'.'+s3
        result = self.ui.outfileRoadText.text() + "/" +s4
        return (result)


    def msg1(self):
        # 使用infomation信息框
        QMessageBox.information(self.ui, "标题", "处理完毕", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    def msg2(self):
        # 使用infomation信息框
        QMessageBox.information(self.ui, "标题", "目录不能为空", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)





if __name__ == '__main__':
    app = QApplication([])
    main = Win_watermark_LSB_tiqu()
    main.ui.show()
    sys.exit(app.exec_())