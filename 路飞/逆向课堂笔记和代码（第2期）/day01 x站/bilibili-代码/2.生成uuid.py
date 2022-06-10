# import uuid
#
# # uid
# uid = str(uuid.uuid4()).upper()
# print(uid)
#
# # 时间戳
# # 1641909583372
# # 1641909620011
# import time
#
# ctime = int(time.time() * 1000)
# print(ctime % 1e5)

#
# import time
# import uuid
#
#
# def gen_uuid():
#     uuid_sec = str(uuid.uuid4())
#     time_sec = str(int(time.time() * 1000 % 1e5))
#     time_sec = time_sec.ljust(5, "0")
#
#     return "{}{}infoc".format(uuid_sec, time_sec)
#
#
# _uuid = gen_uuid()
# print(_uuid)

v = "xo"

data = v.rjust(5, "0")
print(data)
