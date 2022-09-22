import email

fp = open('d:\\1.eml')
msg = email.message_from_file(fp)
subject =msg.get('subject')


'''
if not isinstance(subject, unicode):
    subject = unicode(subject)
print(subject)
'''

h =email.header.Header(subject)


#返回一个列表，里面保存一个元组，（解码后的字符串，字符编码）

'''
[(b'=?gb2312?B?uPfOu8HstbyjutLUz8LKx8rZueLXpLXYzfjQocf40MXPoqOsx+u9q8O709DGpcXkt
b2/zbunvq3A7bXE0KHH+MalxeS1vbj2yMujrNLRvq3GpcXktb249sjLtcTXotLiusu21MrHt/HT0LTtz
vOjrMfr1NrD98zsyc+w4Mewt7TAocalxeTH6b/2o6y9q9TaMdTCMcjVzbPSu7TTz7XNs9bQuPy4xKGj?
=', 'us-ascii')]
'''
dh = email.header.decode_header(h)
print(str(dh[0][0]))
print(type(dh[0][0]))
#print(dh)
#print(msg.get('date'))
#print(msg.get_all())
fp.close()