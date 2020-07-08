
import os

__all__=['copy','add']

def copy(srcPath,targetPath):
    #复制srcPath的文件夹到targetPath中
    for i in os.listdir(srcPath):
        src=os.path.join(srcPath,str(i))
        target=os.path.join(targetPath,str(i))
        if os.path.isdir(src):
            os.mkdir(target)
            copy(src,target)
        else: 
            with open(src,'rb') as stream:
                with open(target,'wb') as stream2:
                    while True:
                        container = stream.readline()
                        if not container:
                            break
                        stream2.write(container)

def add(a,b):
    return a+b
