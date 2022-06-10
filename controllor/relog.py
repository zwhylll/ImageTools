def wlog(inf=" ",ouf=" ", op=" "):
    with open('log.txt', 'a',encoding='utf-8') as f:
        import datetime
        # 获取系统时间
        now = datetime.datetime.now()
        s = str(now)+"\t"+op+"\t"+inf+"\t"+ouf+"\n"
        f.writelines(s)
if __name__ == '__main__':
    wlog("1","2","2")
    wlog("1", "2", "3")