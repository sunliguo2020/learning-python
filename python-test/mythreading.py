#! /usr/bin/python
# -*- coding: utf-8 -*
'''
以下程序的功能是在4个主目录下枚举的320个目录中查找符合要求的640类文件，为了加快运行效率，使用了线程。
该320个目录下大约有3300多万个文件，使用下列程序，能在60秒内遍历完所有文件并查找处符合要求的文件。
线程函数的入参是目录列表，线程的功能是遍历主目录下的每个子目录，列出文件名字符串，并存入数组，以供使用。
程序为了方便使用了全局变量。代码如下，当做学习笔记暂记。核心功能是线程函数，正则表达。
————————————————
版权声明：本文为CSDN博主「Echoli114」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_33195791/article/details/98662071

'''

import os
import sys
import re
import pprint
import threading
from threading import current_thread
import datetime
import traceback
import logging

LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "  # 配置输出日志格式
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a '  # 配置输出时间的格式，注意月份和天数不要搞乱了
LOG_PATH = None  # os.path.join(os.getcwd(),'debugging.log')
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt=DATE_FORMAT,
                    filename=LOG_PATH  # 有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                    )

rate_channel_640 = ['CHGEMOB.00101', 'CHGEMOB.00102', 'CHGEMOB.00201', 'CHGEMOB.00202', 'CHGEMOB.00301',
                    'CHGEMOB.00302', 'CHGEMOB.00401', 'CHGEMOB.00402', 'CHGEMOB.00501', 'CHGEMOB.00502',
                    'CHGEMOB.00601', 'CHGEMOB.00602', 'CHGEMOB.00701', 'CHGEMOB.00702', 'CHGEMOB.00801',
                    'CHGEMOB.00802', 'CHGEMOB.00901', 'CHGEMOB.00902', 'CHGEMOB.01001', 'CHGEMOB.01002',
                    'CHGEMOB.01101', 'CHGEMOB.01102', 'CHGEMOB.01201', 'CHGEMOB.01202', 'CHGEMOB.01301',
                    'CHGEMOB.01302', 'CHGEMOB.01401', 'CHGEMOB.01402', 'CHGEMOB.01501', 'CHGEMOB.01502',
                    'CHGEMOB.01601', 'CHGEMOB.01602', 'CHGEMOB.01701', 'CHGEMOB.01702', 'CHGEMOB.01801',
                    'CHGEMOB.01802', 'CHGEMOB.01901', 'CHGEMOB.01902', 'CHGEMOB.02001', 'CHGEMOB.02002',
                    'CHGEMOB.02101', 'CHGEMOB.02102', 'CHGEMOB.02201', 'CHGEMOB.02202', 'CHGEMOB.02301',
                    'CHGEMOB.02302', 'CHGEMOB.02401', 'CHGEMOB.02402', 'CHGEMOB.02501', 'CHGEMOB.02502',
                    'CHGEMOB.02601', 'CHGEMOB.02602', 'CHGEMOB.02701', 'CHGEMOB.02702', 'CHGEMOB.02801',
                    'CHGEMOB.02802', 'CHGEMOB.02901', 'CHGEMOB.02902', 'CHGEMOB.03001', 'CHGEMOB.03002',
                    'CHGEMOB.03101', 'CHGEMOB.03102', 'CHGEMOB.03201', 'CHGEMOB.03202', 'CHGEMOB.03301',
                    'CHGEMOB.03302', 'CHGEMOB.03401', 'CHGEMOB.03402', 'CHGEMOB.03501', 'CHGEMOB.03502',
                    'CHGEMOB.03601', 'CHGEMOB.03602', 'CHGEMOB.03701', 'CHGEMOB.03702', 'CHGEMOB.03801',
                    'CHGEMOB.03802', 'CHGEMOB.03901', 'CHGEMOB.03902', 'CHGEMOB.04001', 'CHGEMOB.04002',
                    'CHGEMOB.04101', 'CHGEMOB.04102', 'CHGEMOB.04201', 'CHGEMOB.04202', 'CHGEMOB.04301',
                    'CHGEMOB.04302', 'CHGEMOB.04401', 'CHGEMOB.04402', 'CHGEMOB.04501', 'CHGEMOB.04502',
                    'CHGEMOB.04601', 'CHGEMOB.04602', 'CHGEMOB.04701', 'CHGEMOB.04702', 'CHGEMOB.04801',
                    'CHGEMOB.04802', 'CHGEMOB.04901', 'CHGEMOB.04902', 'CHGEMOB.05001', 'CHGEMOB.05002',
                    'CHGEMOB.05101', 'CHGEMOB.05102', 'CHGEMOB.05201', 'CHGEMOB.05202', 'CHGEMOB.05301',
                    'CHGEMOB.05302', 'CHGEMOB.05401', 'CHGEMOB.05402', 'CHGEMOB.05501', 'CHGEMOB.05502',
                    'CHGEMOB.05601', 'CHGEMOB.05602', 'CHGEMOB.05701', 'CHGEMOB.05702', 'CHGEMOB.05801',
                    'CHGEMOB.05802', 'CHGEMOB.05901', 'CHGEMOB.05902', 'CHGEMOB.06001', 'CHGEMOB.06002',
                    'CHGEMOB.06101', 'CHGEMOB.06102', 'CHGEMOB.06201', 'CHGEMOB.06202', 'CHGEMOB.06301',
                    'CHGEMOB.06302', 'CHGEMOB.06401', 'CHGEMOB.06402', 'CHGEMOB.06501', 'CHGEMOB.06502',
                    'CHGEMOB.06601', 'CHGEMOB.06602', 'CHGEMOB.06701', 'CHGEMOB.06702', 'CHGEMOB.06801',
                    'CHGEMOB.06802', 'CHGEMOB.06901', 'CHGEMOB.06902', 'CHGEMOB.07001', 'CHGEMOB.07002',
                    'CHGEMOB.07101', 'CHGEMOB.07102', 'CHGEMOB.07201', 'CHGEMOB.07202', 'CHGEMOB.07301',
                    'CHGEMOB.07302', 'CHGEMOB.07401', 'CHGEMOB.07402', 'CHGEMOB.07501', 'CHGEMOB.07502',
                    'CHGEMOB.07601', 'CHGEMOB.07602', 'CHGEMOB.07701', 'CHGEMOB.07702', 'CHGEMOB.07801',
                    'CHGEMOB.07802', 'CHGEMOB.07901', 'CHGEMOB.07902', 'CHGEMOB.08001', 'CHGEMOB.08002',
                    'CHGEMOB.08101', 'CHGEMOB.08102', 'CHGEMOB.08201', 'CHGEMOB.08202', 'CHGEMOB.08301',
                    'CHGEMOB.08302', 'CHGEMOB.08401', 'CHGEMOB.08402', 'CHGEMOB.08501', 'CHGEMOB.08502',
                    'CHGEMOB.08601', 'CHGEMOB.08602', 'CHGEMOB.08701', 'CHGEMOB.08702', 'CHGEMOB.08801',
                    'CHGEMOB.08802', 'CHGEMOB.08901', 'CHGEMOB.08902', 'CHGEMOB.09001', 'CHGEMOB.09002',
                    'CHGEMOB.09101', 'CHGEMOB.09102', 'CHGEMOB.09201', 'CHGEMOB.09202', 'CHGEMOB.09301',
                    'CHGEMOB.09302', 'CHGEMOB.09401', 'CHGEMOB.09402', 'CHGEMOB.09501', 'CHGEMOB.09502',
                    'CHGEMOB.09601', 'CHGEMOB.09602', 'CHGEMOB.09701', 'CHGEMOB.09702', 'CHGEMOB.09801',
                    'CHGEMOB.09802', 'CHGEMOB.09901', 'CHGEMOB.09902', 'CHGEMOB.10001', 'CHGEMOB.10002',
                    'CHGEMOB.10101', 'CHGEMOB.10102', 'CHGEMOB.10201', 'CHGEMOB.10202', 'CHGEMOB.10301',
                    'CHGEMOB.10302', 'CHGEMOB.10401', 'CHGEMOB.10402', 'CHGEMOB.10501', 'CHGEMOB.10502',
                    'CHGEMOB.10601', 'CHGEMOB.10602', 'CHGEMOB.10701', 'CHGEMOB.10702', 'CHGEMOB.10801',
                    'CHGEMOB.10802', 'CHGEMOB.10901', 'CHGEMOB.10902', 'CHGEMOB.11001', 'CHGEMOB.11002',
                    'CHGEMOB.11101', 'CHGEMOB.11102', 'CHGEMOB.11201', 'CHGEMOB.11202', 'CHGEMOB.11301',
                    'CHGEMOB.11302', 'CHGEMOB.11401', 'CHGEMOB.11402', 'CHGEMOB.11501', 'CHGEMOB.11502',
                    'CHGEMOB.11601', 'CHGEMOB.11602', 'CHGEMOB.11701', 'CHGEMOB.11702', 'CHGEMOB.11801',
                    'CHGEMOB.11802', 'CHGEMOB.11901', 'CHGEMOB.11902', 'CHGEMOB.12001', 'CHGEMOB.12002',
                    'CHGEMOB.12101', 'CHGEMOB.12102', 'CHGEMOB.12201', 'CHGEMOB.12202', 'CHGEMOB.12301',
                    'CHGEMOB.12302', 'CHGEMOB.12401', 'CHGEMOB.12402', 'CHGEMOB.12501', 'CHGEMOB.12502',
                    'CHGEMOB.12601', 'CHGEMOB.12602', 'CHGEMOB.12701', 'CHGEMOB.12702', 'CHGEMOB.12801',
                    'CHGEMOB.12802', 'CHGEMOB.12901', 'CHGEMOB.12902', 'CHGEMOB.13001', 'CHGEMOB.13002',
                    'CHGEMOB.13101', 'CHGEMOB.13102', 'CHGEMOB.13201', 'CHGEMOB.13202', 'CHGEMOB.13301',
                    'CHGEMOB.13302', 'CHGEMOB.13401', 'CHGEMOB.13402', 'CHGEMOB.13501', 'CHGEMOB.13502',
                    'CHGEMOB.13601', 'CHGEMOB.13602', 'CHGEMOB.13701', 'CHGEMOB.13702', 'CHGEMOB.13801',
                    'CHGEMOB.13802', 'CHGEMOB.13901', 'CHGEMOB.13902', 'CHGEMOB.14001', 'CHGEMOB.14002',
                    'CHGEMOB.14101', 'CHGEMOB.14102', 'CHGEMOB.14201', 'CHGEMOB.14202', 'CHGEMOB.14301',
                    'CHGEMOB.14302', 'CHGEMOB.14401', 'CHGEMOB.14402', 'CHGEMOB.14501', 'CHGEMOB.14502',
                    'CHGEMOB.14601', 'CHGEMOB.14602', 'CHGEMOB.14701', 'CHGEMOB.14702', 'CHGEMOB.14801',
                    'CHGEMOB.14802', 'CHGEMOB.14901', 'CHGEMOB.14902', 'CHGEMOB.15001', 'CHGEMOB.15002',
                    'CHGEMOB.15101', 'CHGEMOB.15102', 'CHGEMOB.15201', 'CHGEMOB.15202', 'CHGEMOB.15301',
                    'CHGEMOB.15302', 'CHGEMOB.15401', 'CHGEMOB.15402', 'CHGEMOB.15501', 'CHGEMOB.15502',
                    'CHGEMOB.15601', 'CHGEMOB.15602', 'CHGEMOB.15701', 'CHGEMOB.15702', 'CHGEMOB.15801',
                    'CHGEMOB.15802', 'CHGEMOB.15901', 'CHGEMOB.15902', 'CHGEMOB.16001', 'CHGEMOB.16002',
                    'CHGEMOB.16101', 'CHGEMOB.16102', 'CHGEMOB.16201', 'CHGEMOB.16202', 'CHGEMOB.16301',
                    'CHGEMOB.16302', 'CHGEMOB.16401', 'CHGEMOB.16402', 'CHGEMOB.16501', 'CHGEMOB.16502',
                    'CHGEMOB.16601', 'CHGEMOB.16602', 'CHGEMOB.16701', 'CHGEMOB.16702', 'CHGEMOB.16801',
                    'CHGEMOB.16802', 'CHGEMOB.16901', 'CHGEMOB.16902', 'CHGEMOB.17001', 'CHGEMOB.17002',
                    'CHGEMOB.17101', 'CHGEMOB.17102', 'CHGEMOB.17201', 'CHGEMOB.17202', 'CHGEMOB.17301',
                    'CHGEMOB.17302', 'CHGEMOB.17401', 'CHGEMOB.17402', 'CHGEMOB.17501', 'CHGEMOB.17502',
                    'CHGEMOB.17601', 'CHGEMOB.17602', 'CHGEMOB.17701', 'CHGEMOB.17702', 'CHGEMOB.17801',
                    'CHGEMOB.17802', 'CHGEMOB.17901', 'CHGEMOB.17902', 'CHGEMOB.18001', 'CHGEMOB.18002',
                    'CHGEMOB.18101', 'CHGEMOB.18102', 'CHGEMOB.18201', 'CHGEMOB.18202', 'CHGEMOB.18301',
                    'CHGEMOB.18302', 'CHGEMOB.18401', 'CHGEMOB.18402', 'CHGEMOB.18501', 'CHGEMOB.18502',
                    'CHGEMOB.18601', 'CHGEMOB.18602', 'CHGEMOB.18701', 'CHGEMOB.18702', 'CHGEMOB.18801',
                    'CHGEMOB.18802', 'CHGEMOB.18901', 'CHGEMOB.18902', 'CHGEMOB.19001', 'CHGEMOB.19002',
                    'CHGEMOB.19101', 'CHGEMOB.19102', 'CHGEMOB.19201', 'CHGEMOB.19202', 'CHGEMOB.19301',
                    'CHGEMOB.19302', 'CHGEMOB.19401', 'CHGEMOB.19402', 'CHGEMOB.19501', 'CHGEMOB.19502',
                    'CHGEMOB.19601', 'CHGEMOB.19602', 'CHGEMOB.19701', 'CHGEMOB.19702', 'CHGEMOB.19801',
                    'CHGEMOB.19802', 'CHGEMOB.19901', 'CHGEMOB.19902', 'CHGEMOB.20001', 'CHGEMOB.20002',
                    'CHGEMOB.20101', 'CHGEMOB.20102', 'CHGEMOB.20201', 'CHGEMOB.20202', 'CHGEMOB.20301',
                    'CHGEMOB.20302', 'CHGEMOB.20401', 'CHGEMOB.20402', 'CHGEMOB.20501', 'CHGEMOB.20502',
                    'CHGEMOB.20601', 'CHGEMOB.20602', 'CHGEMOB.20701', 'CHGEMOB.20702', 'CHGEMOB.20801',
                    'CHGEMOB.20802', 'CHGEMOB.20901', 'CHGEMOB.20902', 'CHGEMOB.21001', 'CHGEMOB.21002',
                    'CHGEMOB.21101', 'CHGEMOB.21102', 'CHGEMOB.21201', 'CHGEMOB.21202', 'CHGEMOB.21301',
                    'CHGEMOB.21302', 'CHGEMOB.21401', 'CHGEMOB.21402', 'CHGEMOB.21501', 'CHGEMOB.21502',
                    'CHGEMOB.21601', 'CHGEMOB.21602', 'CHGEMOB.21701', 'CHGEMOB.21702', 'CHGEMOB.21801',
                    'CHGEMOB.21802', 'CHGEMOB.21901', 'CHGEMOB.21902', 'CHGEMOB.22001', 'CHGEMOB.22002',
                    'CHGEMOB.22101', 'CHGEMOB.22102', 'CHGEMOB.22201', 'CHGEMOB.22202', 'CHGEMOB.22301',
                    'CHGEMOB.22302', 'CHGEMOB.22401', 'CHGEMOB.22402', 'CHGEMOB.22501', 'CHGEMOB.22502',
                    'CHGEMOB.22601', 'CHGEMOB.22602', 'CHGEMOB.22701', 'CHGEMOB.22702', 'CHGEMOB.22801',
                    'CHGEMOB.22802', 'CHGEMOB.22901', 'CHGEMOB.22902', 'CHGEMOB.23001', 'CHGEMOB.23002',
                    'CHGEMOB.23101', 'CHGEMOB.23102', 'CHGEMOB.23201', 'CHGEMOB.23202', 'CHGEMOB.23301',
                    'CHGEMOB.23302', 'CHGEMOB.23401', 'CHGEMOB.23402', 'CHGEMOB.23501', 'CHGEMOB.23502',
                    'CHGEMOB.23601', 'CHGEMOB.23602', 'CHGEMOB.23701', 'CHGEMOB.23702', 'CHGEMOB.23801',
                    'CHGEMOB.23802', 'CHGEMOB.23901', 'CHGEMOB.23902', 'CHGEMOB.24001', 'CHGEMOB.24002',
                    'CHGEMOB.24101', 'CHGEMOB.24102', 'CHGEMOB.24201', 'CHGEMOB.24202', 'CHGEMOB.24301',
                    'CHGEMOB.24302', 'CHGEMOB.24401', 'CHGEMOB.24402', 'CHGEMOB.24501', 'CHGEMOB.24502',
                    'CHGEMOB.24601', 'CHGEMOB.24602', 'CHGEMOB.24701', 'CHGEMOB.24702', 'CHGEMOB.24801',
                    'CHGEMOB.24802', 'CHGEMOB.24901', 'CHGEMOB.24902', 'CHGEMOB.25001', 'CHGEMOB.25002',
                    'CHGEMOB.25101', 'CHGEMOB.25102', 'CHGEMOB.25201', 'CHGEMOB.25202', 'CHGEMOB.25301',
                    'CHGEMOB.25302', 'CHGEMOB.25401', 'CHGEMOB.25402', 'CHGEMOB.25501', 'CHGEMOB.25502',
                    'CHGEMOB.25601', 'CHGEMOB.25602', 'CHGEMOB.25701', 'CHGEMOB.25702', 'CHGEMOB.25801',
                    'CHGEMOB.25802', 'CHGEMOB.25901', 'CHGEMOB.25902', 'CHGEMOB.26001', 'CHGEMOB.26002',
                    'CHGEMOB.26101', 'CHGEMOB.26102', 'CHGEMOB.26201', 'CHGEMOB.26202', 'CHGEMOB.26301',
                    'CHGEMOB.26302', 'CHGEMOB.26401', 'CHGEMOB.26402', 'CHGEMOB.26501', 'CHGEMOB.26502',
                    'CHGEMOB.26601', 'CHGEMOB.26602', 'CHGEMOB.26701', 'CHGEMOB.26702', 'CHGEMOB.26801',
                    'CHGEMOB.26802', 'CHGEMOB.26901', 'CHGEMOB.26902', 'CHGEMOB.27001', 'CHGEMOB.27002',
                    'CHGEMOB.27101', 'CHGEMOB.27102', 'CHGEMOB.27201', 'CHGEMOB.27202', 'CHGEMOB.27301',
                    'CHGEMOB.27302', 'CHGEMOB.27401', 'CHGEMOB.27402', 'CHGEMOB.27501', 'CHGEMOB.27502',
                    'CHGEMOB.27601', 'CHGEMOB.27602', 'CHGEMOB.27701', 'CHGEMOB.27702', 'CHGEMOB.27801',
                    'CHGEMOB.27802', 'CHGEMOB.27901', 'CHGEMOB.27902', 'CHGEMOB.28001', 'CHGEMOB.28002',
                    'CHGEMOB.28101', 'CHGEMOB.28102', 'CHGEMOB.28201', 'CHGEMOB.28202', 'CHGEMOB.28301',
                    'CHGEMOB.28302', 'CHGEMOB.28401', 'CHGEMOB.28402', 'CHGEMOB.28501', 'CHGEMOB.28502',
                    'CHGEMOB.28601', 'CHGEMOB.28602', 'CHGEMOB.28701', 'CHGEMOB.28702', 'CHGEMOB.28801',
                    'CHGEMOB.28802', 'CHGEMOB.28901', 'CHGEMOB.28902', 'CHGEMOB.29001', 'CHGEMOB.29002',
                    'CHGEMOB.29101', 'CHGEMOB.29102', 'CHGEMOB.29201', 'CHGEMOB.29202', 'CHGEMOB.29301',
                    'CHGEMOB.29302', 'CHGEMOB.29401', 'CHGEMOB.29402', 'CHGEMOB.29501', 'CHGEMOB.29502',
                    'CHGEMOB.29601', 'CHGEMOB.29602', 'CHGEMOB.29701', 'CHGEMOB.29702', 'CHGEMOB.29801',
                    'CHGEMOB.29802', 'CHGEMOB.29901', 'CHGEMOB.29902', 'CHGEMOB.30001', 'CHGEMOB.30002',
                    'CHGEMOB.30101', 'CHGEMOB.30102', 'CHGEMOB.30201', 'CHGEMOB.30202', 'CHGEMOB.30301',
                    'CHGEMOB.30302', 'CHGEMOB.30401', 'CHGEMOB.30402', 'CHGEMOB.30501', 'CHGEMOB.30502',
                    'CHGEMOB.30601', 'CHGEMOB.30602', 'CHGEMOB.30701', 'CHGEMOB.30702', 'CHGEMOB.30801',
                    'CHGEMOB.30802', 'CHGEMOB.30901', 'CHGEMOB.30902', 'CHGEMOB.31001', 'CHGEMOB.31002',
                    'CHGEMOB.31101', 'CHGEMOB.31102', 'CHGEMOB.31201', 'CHGEMOB.31202', 'CHGEMOB.31301',
                    'CHGEMOB.31302', 'CHGEMOB.31401', 'CHGEMOB.31402', 'CHGEMOB.31501', 'CHGEMOB.31502',
                    'CHGEMOB.31601', 'CHGEMOB.31602', 'CHGEMOB.31701', 'CHGEMOB.31702', 'CHGEMOB.31801',
                    'CHGEMOB.31802', 'CHGEMOB.31901', 'CHGEMOB.31902', 'CHGEMOB.32001', 'CHGEMOB.32002']

