# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/13 17:30
"""

#集合的相关操作
s = {10,20,20,30,30,50}
#集合元素的判断操作
print(10 in s)
print(100 in s)
#集合元素的新增操作
s.add(("dfsdf",'80'))
print(s)
s.update(range(10,12))
print(s)
s.update({10,20,30,40,50})
print(s)
#s.remove(('dfsdf','803')) #KeyError: ('dfsdf', '803')
print(s)
s.discard('sdfsafd')
s.pop()
print(s)