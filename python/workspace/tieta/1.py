#coding:utf-8
import json 

a = {"name":'wang',
     'age':29     
     }
b = json.dumps(a)
print(a)
print(type(a))
print(b)
print(type(b))

obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
encodedjson = json.dumps(obj)
print(obj)
print(type(obj))
print(encodedjson)
print(type(encodedjson))

a = ['a','b']

print("aaa"+str(a))