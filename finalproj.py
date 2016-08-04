

'''
def getFileExtList (dirPath,uniq=True,sorted=True):
    extList=list()
    for dirpath,dirnames,filenames in os.walk(dirPath):
        for file in filenames:
            fileExt=os.path.splitext(file)[-1]
            extList.append(fileExt)
 
    if uniq:
        extList=list(set(extList))
    if sorted:
        extList.sort()
    return extList

'''

"""
Write a program that takes as an argument the name of a directory (folder)
and then finds the extension of each file. Then, for each extension found,
it prints the number of files with that extension and the minimum, average,
and maximum size for files with that extension in the selected directory.

pseudo-code-

-DONE needs to accept directory name as input
-DONE needs to search entire computer for that directory and iterate through the
directory.
- needs to determine if object is file or folder with something maybe below

dirname = "c:\\"
f for f in os.listdir(dirname):
    if os.path.isfile(os.path.join)    #notcomplete from- http://www.diveintopython.net/file_handling/os_module.html

print os.path.splitext("/home/aa/bb/ff.html")[1]  #http://xahlee.info/perl-python/python_path_manipulation.html
gives # '.html'

"""

##run from command line with 'python finalproject.py <complete filepath>' 
##
##import os
##import sys
##from collections import Counter
##
##extlist = []
##path = sys.argv[1]
##
##def SearchExt():
##    for root, dirs, files in os.walk(path):
##        for name in files:
##            filepath = os.path.join(root, name)
##            size = os.stat(filepath).st_size
##            if len(os.path.splitext(filepath)[1]) < 2:
##                continue
##            extlist.append(os.path.splitext(filepath)[1])
##                
##    print(Counter(extlist))
##
##if __name__ == "__main__":
##   SearchExt()


'''
import os
import sys
from collections import Counter

path = sys.argv[1]
typesizeH = {}
typesize = {}
##extdict = {}
count = 0
extlist = []
try:
   for root, dirs, files in os.walk(path):
       for file in files:
          filepath = os.path.join(root, file)
##          size = os.stat(filepath).st_size
          if len(os.path.splitext(filepath)[1]) > 2:
              extlist.append(os.path.splitext(filepath)[1])

          prefix, extension = os.path.splitext(file)
          if extension not in typesize:
              typesize[extension] = 0
          typesize[extension] += os.stat(root + os.sep + file).st_size

except KeyboardInterrupt:
   pass


for key in typesize:
   typesizeH[key] = typesize[key]

##print(str(extension))

types = typesize.keys()
extdict = Counter(extlist)
extdictforkeys = dict(extdict)
##print("\n")
##print("{0} \n\n{1}".format(extdictforkeys.keys(), extdictforkeys.values()))
##print("\n")
for key, value in extdictforkeys.items():
   print(key, value)


print("Filetype\tSize")
for type in types:
   print("{0}\t{1}".format(type, typesizeH[type]))
'''


'''
simplified working version, no average count or anything yet

import os
import sys
from collections import Counter

path = sys.argv[1]
typesize = {}
count = 0
extlist = []
try:
   for root, dirs, files in os.walk(path):
       for file in files:
          filepath = os.path.join(root, file)

          if len(os.path.splitext(filepath)[1]) > 2:
              extlist.append(os.path.splitext(filepath)[1])

          prefix, extension = os.path.splitext(file)
          if extension not in typesize:
              typesize[extension] = 0
              typesize[extension] += os.stat(filepath).st_size

except KeyboardInterrupt:
   pass

types = typesize.keys()
extdict = Counter(extlist)
extdictforkeys = dict(extdict)

for key, value in extdictforkeys.items():
   print(key, value)

print("Filetype\tSize")
for type in types:
   print("{0}\t{1}".format(type, typesize[type]))


'''


#maybe make a list of dict so that each ext has its one dict with name, size, count
##for iframe in soup.find_all('iframe'):   http://stackoverflow.com/questions/11492656/create-list-of-dictionary-python
##    info = {
##        "src":    iframe.get('src'),
##        "height": iframe.get('height'),
##        "width":  iframe.get('width'),
##    }
##    content.append(info)
##http://chrisalbon.com/python/create_list_from_dictionary_keys_and_values.html

## so if i ahve a dict with extname and sizes, how can i add the count of those exts up and find
## average size of each ext
'''
>>> keys = ['a', 'b', 'c']
>>> values = [1, 2, 3]
>>> dictionary = dict(zip(keys, values))
>>> print dictionary
{'a': 1, 'b': 2, 'c': 3}
'''

##http://stackoverflow.com/questions/30720308/python-program-to-produce-dictionary-of-file-extensions-and-sizes

import os
import sys
from collections import Counter

path = sys.argv[1]
typesize = {}
count = 0
extlist = {}
exxtlist = []
try:
   for root, dirs, files in os.walk(path):
       for file in files:
          filepath = os.path.join(root, file)

          if len(os.path.splitext(filepath)[1]) > 1:
             count = 0
             extdick= {
                'extname': os.path.splitext(filepath)[1],
                'size': os.stat(filepath).st_size,
##                'count': (count +=1),
                }
             exxtlist.append(extdick)


             
##              extlist[os.path.splitext(filepath)[1]] = os.stat(filepath).st_size
##              print(extlist.items())

##          prefix, extension = os.path.splitext(file)
##          if extension not in typesize:
##              typesize[extension] = 0
##              typesize[extension] += os.stat(filepath).st_size

except KeyboardInterrupt:
   pass

types = typesize.keys()
extdict = Counter(extlist)
extdictforkeys = dict(extdict)

for key, value in extdictforkeys.items():
   print(key, value)

print("Filetype\tSize")
for type in types:
   print("{0}\t{1}".format(exxtlist.extdick['extname'], exxtlist.extdick['size']))


