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

# from lib.share import SI
from controllor.imagecut_2 import imaCut
from controllor.relog import wlog


class Win_imageCut:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('imageCut.ui')
        self.ui.imageSelectBtn.clicked.connect(self.loadImage)
        self.ui.compressBtn.clicked.connect(self.cutimage)
        self.ui.outfileRoadBtn.clicked.connect(self.selectOutfileRoad)

    def loadImage(self):
        fname, _ = QFileDialog.getOpenFileName(self.ui, '打开文件', '.', '图像文件(*.jpg *.png)')
        self.ui.fileRoadSelect.setText(fname)

        fname.encode('utf-8')
        self.ui.label.setScaledContents(True);
        self.ui.label.setPixmap(QPixmap(fname.encode('utf-8')))
        return fname

    def getCompressResolution(self):
        compressL = self.ui.LText_2.text()
        compressW = self.ui.WText_2.text()
        result = compressL + "*" + compressW
        return result
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
    def cutimage(self):
        path = self.ui.fileRoadSelect.text()
        '''
        src = cv.imread(path)
        src_copy = src.copy()
        points = get_points(src)
        print(points)
        print(points[0][1])
        y0 = points[0][1]
        y1 = points[1][1]
        x0 = points[0][0]
        x1 = points[1][0]
        crop_img = src_copy[y0:y1, x0:x1]
        output_file = self.outfileName()

        cv.imwrite(output_file, crop_img)
        infileName = output_file
        outfileName = self.outnewfileName()
        print(infileName)
        print(outfileName)
        '''
        output_file = self.outfileName()
        road = self.ui.outfileRoadText.text()
        if (len(road) == 0 or len(path) == 0):
            self.msg1("目录不能为空")
        else:

            imaCut(path,output_file)


            compresslevel = self.getCompressResolution()

            s2 = compresslevel.split("*")[0]
            s3 = compresslevel.split("*")[-1]
        # outfile =
        #self.msg1("裁剪成功")
            outfileName = self.outnewfileName()

            compressPicWH(output_file, outfileName, int(s2), int(s3))
            wlog(path, outfileName, "图像裁剪")

            self.msg1("裁剪成功")

        # self.ui.btn_login.clicked.connect(self.onSignIn)
        # self.ui.edt_password.returnPressed.connect(self.onSignIn)

    def msg1(self,message):
        # 使用infomation信息框
        QMessageBox.information(self.ui, "标题", message, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    #
    def outnewfileName(self):
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
        s5 = self.ui.formImageBox_2.currentText()
        if s5=="原格式":
            s4 = s2 + s1 +'.'+ s3
        else:
            s4 = s2 + s1 +s5

        result = self.ui.outfileRoadText.text() + "/" +s4
        return (result)
if __name__ == '__main__':
    app = QApplication([])
    main = Win_imageCut()
    main.ui.show()
    sys.exit(app.exec_())