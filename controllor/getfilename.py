import os


def get_allfile(path):  # 获取所有文件
    all_file = []
    all_filename = []
    for f in os.listdir(path):  # listdir返回文件中所有目录
        f_name = os.path.join(path, f)
        print(f)
        all_filename.append(f)
        all_file.append(f_name)
    return all_filename

def SearchFiles(directory, fileType):
    fileList=[]
    namelist=[]
    if(fileType == "all"):
        for root, subDirs, files in os.walk(directory):
            for fileName in files:
                if fileName.endswith(".jpg")|fileName.endswith(".png")|fileName.endswith(".jpeg"):
                    fileList.append(os.path.join(root, fileName))
                    namelist.append(fileName)
    else:
        for root, subDirs, files in os.walk(directory):
            for fileName in files:
                if fileName.endswith(fileType):
                    fileList.append(os.path.join(root,fileName))
                    namelist.append(fileName)
    return namelist

def SearchVideoFiles(directory, fileType):
    fileList=[]
    namelist=[]
    if(fileType == "all"):
        for root, subDirs, files in os.walk(directory):
            for fileName in files:
                if fileName.endswith(".mp4")|fileName.endswith(".avi")|fileName.endswith(".mpeg"):
                    fileList.append(os.path.join(root, fileName))
                    namelist.append(fileName)
    else:
        for root, subDirs, files in os.walk(directory):
            for fileName in files:
                if fileName.endswith(fileType):
                    fileList.append(os.path.join(root,fileName))
                    namelist.append(fileName)
    return namelist

def getoutfileName(path,filename):
    infileRoad = filename
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
    result = path + "/" +s4
    return (result)
if __name__ == '__main__':
    all_file = get_allfile("C:/Users/ASUS/Desktop/out")  # tickets要获取文件夹名
    jpgfile = SearchFiles("C:/Users/ASUS/Desktop/out",'.jpg')
    outfile = getoutfileName("C:/Users/ASUS/Desktop/out","C:/Users/ASUS/Desktop/out.jpg")
    s = "C:/Users/ASUS/Desktop/out"
    mg_path_str="\\\\".join(s.split("/"))
    s1 = "\\:".join(mg_path_str.split(":"))
    print(s1)
    print(all_file)
    print(jpgfile)
    print(outfile)

