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
from controllor.getfilename import SearchFiles, getoutfileName
from controllor.relog import wlog
from controllor.watermarkAdd import addWaterMark, ls_addWaterMark


# from lib.share import SI

class Win_ls_watermark:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ls_imageWatermark.ui')
        self.ui.imageSelectBtn.clicked.connect(self.loadImage)
        self.ui.compressBtn.clicked.connect(self.addwatermark)
        self.ui.outfileRoadBtn.clicked.connect(self.selectOutfileRoad)
        #self.ui.watermarkBtn.clicked.connect(self.viewwatermark)

    def loadImage(self):
        fname = QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")
        self.ui.fileRoadSelect.setText(fname)

        fname.encode('utf-8')
        #self.ui.label.setScaledContents(True);
        # self.ui.label.setPixmap(QPixmap(fname.encode('utf-8')))
        return fname
    def getCompressResolution(self):
        compresslevel = self.ui.selectResolutionBox.currentText()
        print(compresslevel)
        return compresslevel
    def selectOutfileRoad(self):
        directory = QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        self.ui.outfileRoadText.setText(directory)
    # 压缩图片响应函数
    def compressImage(self):
        infileName = self.ui.fileRoadSelect.text()
        outfileName = self.outfileName()
        print(infileName)
        print(outfileName)
        compresslevel = self.getCompressResolution()


        s2 = compresslevel.split("*")[0]
        s3 = compresslevel.split("*")[-1]
        # outfile =

        compressPicWH(infileName, outfileName, int(s2),int(s3))

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
    def tmpfileName(self):
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
        s4 = 'tmp.'+s3
        result = self.ui.outfileRoadText.text() + "/" +s4
        return (result)


    def msg1(self):
        # 使用infomation信息框
        QMessageBox.information(self.ui, "标题", "裁剪成功", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    def getwatermarkW(self):
        w = self.ui.watermarkWtext.text()
        return w
        print(w)
    def getwatermarkH(self):
        h = self.ui.watermarkHtext.text()
        return h
        print(h)
    def getwatermarkText(self):
        text = self.ui.watermarkText.text()
        return text
        print(text)
    def getwatermarkFontSize(self):
        text = self.ui.fontSizetext.text()
        return text
        print(text)

    def viewwatermark(self):
        infileName = self.ui.fileRoadSelect.text()
        outfileName = self.tmpfileName()
        #print(infileName)
        #print(outfileName)
        #compresslevel = self.getCompressResolution()

        #s2 = compresslevel.split("*")[0]
        #s3 = compresslevel.split("*")[-1]
        # outfile =

        #compressPicWH(infileName, outfileName, int(s2), int(s3))
        w = self.getwatermarkW()
        h = self.getwatermarkH()
        text  = self.getwatermarkText()
        fontsize = self.getwatermarkFontSize()
        lut = self.ui.lut.text()
        addWaterMark(infileName,outfileName,w,h,float(lut),fontsize,text)

        self.ui.label.setScaledContents(True);
        self.ui.label.setPixmap(QPixmap(outfileName.encode('utf-8')))
        self.msg1()
    def msg1(self):
        # 使用infomation信息框
        QMessageBox.information(self.ui, "标题", "处理完毕", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    def msg2(self):
        # 使用infomation信息框
        QMessageBox.information(self.ui, "标题", "目录不能为空", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def addwatermark(self):
        infileName = self.ui.fileRoadSelect.text()
        outfileName = self.ui.outfileRoadText.text()
        #print(infileName)
        #print(outfileName)
        #compresslevel = self.getCompressResolution()

        #s2 = compresslevel.split("*")[0]
        #s3 = compresslevel.split("*")[-1]
        # outfile =

        #compressPicWH(infileName, outfileName, int(s2), int(s3))
        #w = self.getwatermarkW()
        #h = self.getwatermarkH()
        text  = self.getwatermarkText()
        fontsize = self.getwatermarkFontSize()
        lut = self.ui.lut.text()
        imagetpye = self.ui.videoTypeBox.currentText()
        site = self.ui.siteBox.currentText()

        if (site == "左上"):
            w="10"
            h="10"
        if (site == "正中"):
            w = "W/2"
            h=  "H/2"
        if (site == "右下"):
            w = "W-tw-10"
            h=  "H-th-10"

        color = self.ui.comboBox.currentText()
        road = self.ui.outfileRoadText.text()
        mes = self.ui.labelmes
        mes.setText("处理中，请稍等")
        QApplication.processEvents()
        if (len(road) == 0 or len(infileName) == 0):
            self.msg2()
        else:
            wlog(infileName, outfileName, "图像批量文字水印")

            for filename in SearchFiles(infileName, imagetpye):
                print(filename)
                inf = infileName + "/" + filename
                print(inf)
                print()
                ouf = getoutfileName(outfileName, inf)
                ls_addWaterMark(inf,ouf,w,h,float(lut),fontsize,text,color)
                QApplication.processEvents()
            self.msg1()
        mes.setText("没有任务")
        #self.ui.label.setScaledContents(True);
       # self.ui.label.setPixmap(QPixmap(outfileName.encode('utf-8')))






if __name__ == '__main__':
    app = QApplication([])
    main = Win_ls_watermark()
    main.ui.show()
    sys.exit(app.exec_())