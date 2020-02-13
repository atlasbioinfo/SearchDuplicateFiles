from os import walk,path,mkdir
from hashlib import md5
from shutil import copy,move

def getMd5(fname):
    m = md5()
    with open(fname,'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()

if __name__ == '__main__':
    #默认把重复文件移动到这个文件夹，可以自定义名字
    #Default to move the duplicate file to this folder and can customize the name
    dupDir="Duplications"
    mkdir(dupDir)
    mdFile={}
    fileName={}
    for fpath,dirs,fs in walk('.'):
        for f in fs:
            tfile=path.join(fpath,f)
            if (path.samefile(fpath,dupDir)):
                continue
            tMD=getMd5(tfile)
            if (tMD in mdFile):
                mdFile[tMD]+=1
                if (len(f)>len(path.basename(fileName[tMD]))):
                    move(tfile,path.join(dupDir,path.splitext(f)[0]+str(mdFile[tMD])+path.splitext(f)[1]))
                    
                else:
                    tname=path.basename(fileName[tMD])
                    move(fileName[tMD],path.join(dupDir,path.splitext(tname)[0]+str(mdFile[tMD])+path.splitext(tname)[1]))
                    fileName[tMD]=tfile
                    
            else:
                mdFile[tMD]=1
                fileName[tMD]=tfile

