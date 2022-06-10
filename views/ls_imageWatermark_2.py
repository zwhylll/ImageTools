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
from controllor.getfilename import SearchVideoFiles, getoutfileName, SearchFiles
from controllor.relog import wlog
from controllor.watermarkAdd import addWaterMark
# from lib.share import SI
from controllor.watermarkAdd import *
class Win_ls_Imagewatermark_2:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ls_ImageWaterMark_2.ui')
        self.ui.imageSelectBtn.clicked.connect(self.loadImage)
        self.ui.imageSelectBtn_2.clicked.connect(self.loadLogo)
        self.ui.compressBtn.clicked.connect(self.addwatermark)
        self.ui.outfileRoadBtn.clicked.connect(self.selectOutfileRoad)
        #self.ui.watermarkBtn.clicked.connect(self.viewwatermark)

    def loadImage(self):
        fname = QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")
        self.ui.fileRoadSelect.setText(fname)

        fname.encode('utf-8')
        self.ui.label.setScaledContents(True);
        # self.ui.label.setPixmap(QPixmap(fname.encode('utf-8')))
        return fname
    def loadLogo(self):
        fname, _ = QFileDialog.getOpenFileName(self.ui, '打开文件', '.', '图像文件(*.jpg *.png *.bmp)')
        self.ui.fileRoadSelect_2.setText(fname)

        #fname.encode('utf-8')
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
        addPicMark(infileName,outfileName,)

        #compressPicWH(infileName, outfileName, int(s2),int(s3))

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
        addWaterMark(infileName,outfileName,w,h,fontsize,text)
        self.ui.label.setScaledContents(True);
        self.ui.label.setPixmap(QPixmap(outfileName.encode('utf-8')))
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
        w = self.getwatermarkW()
        h = self.getwatermarkH()
        lut = float(self.ui.fontSizetext.text())
        #x=self.ui.waterx.text()
        #y = self.ui.watery.text()
        #text = self.getwatermarkText()
        #fontsize = self.getwatermarkFontSize()
        markroad = self.ui.fileRoadSelect_2.text()
        #addWaterMark(infileName,outfileName,w,h,fontsize,text)
        #addPicMark(infileName,outfileName,w,h,lut,markroad,x,y)
        #self.ui.label.setScaledContents(True);
        #self.ui.label.setPixmap(QPixmap(outfileName.encode('utf-8')))
        #from pathlib import Path
        #import os

        #my_file = Path(self.tmpfileName())
        #if(my_file.exists()):
            #os.remove(self.tmpfileName())
        imagetpye = self.ui.videoTypeBox.currentText()
        site = self.ui.siteBox.currentText()
        if(site == "左上"):
            realsite = "10:10"
        if(site == "正中"):
            realsite = "main_w/2-overlay_w/2:main_h/2-overlay_h/2"
        if(site == "右下"):
            realsite ="main_w-overlay_w-10:main_h-overlay_h-10"
        mes = self.ui.labelmes
        mes.setText("处理中，请稍等")
        QApplication.processEvents()

        road = self.ui.outfileRoadText.text()
        if (len(road) == 0 or len(infileName) == 0):
            self.msg2()
        else:
            wlog(infileName, outfileName, "图像批量图片水印")
            for filename in SearchFiles(infileName, imagetpye):
                print(filename)
                inf = infileName + "/" + filename
                print(inf)
                ouf = getoutfileName(outfileName, inf)
            # compressPicWH(inf, ouf, int(s2), int(s3))

                ls_addPicMark(inf,ouf,w,h,lut,markroad,realsite)
                QApplication.processEvents()
            self.msg1()
        mes.setText("没有任务")
    def msg1(self):
        # 使用infomation信息框
        QMessageBox.information(self.ui, "标题", "处理完毕", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    def msg2(self):
        # 使用infomation信息框
        QMessageBox.information(self.ui, "标题", "目录不能为空", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)







if __name__ == '__main__':
    app = QApplication([])
    main = Win_ls_Imagewatermark_2()
    main.ui.show()
    sys.exit(app.exec_())