import os
import json
import util
import math
from Parser import Parser
from datetime import datetime

parser = Parser()

d = json.load(open("./IDF.json"))
WordFreInDoc = json.loads(d)

d2 = json.load(open("./Word.json"))
WordIndex = json.loads(d2)


t1 = datetime.now()

for file in os.listdir("../lyrics_process"):
    
    top5 = [0] * 5
    top5word = [""] * 5

    f = open("../lyrics_process/" + file, 'r')
    content = f.read()
    content = content.split(' ')
    f.close()

    if content[0] == "":
        content = content[1::]

    DiffTerm = util.removeDuplicates(content)
    
    print("=== Counting TF-IDF ===")

    for word in DiffTerm:
        
        print(word)

        tfidf = content.count(word) * math.log(81975/ (1 + WordFreInDoc[WordIndex[word]]))
        
        print("----- TOP5 Word -----")

        for index in range(0,5):
            
            if tfidf > top5[index]:

                top5[index] = tfidf
                top5word[index] = word
                
                break
    
    print("Dump json file...")
    w = open("../lyrics_tfidf/" + file + ".json", 'w')
    json_array = json.dumps(top5word)
    json.dump(json_array, w)
    w.close()

t2 = datetime.now()
t3 = t2 - t1

print("Process Time: " + str(t3.seconds/60) + " mins")
