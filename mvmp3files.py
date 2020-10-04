import os
import shutil

abspath = os.path.abspath('.')

def mvclass(classname):
    idxname = os.path.join(abspath,classname+".txt")
    flist = os.listdir(abspath)
    with open(idxname,"r",encoding='UTF-8') as f:
        for mp3file in f.readlines():
            if len(mp3file)>10:
                mp3file=mp3file.strip()
                pos = mp3file.find("mp3")
                dirname = os.path.join(abspath,classname)
                filename = mp3file[:pos+3]
                if filename in flist:
                #dstfilename = os.path.join(dirname,filename)
                    shutil.move(filename,dirname)
                else:
                    print(classname)
                    print("----------"+filename)



cnt = 0
with open("classlist.txt","r",encoding='UTF-8') as clslist:
    for cls in clslist.readlines():
        clsname = cls.strip()[:-1]
        if os.path.isdir(os.path.join(abspath,clsname)) and os.path.isfile(clsname+'.txt'):
            #print("~"+clsname)
            cnt += 1
            mvclass(clsname)
        else:
            print(clsname)

print(cnt)


