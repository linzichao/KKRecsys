import os
import util
import json
from Parser import Parser
from datetime import datetime

AllWord = []

vectorIndex = {}

t1 = datetime.now()

for file in os.listdir("../lyrics_tfidf"):
    
    d = json.load(open("../lyrics_tfidf/" + file))
    data = json.loads(d)
    
    AllWord += data

AllWord = util.removeDuplicates(AllWord)

offset = 0
for word in AllWord:
    vectorIndex[word] = offset
    offset += 1

print(len(AllWord))

t2 = datetime.now()
t3 = t2 - t1
print("Process Time: " + str(t3.seconds/60))

print("Dump json file")
f = open("./allword.json", "w")
json_array = json.dumps(vectorIndex)
json.dump(json_array, f)
f.close()
