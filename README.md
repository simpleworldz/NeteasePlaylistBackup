# NeteasePlaylistBackup
网易云播放列表信息备份和检测增删（以文字形式），支持超过1000首。  

[NeteasePlaylistBackup(json)]  
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

