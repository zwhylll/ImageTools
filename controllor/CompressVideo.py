
def changeVideoSize(infilename = '', outfilename='', wh = '',fps = '',bit = ''):

    '''

    ffmpeg  -i  Desktop/input.mp4  -fs 10MB  Desktop/output.mp4
    -fs 10 : 表示文件大小最大值为10MB
    ffmpeg  -i  Desktop/input.mp4  -s 1920x1080  -b:v 1M  -r 20  Desktop/output.mp4
    '''
    cmd_str = 'ffmpeg -i '  + '"'+infilename + '"'+ ' -s '+str(wh) +' -b:v ' +str(bit)+"k"+" -bufsize "+str(bit)+"k"+" -r "+str(fps)+" "+ '"'+outfilename+ '"'
    print(cmd_str)
    run_cmd(cmd_str)
def changeVideoForm(infilename = '', outfilename='', vcodec = "h264"):

    '''

    ffmpeg  -i  Desktop/input.mp4  -fs 10MB  Desktop/output.mp4
    -fs 10 : 表示文件大小最大值为10MB
    ffmpeg  -i  Desktop/input.mp4  -s 1920x1080  -b:v 1M  -r 20  Desktop/output.mp4
    '''
    cmd_str = 'ffmpeg -i ' + '"'+ infilename+ '"' + ' -vcodec '+str(vcodec) +" "+ '"'+outfilename+ '"'
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
    changeVideoSize('C:/Users/ASUS/Desktop/out.png', 'C:/Users/ASUS/Desktop/out/3.png', '10MB')
    run_cmd('adb devices')
    run_cmd_Popen_fileno('adb devices')
    run_cmd_Popen_PIPE('adb devices')