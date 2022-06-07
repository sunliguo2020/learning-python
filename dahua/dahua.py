# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/4/28 12:19
"""
from ctypes import *
libc = windll.LoadLibrary('lib/dhnetsdk.dll')
g_bNetSDKInitFlag = False


def InitTest():
    print(libc.CLIENT_Init)
    id = create_string_buffer(1024)
    char = create_string_buffer(1024)
    long = create_string_buffer(1024)
    word = create_string_buffer(1024)

    g_bNetSDKInitFlag = libc.CLIENT_Init(DisConnect(id, char, long, word), 0)

    if not g_bNetSDKInitFlag:
        print("Initialize False")
    else:
        print("Initialize client SDK done; \n")
    dwNetSDKVersion = libc.CLIENT_GetSDKVersion()
    print("NetSDK version is %d" % dwNetSDKVersion)

def RunTest():
    if not g_bNetSDKInitFlag:
        return

def EndTest():
    print("input any key to quit!\n")
    #getChar()

    if not g_bNetSDKInitFlag:
        #CLIENT_Cleanup()
        NetFlag()
    #return

def NetFlag():
    g_bNetSDKInitFlag = False


def DisConnect( lLoginID, pchDVRIP, nDVRPort, dwUser):
    print("Call HaveReConnect \n")
    print("lLoginID[ 0x%x ]", lLoginID)
    if pchDVRIP:
        print("pchDVRIP[%s]\n", pchDVRIP)
    print("nDVRPort[%d]\n", nDVRPort)
    print('dwUser[%p]\n', dwUser)
    print( "\n")

def HaveReConnect( lLoginID, pchDVRIP, nDVRPort, dwUser):
    print("Call HaveReConnect \n")
    print("lLoginID[ 0x%x ]", lLoginID)
    if pchDVRIP:
        print("pchDVRIP[%s]\n", pchDVRIP)
    print("nDVRPort[%d]\n", nDVRPort)
    print('dwUser[%p]\n', dwUser)
    print( "\n")


def main():
    InitTest()
    RunTest()
    EndTest()

if __name__ == '__main__':
    main()