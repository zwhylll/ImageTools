def compressPic(infilename = '', outfilename='', compresslevel = 0):
    cmd_str = 'ffmpeg -i '+ '"'+infilename +'"'+ ' -q ' + str(compresslevel) +' '++ '"'+ outfilename+ '"'
    # print(cmd_str)
    run_cmd(cmd_str)
    # ffmpeg -i image_source -vf scale=width:height out_source
def compressPicWH(infilename = '', outfilename='', weight = -1, hight = -1):
    cmd_str = 'ffmpeg -i '  + '"'+infilename + '"'+ ' -vf scale=' +str(weight)+':'+ str(hight) + ' '  +'"'+outfilename+ '"'
    #print(cmd_str)
    run_cmd_Popen_PIPE(cmd_str)
def compressPicZoom(infilename = '', outfilename='', compresslevel = 0.00):
    cmd_str = 'ffmpeg -i ' + '"'+infilename + '"'+ ' -vf scale=iw*' + str(compresslevel) +':ih*'+ str(compresslevel)+' '+  '"'+outfilename+ '"'
    # print(cmd_str)
    run_cmd(cmd_str)
    #ffmpeg -i input.jpg -vf scale=iw*2:ih input_double_width.png
def run_cmd( cmd_str='', echo_print=1):
    """
    执行cmd命令，不显示执行过程中弹出的黑框
    备注：subprocess.run()函数会将本来打印到cmd上的内容打印到python执行界面上，所以避免了出现cmd弹出框的问题
    :param cmd_str: 执行的cmd命令
    :return:
    """
    from subprocess import run
    from subprocess import PIPE
    if echo_print == 1:
        print('\n执行cmd指令="{}"'.format(cmd_str))
    run(cmd_str, shell=True,stdout=PIPE)


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
    compressPic('C:/Users/ASUS/Desktop/hd iamge/out.jpg','C:/Users/ASUS/Desktop/out4.png',10)
    #compressPicWH('C:/Users/ASUS/Desktop/3JG6%5JF_ZE4[@]L~UYJCO2.png', 'C:/Users/ASUS/Desktop/out5.png', 960,450)
    #run_cmd('adb devices')
    #run_cmd_Popen_fileno('adb devices')
    #run_cmd_Popen_PIPE('adb devices')