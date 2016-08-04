import os
import sys
path = sys.argv[1]


for root, dirs, files in os.walk(path):
        contents={}
        for name in files:
            size=os.path.getsize(root+ os.sep +name)
            title, extension=os.path.splitext(name)
            if extension not in contents:
                contents[extension]=[1, size, size, size]
            else:
                contents[extension][0]=contents[extension][0]+1
                contents[extension][3]=contents[extension][3]+size
                if size>=contents[extension][1]:
                    contents[extension][1]=size
                elif size<contents[extension][2]:
                    contents[extension][2]=size
        contents[extension][3]=contents[extension][3]/contents[extension][0]
        print(contents)
