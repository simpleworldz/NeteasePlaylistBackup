import json
import time
import os
import argparse

PATH_PLAYLIST = os.environ["localappdata"]+"/Netease/CloudMusic/webdata/file/queue"

def backup_queue(path):
    f = open(path,mode="r",encoding="UTF-8")
    data = f.read().encode("gbk","ignore").decode("gbk")
    data_dese = json.loads(data)   
    playlist_dic = {}
    index = 1
    '''{0} 待增加其他信息'''
    for item in data_dese:
        track = item["track"]
        name = track["name"]
        album_name = track["album"]["name"]
        artists = ""
        for artist in track["artists"]:
            artists += artist["name"] +"/"
        artists = artists[:-1]
        # playlist_dic[track["id"]] = track["name"]
        '''{0}对其后面再改进吧'''
        playlist_dic[track["id"]] = "index:{3:<8}name:{0}\talbum:{1}\tartists:{2}".format(name,album_name,artists,index)
        index += 1 
    print("playlist含{0}首歌".format(len(playlist_dic)))
    dumped_playlist_dic = json.dumps(playlist_dic)
    backup_save_name = "bk"+time.strftime("%Y%m%d%H%M%S",time.localtime())
    save_dic = open(backup_save_name,"w")
    save_dic.write(dumped_playlist_dic)
    save_dic.close()

def read_dic(path):
    f = open(path)
    return json.load(f)

def detect_change(path1,path2):
    playlist_dic1 = read_dic(path1)
    playlist_dic2 = read_dic(path2)
    print("playlistA:{0}首".format(len(playlist_dic1)))
    print("playlistB:{0}首".format(len(playlist_dic2)))
    key1,key2 = playlist_dic1.keys(),playlist_dic2.keys()
    remove = key1 - key2
    add = key2 - key1
    # print("{0} {1}".format(len(remove),len(add)))
    # print(remove)
    # print(add)
    change_save_name = "cg"+time.strftime("%Y%m%d%H%M%S",time.localtime())
    with open(change_save_name,"a") as a:
        a.write("remove:{0}\tadd:{1}\n".format(len(remove),len(add)))
        a.write("remove:\n")
        for key in remove:
            # a.write("id:{0:<10}\tname:{1}\n".format(key,playlist_dic1[key]))
            #print("id:{0}\tname:{1}\n".format(key,playlist_dic1[key]))
            a.write("id:{0:<10}\t{1}\n".format(key,playlist_dic1[key]))
        a.write("add:\n")
        for key in add:
            # a.write("id:{0:<10}\tname:{1}\n".format(key,playlist_dic2[key]))
            a.write("id:{0:<10}\t{1}\n".format(key,playlist_dic2[key]))
    print("change save in: "+change_save_name)

if __name__ == "__main__":

    parse = argparse.ArgumentParser(description="use -b backup;use -c1 -c2 detect change")
    parse.add_argument("-b","--backup",action='store_true',required=False,help="backup playlist")
    parse.add_argument("-bf","--backupf",type=str,required=False,help="backup playlist use appoint file")
    parse.add_argument("-c1","--compare1",type=str,required=False,help="need compare playlist  1")
    parse.add_argument("-c2","--compare2",type=str,required=False,help="need compare playlist  2")
    args = parse.parse_args()
    if args.backup:
        backup_queue(PATH_PLAYLIST)
    elif args.backupf:
        backup_queue(args.backupf)
    elif args.compare1 and args.compare2:
            detect_change(args.compare1,args.compare2)
    else:
        parse.print_help()  