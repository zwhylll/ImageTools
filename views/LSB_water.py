from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
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
from views.imageWatermark_LSB import *
from views.imageWatermark_LSB_tiqu import *
# import requests
import PyQt5
# from lib.share import SI
from views.videoWatermark_2 import Win_Videowatermark_2


class newwin:
    #mainWin = Win_LSB()
    #loginWin = None
    testWin = None
    compressImageWin = None





class Win_LSB :

    def __init__(self):
        self.ui = QUiLoader().load('LSB_water.ui')
        #self.ui.actionExit.triggered.connect(self.onSignOut)
        # self.ui.treeWidget.setColumnCount(2)
        #root = self.ui.treeWidget
        #root.itemClicked.connect(self.ontestUi)
        self.ui.pushButton.clicked.connect(self.wirte_lsb)
        self.ui.pushButton_2.clicked.connect(self.get_lsb)
    def onSignOut(self):
        #SI.mainWin.ui.hide()
        app = QApplication.instance()  # 获取QApplication对象
        app.quit()  # 退出应用
        #SI.loginWin.ui.show()

    def wirte_lsb(self):
        newwin.testWin = Win_watermark_LSB()
        newwin.testWin.ui.show()
    def get_lsb(self):
        newwin.testWin = Win_watermark_LSB_tiqu()
        newwin.testWin.ui.show()






if __name__ == '__main__':
    app = QApplication([])
    main = Win_LSB()
    main.ui.show()
    sys.exit(app.exec_())