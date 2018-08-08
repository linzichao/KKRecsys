import os
import json
import util
import math
from datetime import datetime


d1 = json.load(open("./IDF_final.json"))
WordFreInDoc = json.loads(d1)

d2 = json.load(open("./allword.json"))
WordIndex = json.loads(d2)

t1 = datetime.now()

for file in os.listdir("../lyrics_tfidf"):
    
    w = open("./ETnetwork.csv", 'a')

    f = open("../lyrics_tfidf/" + file, 'r')
    content = f.read()
    d = json.loads(content)
    data = json.loads(d)
    f.close()

    print("=== Counting TF-IDF ===")

    for word in data:

        tfidf = data.count(word) * math.log(81975/ (1 + WordFreInDoc[WordIndex[word]]))
        w.write(file.replace(".json", "") + "," + word + "," + str(tfidf) + "\n")

    #json_array = json.dumps(dic)
    #json.dump(json_array, w)
    w.close()
