from .backup import gain_music_list
import numpy as np 

'''还是用默认参数的方法吧'''
#def compare(compare_name1,*compare_name2):
def compare(compare_name1,compare_name2="",backup_name=""):
    """比较两个歌单list增删"""
    #不行
    #music_list2 = compare_name2 == ()?gain_music_list():np.load(compare_name2[0])
    #这个行 但是报错了你都不懂是哪里错的。。
    #music_list2 = gain_music_list(backup_name) if compare_name2 == () else np.load(compare_name2[0])
    if compare_name2 == "":
        music_list2 = gain_music_list(backup_name)
    else:
        music_list2 = np.load(compare_name2)
    music_list1 = np.load(compare_name1)
    print("listA:{0}首，listB:{1}首".format(len(music_list1),len(music_list2)))
    
    music_tuplelist1  = list(map(tuple,music_list1))
    music_tuplelist2  = list(map(tuple,music_list2))
    '''方法一'''
    #list_remove =  np.setdiff1d(music_list1,music_list2)
    #list_add = np.setdiff1d(music_list2,music_list1)
    '''方法二'''
    #list_remove = np.setdiff1d(music_list1[:,0],music_list2[:,0])
    #list_add = np.setdiff1d(music_list2[:,0],music_list1[:,0])
    '''方法三'''
    list_remove =list(diff(music_tuplelist1,music_tuplelist2))
    list_add = list(diff(music_tuplelist2,music_tuplelist1))
    list_remove1,list_add1 = [],[]
    #print([music_tuplelist1.index(list_remove[1])]+list(list_remove[1]))
    
    for x in range(0,len(list_remove)):
        list_remove1.append( [music_tuplelist1.index(list_remove[x])]+list(list_remove[x]))
    for x in range(0,len(list_add)):
        list_add1.append([music_tuplelist2.index(list_add[x])] + list(list_add[x]))
    
    return list_remove1,list_add1

def diff(listA,listB):
    "在listA中不在listB中"
    #return list(set(listA) - set(listB))
    return set(listA).difference(set(listB))



#compare("11")
