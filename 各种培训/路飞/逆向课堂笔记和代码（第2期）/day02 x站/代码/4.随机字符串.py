import random
import string

total_string = string.digits + "abcdef"

v1 = "".join([random.choice(total_string) for i in range(32)])
print(v1)
