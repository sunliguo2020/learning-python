def get_uuid():
    import execjs
    node = execjs.get()
    fp = open('uuid.js','r',encoding='utf-8')
    ctx = node.compile(fp.read())
    uuid = ctx.eval('get_uuid()')
    return uuid
print(get_uuid())

