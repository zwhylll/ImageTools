import sys
import os

# import unicode
from time import sleep

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMessageBox, QFileDialog
from PySide6.QtUiTools import QUiLoader
from controllor.CompressPicture import compressPic
# import requests
from controllor.CompressVideo import *
# from lib.share import SI
from controllor.relog import wlog
from controllor.videoSize import *
from controllor.getVideoInfo import *
class Win_VideoCompress:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('videocompress_1.ui')
        self.ui.imageSelectBtn.clicked.connect(self.loadImage)
        self.ui.compressBtn.clicked.connect(self.changemes)
        self.ui.outfileRoadBtn.clicked.connect(self.selectOutfileRoad)

    def loadImage(self):
        fname, _ = QFileDialog.getOpenFileName(self.ui, '打开文件', '.', '视频文件(*.mp4 *.avi *.wmv *.mpeg)')
        self.ui.fileRoadSelect.setText(fname)

        fname.encode('utf-8')
        #self.ui.label.setScaledContents(True);
        # self.ui.label.setPixmap(QPixmap(fname.encode('utf-8')))
        infileName = self.ui.fileRoadSelect.text()
        outfileName = self.outfileName()
        oldsize = getVideoFps_WH(infileName)
        fps = oldsize[0]
        wh = oldsize[1]
        bitrate = get_video_bitrate(infileName)
        self.ui.old_videoSizeText.setText(str(wh))
        self.ui.old_videoFps.setText(str(fps))
        self.ui.old_videoBitRate.setText(str(bitrate))
        return fname
    '''
    
    def getCompressLevel(self):
        compresslevel = self.ui.compresslevelBox.currentText()
        print(compresslevel)
        return int(compresslevel)
    '''
    def selectOutfileRoad(self):
        directory = QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        self.ui.outfileRoadText.setText(directory)
    # 压缩图片响应函数
    def changemes(self):
        mes = self.ui.labelmes
        mes.setText("处理中，请稍等")
        QApplication.processEvents()

        self.compressImage()
        mes.setText("处理完毕")

    def compressImage(self):
        #mes = self.ui.labelmes
        #mes.setText("处理中，请稍等")
        #print(mes.text())
        infileName = self.ui.fileRoadSelect.text()
        outfileName = self.outfileName()
        #self.mes()
        #oldsize = getDocSize(infileName)
        #self.ui.old_videoSizeText.setText(oldsize)
        newsize = self.ui.new_videoSizeText.text()
        fps = self.ui.new_videoFps.text()
        bit = self.ui.new_videoBitRate.text()
        vodec = self.ui.comboBox.currentText()
        road = self.ui.outfileRoadText.text()

        if (len(road) == 0 or len(infileName) == 0):
            self.msg2()
        else:

            #sleep(100)
            wlog(infileName, outfileName, "视频压缩")
            changeVideoSize(infileName,outfileName,str(newsize),str(fps),str(bit))
            newout = self.outfileName()
            changeVideoForm(outfileName,newout,vodec)
            from pathlib import Path
            import os

            my_file = Path(outfileName)
            if (my_file.exists()):
                os.remove(outfileName)
        #print(outfileName)
        # compresslevel = int(self.getCompressLevel())
        # compressPic(infileName,outfileName,compresslevel)
        # outfile =
            self.msg1()
        #self.ui.labelmes.setText("未开始处理")
    def msg1(self):
        # 使用infomation信息框
        QMessageBox.information(self.ui, "标题", "处理完毕", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    def msg2(self):
        # 使用infomation信息框
        QMessageBox.information(self.ui, "标题", "目录不能为空", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)






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

        # self.ui.btn_login.clicked.connect(self.onSignIn)
        # self.ui.edt_password.returnPressed.connect(self.onSignIn)
if __name__ == '__main__':
    app = QApplication([])
    main = Win_VideoCompress()
    main.ui.show()
    sys.exit(app.exec_())