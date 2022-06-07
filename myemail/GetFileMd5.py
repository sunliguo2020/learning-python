import hashlib
import os
import datetime


def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    # f =open(filename,'rb')
    with open(filename, 'rb') as f:
        while True:
            # b =f.read(8096)
            b = f.read()
            if not b:
                break
            myhash.update(b)
    # f.close()
    return myhash.hexdigest()


if __name__ == "__main__":
    filepath = input('please input file path')
    starttime = datetime.datetime.now()
    print(GetFileMd5(filepath))
    endtime = datetime.datetime.now()
# print ("%ds" %((endtime-starttime).seconds)))
