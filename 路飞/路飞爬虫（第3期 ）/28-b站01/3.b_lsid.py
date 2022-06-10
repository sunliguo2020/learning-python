def get_b_lsid():
    import execjs
    import time
    e = str(int(time.time() * 1000))
    node = execjs.get()
    fp = open('b_lsid.js','r',encoding='utf-8')
    ctx = node.compile(fp.read())
    uuid = ctx.eval('get_final_t("%s")'%e)
    return uuid
print(get_b_lsid())