rrdata1_sub = ['km51', 'km67', 'km18', 'km71', 'km34', 'km30', 'km35', 'km73', 'km74', 'km48', 'km53', 'km45', 'km46',
               'km69', 'km78', 'km77', 'km42', 'km43', 'km44', 'km52', 'km68', 'km80', 'km47', 'km70', 'km79', 'km72',
               'km11', 'km55', 'km56', 'km54', 'km41', 'km66', 'km65', 'km50', 'km01', 'km14', 'km33', 'km38', 'km36',
               'km28', 'km27', 'km06', 'km24', 'km16', 'km37', 'km02', 'km20', 'km10', 'km03', 'km07', 'km19', 'km12',
               'km15', 'km26', 'km04', 'km25', 'km09', 'km13', 'km17', 'km05', 'km08', 'km76', 'km75', 'km62', 'km61',
               'km40', 'km39', 'km63', 'km64', 'km22', 'km21', 'km31', 'km32', 'km57', 'km58', 'km23', 'km29', 'km49',
               'km60', 'km59']
rrdata2_sub = ['dh03', 'dh04', 'dh12', 'dh11', 'dh08', 'dh07', 'dq01', 'dq02', 'ws02', 'dh05', 'dh06', 'dh10', 'dh09',
               'ws17', 'qj13', 'qj14', 'qj30', 'qj29', 'qj24', 'qj23', 'qj08', 'dh02', 'dh01', 'lc04', 'lc03', 'lc12',
               'lc11', 'qj07', 'qj11', 'ws12', 'qj12', 'qj16', 'ws06', 'ws14', 'qj15', 'ws11', 'ws03', 'ws05', 'ws01',
               'ws04', 'ws19', 'ws20', 'qj03', 'qj20', 'lc08', 'lc07', 'lc09', 'ws08', 'lc10', 'ws07', 'qj10', 'qj09',
               'qj05', 'qj06', 'qj17', 'qj18', 'ws16', 'ws15', 'qj27', 'qj28', 'qj22', 'qj21', 'ws09', 'ws10', 'ws18',
               'qj04', 'qj19', 'qj02', 'qj01', 'lc02', 'lc01', 'dq04', 'qj25', 'qj26', 'dq03', 'qj31', 'qj32', 'ws13',
               'lc05', 'lc06']
