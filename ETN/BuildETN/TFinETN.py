import os
import json
import util
from datetime import datetime


word = json.load(open("./allword.json"))
words = json.loads(word)

WordIDF = [0] * len(words)

t1 = datetime.now()

for file in os.listdir("../lyrics_tfidf"):
    
    f = open("../lyrics_tfidf/" + file, 'r')
    content = f.read()
    data = json.loads(content)    
    d = json.loads(data)
    diffword = util.removeDuplicates(d)
    
    print("Counting all DOCs")

    for w in diffword:
        WordIDF[words[w]] += 1

    f.close()

t2 = datetime.now()
t3 = t2 - t1
print("Process Time: " + str(t3.seconds/60))

print("Dump json file")
f = open("./IDF_final.json", "w")
json_array = json.dumps(WordIDF)
json.dump(json_array, f)
f.close()
