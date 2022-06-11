import time
import math

# Math.ceil(1642076710486).toString(16).toUpperCase()
t = "%X" % (math.ceil(time.time() * 1000),)
print(t)