rrdata3_sub = ['pe07', 'hh22', 'cx01', 'cx04', 'cx03', 'pe03', 'pe01', 'pe12', 'cx13', 'pe04', 'pe02', 'cx02', 'pe16',
               'pe15', 'cx14', 'pe08', 'pe09', 'pe10', 'pe11', 'yx10', 'yx09', 'hh20', 'hh19', 'hh21', 'hh24', 'hh23',
               'pe06', 'pe05', 'pe14', 'pe13', 'hh01', 'hh02', 'hh07', 'hh08', 'hh15', 'hh16', 'yx04', 'yx03', 'yx06',
               'yx05', 'hh14', 'hh13', 'cx07', 'cx08', 'cx10', 'cx09', 'yx11', 'yx12', 'hh04', 'hh10', 'hh09', 'cx11',
               'cx12', 'hh17', 'hh18', 'hh05', 'hh06', 'cx06', 'cx05', 'hh03', 'cx15', 'cx16', 'nj04', 'nj03', 'yx02',
               'yx01', 'yx07', 'nj02', 'yx08', 'nj01', 'hh12', 'hh11']
rrdata4_sub = ['lj12', 'lj11', 'lj09', 'lj10', 'bs14', 'bs16', 'bs15', 'bn08', 'bs11', 'bn07', 'bs12', 'zt13', 'zt14',
               'zt02', 'zt01', 'lj01', 'zt05', 'lj02', 'bn06', 'bn05', 'lj08', 'lj07', 'zt21', 'dl02', 'dl01', 'lj04',
               'lj03', 'zt23', 'zt24', 'zt17', 'zt18', 'zt27', 'zt26', 'zt25', 'bs02', 'bs01', 'zt12', 'zt03', 'dl15',
               'dl16', 'zt04', 'lj06', 'zt11', 'lj05', 'zt28', 'zt06', 'zt22', 'bs10', 'bs07', 'bs08', 'bs09', 'zt16',
               'zt15', 'bn04', 'bn12', 'bn11', 'bn03', 'dl13', 'dl14', 'bs05', 'bs06', 'bs04', 'bs03', 'dl19', 'dl20',
               'zt10', 'zt09', 'dl08', 'dl05', 'dl07', 'dl06', 'dl12', 'dl10', 'dl11', 'bs13', 'dl09', 'dl03', 'dl04',
               'dl17', 'bn01', 'bn02', 'dl18', 'zt20', 'zt19', 'zt07', 'zt08', 'bn09', 'bn10']

