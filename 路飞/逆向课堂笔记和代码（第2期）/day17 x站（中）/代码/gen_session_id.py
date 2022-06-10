import random

session_id = "".join([hex(item)[2:] for item in random.randbytes(4)])
print(session_id)
