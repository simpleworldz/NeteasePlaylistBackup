from tools.compare import compare
from tools.backup import backup
import numpy as np
import argparse
import sys
import os 

#backup_name = "tools/queue2"
backup_name = os.environ["localappdata"]+"/Netease/CloudMusic/webdata/file/queue"
compare_name1 = "bk20180804150831q1.npy"
compare_name2 = "bk20180804150846q2.npy"
def print_list(list1):
    list(map(print,list1))
def compare_main(compare_name1,compare_name2="",backup_name=""):
    #list_remove,list_add = compare(compare_name1)
    list_remove,list_add = compare(compare_name1,compare_name2,backup_name)

    print("减少歌曲："+ str(len(list_remove))+"首")
    '''
    理解下
    还有，传参不用 空格
    '''
    list_remove.sort(key=lambda x:x[0])
    list_add.sort(key=lambda x:x[0])
    print_list(list_remove)
    print("增加歌曲：{0}首".format(len(list_add)))
    print_list(list_add)
'''
list_addnp,list_removenp = np.array(list_add),np.array(list_remove)
print("remove_name:")
print(list_removenp[:,1])
print("add_name:")
print_list(list_addnp[:,1])
'''
if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    #只给了-b 没有参数内容呢？
    
    parse.add_argument("-b","--backup",action="store_true",required=False,help="backup playlist")
    parse.add_argument("-c1","--compare1",type=str,required=False,help="need compare playlist (.npy file) 1")
    parse.add_argument("-c2","--compare2",type=str,required=False,help="need compare playlist (.npy file) 2 if not, use default platlist in netease directory")
    args = parse.parse_args()
    if args.backup:
        backup(backup_name)
    elif args.compare1:
        if args.compare2:
            compare_main(args.compare1,compare_name2=args.compare2)
        else:
            compare_main(args.compare1,backup_name=backup_name)
    else:
        print("if first argument isn't '-b', '-c1' is must")   