find_base_path_1 = '/rrdata1/data/sender_backup'
find_base_path_2 = '/rrdata2/data/sender_backup'
find_base_path_3 = '/rrdata3/data/sender_backup'
find_base_path_4 = '/rrdata4/data/sender_backup'

find_path1 = []
find_path2 = []
find_path3 = []
find_path4 = []


def build_find_path():
    for sub_path1 in rrdata1_sub:
        path1 = os.path.join(find_base_path_1, str(sub_path1), )
        logging.debug('path1 = %s' % (path1))
        find_path1.append(path1)

    for sub_path2 in rrdata2_sub:
        path2 = os.path.join(find_base_path_2, str(sub_path2), )
        logging.debug('path1 = %s' % (path2))
        find_path2.append(path2)

    for sub_path3 in rrdata3_sub:
        path3 = os.path.join(find_base_path_3, str(sub_path3), )
        logging.debug('path1 = %s' % (path3))
        find_path3.append(path3)

    for sub_path4 in rrdata4_sub:
        path4 = os.path.join(find_base_path_4, str(sub_path4), )
        logging.debug('path1 = %s' % (path4))
        find_path4.append(path4)
    '''
    logging.debug('find_path1 list number is %d' %(len(find_path1)))
    logging.debug(find_path1)
    logging.debug('find_path2 list number is %d' %(len(find_path2)))
    logging.debug(find_path2)
    logging.debug('find_path3 list number is %d' %(len(find_path3)))
    logging.debug(find_path3)
    logging.debug('find_path4 list number is %d' %(len(find_path4)))
    logging.debug(find_path4)
    '''
