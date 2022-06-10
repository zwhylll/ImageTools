from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

from views.DCT_water import Win_DCT
from views.LSB_water_main import Win_LSB_main
from views.fileSelect import Win_FileSelect
from views.compressImage_2 import Win_fileSelect_2
from views.imageCut import Win_imageCut
from views.imageWatermark import Win_watermark
from views.imagedown_water import Win_imagedown
from views.ls_imageWatermark import Win_ls_watermark
from views.ls_imageWatermark_2 import Win_ls_Imagewatermark_2
from views.ls_vdieoWatermark import Win_ls_Vwatermark
from views.ls_videoWatermark_2 import Win_ls_Videowatermark_2
from views.videoCompress import Win_VideoCompress
from views.videoWatermark import Win_Videowatermark
from views.ls_compressImage import Win_ls_imageCompress
from views.ls_videoCompress import Win_ls_VideoCompress
from views.cprImage_in import *
from views.ImageZoom import *
from views.imageWatermark_2 import *
# import requests
import PyQt5
# from lib.share import SI
from views.videoWatermark_2 import Win_Videowatermark_2
from views.LSB_water import *



class SI:
    mainWin = None
    #loginWin = None
    testWin = None
    compressImageWin = None
class Win_Login:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('login.ui')

        self.ui.btn_login.clicked.connect(self.onSignIn)
        self.ui.edt_password.returnPressed.connect(self.onSignIn)


    def onSignIn(self):
        username = self.ui.edt_username.text().strip()
        password = self.ui.edt_password.text().strip()


        SI.mainWin = Win_Main()
        SI.mainWin.ui.show()

        self.ui.edt_password.setText('')
        self.ui.hide()




class Win_Main :

    def __init__(self):
        self.ui = QUiLoader().load('main.ui')
        self.ui.actionExit.triggered.connect(self.onSignOut)
        # self.ui.treeWidget.setColumnCount(2)
        root = self.ui.treeWidget
        root.itemClicked.connect(self.ontestUi)
    def onSignOut(self):
        SI.mainWin.ui.hide()
        app = QApplication.instance()  # 获取QApplication对象
        app.quit()  # 退出应用
        #SI.loginWin.ui.show()
    def getTreeItem(self):
        itm = self.ui.treeWidget.currentItem()
        # print(itm.text(0))
        s = itm.text(0)
        return s
    def ontestUi(self):
        itm = self.ui.treeWidget.currentItem()
        # print (itm.text(0))
        s = itm.text(0)
        if(s == "图像压缩"):
            SI.testWin = Win_FileSelect()
            SI.testWin.ui.show()
        if(s == "图像压缩预设分辨率"):
            SI.testWin = Win_fileSelect_2()
            SI.testWin.ui.show()
        if(s == "图像裁剪"):
            SI.testWin = Win_imageCut()
            SI.testWin.ui.show()
        if(s== "图像水印"):
            SI.testWin = Win_watermark()
            SI.testWin.ui.show()
        if(s=="视频压缩"):
            SI.testWin = Win_VideoCompress()
            SI.testWin.ui.show()
        if(s=="视频水印"):
            SI.testWin = Win_Videowatermark()
            SI.testWin.ui.show()
        if (s == "图像批量压缩"):
            SI.testWin = Win_ls_imageCompress()
            SI.testWin.ui.show()
        if (s == "视频批量压缩"):
            SI.testWin = Win_ls_VideoCompress()
            SI.testWin.ui.show()
        if (s == "自定义分辨率(图像)"):
            SI.testWin = Win_fileSelect_3()
            SI.testWin.ui.show()
        if (s == "图像缩放"):
            SI.testWin = Win_ImageZoom()
            SI.testWin.ui.show()
        if (s == "图像水印(图片）"):
            SI.testWin = Win_watermark_2()
            SI.testWin.ui.show()
        if (s == "视频水印(图片)"):
            SI.testWin = Win_Videowatermark_2()
            SI.testWin.ui.show()
        if (s == "视频批量水印(图片)"):
            SI.testWin = Win_ls_Videowatermark_2()
            SI.testWin.ui.show()
        if (s == "图像批量水印(图片)"):
            SI.testWin = Win_ls_Imagewatermark_2()
            SI.testWin.ui.show()
        if (s == "图像批量水印(文字)"):
            SI.testWin = Win_ls_watermark()
            SI.testWin.ui.show()
        if (s == "视频批量水印(文字)"):
            SI.testWin = Win_ls_Vwatermark()
            SI.testWin.ui.show()
        if (s == "LSB水印算法"):
            SI.testWin = Win_LSB_main()
            SI.testWin.ui.show()
        if (s == "DCT水印算法"):
            SI.testWin = Win_DCT()
            SI.testWin.ui.show()





class Win_Test :

    def __init__(self):
        self.ui = QUiLoader().load('test.ui')
        #self.ui.actionExit.triggered.connect(self.onSignOut)
        # self.ui.treeWidget.setColumnCount(2)
        #root = self.ui.treeWidget
        #root.itemClicked.connect(self.onSignOut)
    def onSignOut(self):
        SI.mainWin.ui.hide()
        #SI.loginWin.ui.show()
app = QApplication([])
SI.mainWin = Win_Main()
SI.mainWin.ui.show()
app.exec_()