from concurrent.futures import ThreadPoolExecutor


def fn(arg1, arg2, arg3=''):
    print("arg1=", arg1)
    print("arg2=", arg2)
    print("arg3=", type(arg3), arg3)
if __name__ == '__main__':

    with ThreadPoolExecutor(2) as t:
        for i in range(3):
            arg1 = "arg1" + str(i)
            arg2 = 'arg2' + str(i)
            t.submit(fn, arg1, arg2, {"key1": "sunliguo"})
