with open('../jiujiu.py') as fp:
    fp.__exit__()
    print(dir(fp))
    print(type(fp))