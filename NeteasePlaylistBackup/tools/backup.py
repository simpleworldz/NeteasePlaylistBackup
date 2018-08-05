import re
import numpy as np
import time

backup_save_name = "bk"+time.strftime("%Y%m%d%H%M%S",time.localtime())
def gain_music_list(backup_name):
    """获取music_list"""
    f = open(backup_name,mode = 'r',encoding = 'UTF-8')
    file1 = f.read()
    #https://blog.csdn.net/circle2015/article/details/52994042?locationNum=12&fps=1
    file1.replace(u'\xa0',u' ')
    '''及其耗时，还没输出的是[]'''
    #pattern = re.compile(r'"album".+?name:"(.+)".+?"name":"(.+)".+?"name":"(.+)","cd"')
    #pattern = re.compile('{"track".+?specialType')
    pattern = re.compile('{"track".+?popularity')
    results = pattern.findall(file1)
    '''没有结果 要print(list(res))这种情况才有输出'''
    #map(lambda x:print(x),results)
    #print(list(map(lambda x: x*2, [1,2,3])))
    
    res = map(gain_music_info,results)

    '''要有这一步(list)它才会执行，不然print也不执行'''
    music_list = np.array(list(res))
    #music_list2 = np.load("1.npy")
    #print(music_list2)
    f.close()
    return music_list

def backup(backup_name):
    """将music_list写入文件(backup)"""
    music_list = gain_music_list(backup_name)
    np.save(backup_save_name,music_list)
    print("备份成功！ 文件名： " + backup_save_name + ".npy")

def read_file_in_line():
    """已行读取文件"""
    pass
def gain_music_info(result):
    pattern = re.compile('"name":"(.+?)"')
    results = pattern.findall(result)
    #music_info = [results[2],results[1],results[0]]
    '''以为可能有多位作者'''
    len1 = len(results)
    artists = results[1]
    if len1 > 3:
        for x in range(2,len1 - 1):
            artists += "/" + results[x]
    music_info = [results[len1 - 1],artists,results[0]]
    return music_info
    
