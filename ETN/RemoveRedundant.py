import os

import datetime
from datetime import datetime

import re

t1 = datetime.now()

for file in os.listdir("./lyrics"):
    

    print("Opening file " + file + "===========")
    f = open("./lyrics/" + file, 'r')
    content = f.read()
    content = content.replace("||", " ")
    content = content.replace("|", " ")
    f.close()
    print("Closing file " + file)
 
    print("Lyrics Processing.....")
    content = re.sub(r"[^a-zA-Z ]", "", content)
    content = re.sub(r"\s+", " ", content)
    content = content.lower()

    print("Writing file " + file)
    f = open("./lyrics/" + file, 'w')
    f.write(content)
    f.close()
    
    
    
t2 = datetime.now()
t3 = t2 - t1
print(t3.seconds/60)
    
