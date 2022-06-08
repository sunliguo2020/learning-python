# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/20 11:07
"""

import vobject

with open(r"c:\Users\sunliguo\Desktop\手机\00001.vcf") as fp:
    #vcf = vobject.readOne(fp)
    vcardlist = vobject.readOne(fp)
    print(type(vcardlist))

    # for vcard in vcardlist:
    #     print(vcard)
