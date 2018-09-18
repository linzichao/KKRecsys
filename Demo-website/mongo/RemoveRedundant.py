import os

import datetime
from datetime import datetime

import re

t1 = datetime.now()


print("========== Opening file ===========")
f = open("./output", 'r')
content = f.read()
content = content.replace("||", " ")
content = content.replace("|", " ")
f.close()
print("Closing file")


print("Writing file")
f = open("./output2", 'w')
f.write(content)
f.close()



t2 = datetime.now()
t3 = t2 - t1
print(t3.seconds/60)
