import os
import cv2
import time

#videoPath=input("C:/Users/ASUS/Desktop/testVideo.mp4：")
# 将视频文件路径转化为标准的路径
def getVideoFps_WH(path=''):
    videoPath=path
# 视屏获取
    videoCapture=cv2.VideoCapture(videoPath)
# 帧率(frames per second)
    fps = int(videoCapture.get(cv2.CAP_PROP_FPS))
    print(fps)
# 总帧数(frames)
    frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    print(frames)
    frame_height =int( videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_width = int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(frame_width,frame_height)
    videoCapture.release()
    s=str(frame_width)+"*"+str(frame_height)
    a = (fps,s)
    return a


#图片存储地址：
'''
pathSave="C:/Users/ASUS/Desktop/out"
if(os.path.exists(pathSave)!=True):
    os.makedirs(pathSave)


#间隔多少帧取一张图片
skipNum=2  #注：间隔2帧取一个图；
count=0
f=open("C:/Users/ASUS/Desktop/out/"+"rgb.txt","w",encoding="utf-8")
f.write("# timestamp filename\n")
while (True):
    ret,frame=videoCapture.read()
    if(ret):
        if(count%(skipNum+1)==0):
            imgName="{:.6f}".format(time.time()+1.0*skipNum/fps-0.001*skipNum)
            imgPath=" rgb/"+imgName+ '.png'
            cv2.imwrite(pathSave + imgName + '.png', frame)
            f.write(imgName+imgPath+"\n")
        count+=1
#         cv2.waitKey(int(1.0*skipNum/fps*1000))
        cv2.waitKey(1)
#         time.sleep()
    else:
        print("视屏处理完毕！")
        break
'''
import ffmpeg

def get_video_bitrate(path):
    probe = ffmpeg.probe(path)
    #print(probe)  # 获取视频多媒体文件的信息
    format = probe['format']
    # print(format)
    bit_rate = format['bit_rate']
    #print(int(bit_rate)/1024)  # 单位 bps（每秒字节数）
    kbps = int(bit_rate) / 1024

    duration = format['duration']
    duration = int(float(duration))  # 时长（单位秒）

    #print(int(format['size']))  # 获取文件大小（单位字节）
    #print(int(int(probe['streams'][0]['r_frame_rate'].split('/')[0]) / int(
        #probe['streams'][0]['r_frame_rate'].split('/')[1])))  # 获取帧率

    # 通过比特率X时长/8 计算文件大小
    file_size = kbps * duration / 8
    #print(file_size)  # 得到文件的大小是 KB
    #print(file_size / 1024)  # 计算得到的数据
    #print(int(format['size']) / 1024 / 1024)  # 读取得到的数据
    return int(kbps)


if __name__ == '__main__':
    #compressPic('C:/Users/ASUS/Desktop/3JG6%5JF_ZE4[@]L~UYJCO2.png','C:/Users/ASUS/Desktop/out/out.png',10)
    print(getVideoFps_WH("C:/Users/ASUS/Desktop/testVideo.mp4"))
    print(get_video_bitrate("C:/Users/ASUS/Desktop/testVideo.mp4"))