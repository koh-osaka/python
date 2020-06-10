#coding:utf-8
import os

file_list=[]
for i in range(74):
    name=('adf40_ca#w%s.dat' %i)
    file_list.append(name)
 
    
#読み込むファイルをtext出力
new_dir_path=('matsu/ADF04/')
path = ('%s/file-name.txt' %new_dir_path)
os.makedirs(new_dir_path, exist_ok=True)
with open(path,mode='w') as f:
    for i in range(len(file_list)):
        f.write('%s\n' %file_list[i])
        
    
#print(file_list)