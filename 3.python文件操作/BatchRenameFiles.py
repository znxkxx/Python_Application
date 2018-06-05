# encoding: utf-8
# ==============================================================================
# 需求描述
# ------------
# 实现遍历子文件夹，给每个子文件夹下的padf文件重命名，
#  增加一个数字编号，共计4位，0000-9999共10000个文件
# 
# ==============================================================================


import os 


def renamefile(mydir):
    for root, dir, files in os.walk(mydir, topdown=True):
     
        i = 0
        for file in files:
            # if file.find(".pdf")<=0 or file[:2]=='00' :
            if file.find(".txt")<=0 or file[:2]=='00' :
                continue
            i += 1
            new_file = '%03d_'%i + file
            os.rename(os.path.join(root,file), os.path.join(root,new_file))
        
        
def renamefile2(mydir) : 
    for root, dir, files in os.walk(mydir, topdown=True):
        for file in files:
            # if file.find(".pdf")<=0 or file[:2]=='00' :
            if file[:3]=='000' :
                new_file = file[3:]
                os.rename(os.path.join(root,file), os.path.join(root,new_file))
                
            
            
if  __name__ == "__main__":
    dir = "/Users/xinxu/Nustore Files/5.工作实习/5.知识准备/2.量化/7.金工研报"
    renamefile(dir)           


