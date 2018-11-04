# NeteasePlaylistBackup
仅适用于**windows**（小程序中播放列表路径是windows的）    
网易云播放列表    
* 歌曲备份（以文字形式）  
* 检测增删  
* 支持超过1000首。  
  
打开网易云客户端，进入需要备份的歌单，点击播放全部，歌曲进入播放列表，即可备份歌单。  
  
[NeteasePlaylistBackup(json)]（推荐使用json版）  
**use -b backup;use -c1 -c2 detect change**

optional arguments:  
  **-h**, --help            show this help message and exit  
  **-b**, --backup          backup playlist  
  **-bf** BACKUPF, --backupf BACKUPF  
                        backup playlist use appoint file  
  **-c1** COMPARE1, --compare1 COMPARE1  
                        need compare playlist 1  
  **-c2** COMPARE2, --compare2 COMPARE2  
                        need compare playlist 2    
                        

[NeteasePlaylistBackup(regex)]  
**usage: main.py [-h] [-b] [-c1 COMPARE1] [-c2 COMPARE2]**  
  
optional arguments:  
**-h**, --help            show this help message and exit  
**-b**, --backup          backup playlist  
**-c1** COMPARE1, --compare1 COMPARE1    
                        need compare playlist (.npy file) 1  
**-c2** COMPARE2, --compare2 COMPARE2    
                        need compare playlist (.npy file) 2 if not, use default platlist in netease directory

