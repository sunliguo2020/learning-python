# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/14 18:23
"""
def stu_registriation_form():
    form  ={
        "name":input("Name:").strip(),
        "age":input("age:").strip(),
        "phone":input('Phone:').strip()
    }
    info_pass_flag = True
    for  k,v in form.items():
        if(len(v)) ==0:
            info_pass_flag  =  False
            break
    return form,info_pass_flag

stu_info,flag = stu_registriation_form()
print(stu_info)
print(flag)