import os

for root,dirs,files in os.walk('.',topdown=False):
    #print(root)
    #print(dirs)
    #print(files)
    for name in files:
        print(os.path.join(root,name))
    #for name in dirs:
        #print(os.path.join(root,name))


#print(os.walk('.',topdown=False))