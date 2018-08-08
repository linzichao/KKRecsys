import os 
import util
from Parser import Parser
from datetime import datetime

parser = Parser()

print("Start file processing")
for file in os.listdir("../lyrics"):
    f = open("../lyrics/" + file, 'r')
    content = f.read()
    content = parser.tokenise(content)
    content = parser.removeStopWords(content)
    content = util.removeDuplicates(content)
    f.close()

    f = open("../lyrics_process/" + file, 'w')
    f.write(" ".join(content))
    f.close()

