
def addWaterMark(infilename = '', outfilename='', weight = 0, hight = 0,lut=1.0,fontsize=50,text='',color="red"):
    # ffmpeg - i output.jpg - vf drawtext = "fontcolor=red:fontfile=simhei.ttf:fontsize=40:x=0:y=h-th:text='测试测试 2021-08-02" - y
    #output.jpg
    #ffmpeg - i C: / Users / ASUS / Desktop / infile / a.png - vf movie = filename = 'C\:\\Users\\ASUS\\Desktop\\water.png', scale = 100:100[watermark];
    #[ in][watermark]overlay = 10:10 C: / Users / ASUS / Desktop / outwe.jpg
    cmd_str = 'ffmpeg -i ' + '"'+infilename + '"'+ ' -vf drawtext="fontcolor='+str(color)+':alpha='+str(lut)+':fontfile=simhei.ttf:fontsize='+str(fontsize)+':x=W-tw-' \
              +str(weight)+':'+':y=H-th-'+ str(hight) + ':text='+text+'" -y ' + '"'+ outfilename+ '"'
    print(cmd_str)
    run_cmd(cmd_str)
def addPicMark(infilename = '', outfilename='', weight = 0, hight = 0,lut=1.0,markroad='',x=0,y=0):
    # ffmpeg - i output.jpg - vf drawtext = "fontcolor=red:fontfile=simhei.ttf:fontsize=40:x=0:y=h-th:text='测试测试 2021-08-02" - y
    #output.jpg
    #ffmpeg - i C: / Users / ASUS / Desktop / infile / a.png - vf movie = filename = 'C\:\\Users\\ASUS\\Desktop\\water.png', scale = 100:100[watermark];
    #[ in][watermark]overlay = 10:10 C: / Users / ASUS / Desktop / outwe.jpg
    s = markroad
    mg_path_str = "\\\\".join(s.split("/"))
    s1 = "\\:".join(mg_path_str.split(":"))
    cmd_str = 'ffmpeg -i ' + '"'+infilename+ '"'+ ' -vf movie=\''+s1+"\',scale="+str(weight)+":"+str(hight)+",lut=a=val*"+str(lut)+"[watermark];[in][watermark]overlay="+str(x)+":"+str(y)+" "+ '"'+outfilename+ '"'
    print(cmd_str)
    run_cmd(cmd_str)
def ls_addPicMark(infilename = '', outfilename='', weight = 0, hight = 0,lut=1.0,markroad='',site=" "):
    # ffmpeg - i output.jpg - vf drawtext = "fontcolor=red:fontfile=simhei.ttf:fontsize=40:x=0:y=h-th:text='测试测试 2021-08-02" - y
    #output.jpg
    #ffmpeg - i C: / Users / ASUS / Desktop / infile / a.png - vf movie = filename = 'C\:\\Users\\ASUS\\Desktop\\water.png', scale = 100:100[watermark];
    #[ in][watermark]overlay = 10:10 C: / Users / ASUS / Desktop / outwe.jpg
    s = markroad
    mg_path_str = "\\\\".join(s.split("/"))
    s1 = "\\:".join(mg_path_str.split(":"))
    cmd_str = 'ffmpeg -i ' + '"'+infilename+ '"'+ ' -vf movie=\''+s1+"\',scale="+str(weight)+":"+str(hight)+",lut=a=val*"+str(lut)+"[watermark];[in][watermark]overlay="+site+" "+ '"'+outfilename+ '"'
    print(cmd_str)
    run_cmd(cmd_str)
def ls_addWaterMark(infilename = '', outfilename='', weight = "0", hight = "0",lut=1.0,fontsize=50,text='',color = "red"):
    # ffmpeg - i output.jpg - vf drawtext = "fontcolor=red:fontfile=simhei.ttf:fontsize=40:x=0:y=h-th:text='测试测试 2021-08-02" - y
    #output.jpg
    #ffmpeg - i C: / Users / ASUS / Desktop / infile / a.png - vf movie = filename = 'C\:\\Users\\ASUS\\Desktop\\water.png', scale = 100:100[watermark];
    #[ in][watermark]overlay = 10:10 C: / Users / ASUS / Desktop / outwe.jpg
    cmd_str = 'ffmpeg -i ' + '"'+infilename+ '"' + ' -vf drawtext="fontcolor='+str(color)+':alpha='+str(lut)+':fontfile=simhei.ttf:fontsize='+str(fontsize)+':x=' \
              +str(weight)+''+':y='+ str(hight) + ':text='+text+'" -y '  + '"'+outfilename+ '"'
    print(cmd_str)
    run_cmd(cmd_str)

def run_cmd( cmd_str='', echo_print=1):
    """
    执行cmd命令，不显示执行过程中弹出的黑框
    备注：subprocess.run()函数会将本来打印到cmd上的内容打印到python执行界面上，所以避免了出现cmd弹出框的问题
    :param cmd_str: 执行的cmd命令
    :return:
    """
    from subprocess import run
    if echo_print == 1:
        print('\n执行cmd指令="{}"'.format(cmd_str))
    run(cmd_str, shell=True)


def run_cmd_Popen_fileno(cmd_string):
    """
    执行cmd命令，并得到执行后的返回值，python调试界面输出返回值
    :param cmd_string: cmd命令，如：'adb devices'
    :return:
    """
    import subprocess

    print('运行cmd指令：{}'.format(cmd_string))
    return subprocess.Popen(cmd_string, shell=True, stdout=None, stderr=None).wait()


def run_cmd_Popen_PIPE(cmd_string):
    """
    执行cmd命令，并得到执行后的返回值,python调试界面不输出返回值
    :param cmd_string: cmd命令，如：'adb devices"'
    :return:
    """
    import subprocess

    print('运行cmd指令：{}'.format(cmd_string))
    return \
    subprocess.Popen(cmd_string, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                     encoding='gbk').communicate()[0]


if __name__ == '__main__':
    #compressPic('C:/Users/ASUS/Desktop/3JG6%5JF_ZE4[@]L~UYJCO2.png','C:/Users/ASUS/Desktop/out/out.png',10)
    #addWaterMark('C:/Users/ASUS/Desktop/out.png', 'C:/Users/ASUS/Desktop/out/3.png', 0,0,50,'yy')
    addPicMark('C:/Users/ASUS/Desktop/infile/a.png','C:/Users/ASUS/Desktop/outfile/g3.png',150,150,0.5,'C:/Users/ASUS/Desktop/out.jpg',10,10)
    run_cmd('adb devices')
    run_cmd_Popen_fileno('adb devices')
    run_cmd_Popen_PIPE('adb devices')