crrpath = os.getcwd()

FIND_PATH = []
for i in range(1, 5):
    FIND_PATH.append('/rrdata%s/data/sender_backup' % (i))
logging.debug(FIND_PATH)


def routine_list_path(find_path, result, not_inc_file):
    regRule = re.compile(r'CHGEMOB.\w+')
    thread = threading.current_thread()
    thread_name = thread.getName()
    try:
        for sub_path in find_path:
            listdir = os.listdir(sub_path)
            file_num = len(listdir)
            count = 0
            for i in range(file_num):
                rulefile = regRule.findall(str(listdir[i]))
                if len(rulefile) != 0:
                    result.append(listdir[i])
                    count += 1
            if 0 == count:
                not_inc_file.append(str(sub_path))
            '''
            nowtime = datetime.datetime.now()
            logging.debug('current thread is %s,find forlder is %s, count = %d, now_time is %s' %(thread_name,sub_path, count,nowtime.strftime("%Y-%m-%d %H:%M:%S")))
            '''
            logging.debug('current thread is %s,find forlder is %s, count = %d' % (thread_name, sub_path, count))

    except:
        # 记录错误
        logging.debug(traceback.format_exc())


def walkdir_find():
    files_list = []
    path_list = []

    result1 = []
    result2 = []
    result3 = []
    result4 = []

    not_inc_file1 = []
    not_inc_file2 = []
    not_inc_file3 = []
    not_inc_file4 = []

    logging.debug('try to create thread...')
    t1 = threading.Thread(target=routine_list_path, name='thread1', args=(find_path1, result1, not_inc_file1))
    t2 = threading.Thread(target=routine_list_path, name='thread2', args=(find_path2, result2, not_inc_file2))
    t3 = threading.Thread(target=routine_list_path, name='thread3', args=(find_path3, result3, not_inc_file3))
    t4 = threading.Thread(target=routine_list_path, name='thread4', args=(find_path4, result4, not_inc_file4))
    # start
    t1.start()
    logging.debug('starting thread1...')
    t2.start()
    logging.debug('starting thread2...')
    t3.start()
    logging.debug('starting thread3...')
    t4.start()
    logging.debug('starting thread4...')

    # join
    t1.join()
    logging.debug('join thread1...')
    t2.join()
    logging.debug('join thread2...')
    t3.join()
    logging.debug('join thread3...')
    t4.join()
    logging.debug('join thread4...')

    # logging.debug('total %d files finded' %(count))
    # logging.debug(find_list)
    '''
    logging.debug('--------------------------------------result1--------------------------------------------')
    logging.debug(result1)
    logging.debug('--------------------------------------result2--------------------------------------------')
    logging.debug(result2)
    logging.debug('--------------------------------------result3--------------------------------------------')
    logging.debug(result3)
    logging.debug('--------------------------------------result4--------------------------------------------')
    logging.debug(result4)
    '''
    files_list = result1 + result2 + result3 + result4
    path_list = not_inc_file1 + not_inc_file2 + not_inc_file3 + not_inc_file4

    return files_list  # , path_list


