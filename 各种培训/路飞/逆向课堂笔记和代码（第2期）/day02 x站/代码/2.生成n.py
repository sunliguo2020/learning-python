import random
import math
import time


def gen_b_lsid():
    t1 = "%X" % (math.ceil(time.time() * 1000),)

    t = ""
    for i in range(8):
        t += "%X" % (math.ceil(16 * random.random()),)

    res = t.rjust(8, "0")

    return "{}_{}".format(res, t1)


b_lsid = gen_b_lsid()
print(b_lsid)
