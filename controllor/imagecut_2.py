import cv2
def imaCut(infile,outfile):
    img = infile
    img = cv2.imread(img)
    #cv2.namedWindow("Enter to confirm", cv2.WINDOW_NORMAL)
    #cv2.resizeWindow("Enter to confirm", 400, 300)
    #cv2.imshow('Enter to confirm', img)

# 选择ROI
    roi = cv2.selectROI(windowName="Enter to confirm", img=img, showCrosshair=False, fromCenter=False)
    x, y, w, h = roi
    print(roi)

# 显示ROI并保存图片
    if roi != (0, 0, 0, 0):
        crop = img[y:y+h, x:x+w]
        #cv2.imshow('crop', crop)
        cv2.imwrite(outfile, crop)
        print('Saved!')

# 退出
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    imaCut("E:/Pypoject/vesOne/result.jpg","C:/Users/ASUS/Desktop/iou.jpg")