def exduplicat(finded):
    find_dic = {}
    logging.debug('write finded files to CHGEMOB.FIND...')
    finded_file = open(os.path.join(os.getcwd(), 'CHGEMOB.FIND'), 'w')
    finded_file.write(str(pprint.pformat(finded)))
    finded_file.close()

    for changemob in rate_channel_640:
        find_dic.setdefault(changemob, 0)
        rstr = str(changemob)
        temp_reg = re.compile(rstr)
        # logging.debug('rstr = %s' %(rstr))
        for file_name in finded:
            lst_str = temp_reg.findall(file_name)
            if len(lst_str) != 0:
                # logging.debug('finded %s PREFIX file' %(changemob))
                find_dic[changemob] += 1

    return find_dic


def print_find_dic(finds_dic):
    crr_path = os.getcwd()
    list_no_key = []
    list_yes_key = []

    # pprint.pprint(finds_dic)
    for key in finds_dic:
        if finds_dic[key] == 0:
            list_no_key.append(str(key))
        else:
            list_yes_key.append(str(key))

    no_len = len(list_no_key)
    ye_slen = len(list_yes_key)

    # open files to write result
    not_str = ''
    file_no = open(os.path.join(crr_path, 'NOT_FINDED.TXT'), 'w')
    for not_find_str in list_no_key:
        not_find_str = str(not_find_str) + '\n'
        not_str = not_str + not_find_str
    file_no.write(not_str)
    file_no.write('%d TYPE NOT FINDED!\n' % (no_len))

    # logging.debug
    # pprint.pprint(list_no_key)
    logging.debug('################################ ALL DIRECTORY FIND END ################################')
    logging.debug('[%d/640] types file NOT FINDED!' % (no_len))

    file_yes = open(os.path.join(crr_path, 'FINDED.TXT'), 'w')
    yes_str = ''
    for find_str in list_yes_key:
        find_str = str(find_str) + '\n'
        yes_str = yes_str + find_str
    file_yes.write(yes_str)
    file_yes.write('%d TYPE FINDED!\n' % (ye_slen))
    # logging.debug
    # pprint.pprint(list_yes_key)
    logging.debug('[%d/640] types file FINDED' % (ye_slen))

    file_no.close()
    file_yes.close()


if __name__ == '__main__':
    build_find_path()
    find_all = walkdir_find()
    finds_dic = exduplicat(find_all)
    print_find_dic(finds_dic)
