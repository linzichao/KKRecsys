import os
import json
import util
from Parser import Parser
from datetime import datetime 

parser = Parser() 

d = json.load(open("./Word.json"))
data = json.loads(d)

#print(len(data))

WordInDoc = [0] * len(data)

print("Start counting one word in how many docs...")

t1 = datetime.now()

for file in os.listdir("../lyrics"):
    f = open("../lyrics/" + file, 'r')
    content = f.read()
    content = parser.tokenise(content)
    content = parser.removeStopWords(content)
    content = util.removeDuplicates(content)
    f.close()

    print("===== Add in Vector ======")
    for word in content:
        WordInDoc[data[word]] += 1
    
    print("...Next round...")


t2 = datetime.now()
t3 = t2 - t1
print("Process Time: " + str(t3.seconds/60))

print("Dump json file")
f = open("./IDF.json", "w")
json_array = json.dumps(WordInDoc)
json.dump(json_array, f)
f.close()
