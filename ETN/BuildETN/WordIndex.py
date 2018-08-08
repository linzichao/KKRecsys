from pprint import pprint
from Parser import Parser
from collections import Counter
from datetime import datetime
import util
import os
import math
import copy
import json
import re

class VectorSpace:

    #Collection of document id
    documentId = []

    #Collection of document term vectors
    documentVectors = []

    #Collection of document tf-idf vectors
    documentTFIDFVectors = []

    #Mapping of vector index to keyword
    vectorKeywordIndex = {}

    #Tidies terms
    parser=None

    idfweight = []

    def __init__(self, documents={}):
        self.documentVectors=[]
        self.parser = Parser()
        if(len(documents)>0):
            self.build(list(documents.values()))


    def build(self,documents):
        """ Create the vector space for the passed document strings """
        self.vectorKeywordIndex = self.getVectorKeywordIndex(documents)


    def getVectorKeywordIndex(self, documentList):
        """ create the keyword associated to the position of the elements within the document vectors """

        #Mapped documents into a single word string
        vocabularyString = " ".join(documentList)

        vocabularyString = re.sub(r"\s+", " ", vocabularyString)
        vocabularyList = [word for word in vocabularyString.split(" ")]

        uniqueVocabularyList = util.removeDuplicates(vocabularyList)
        
        vectorIndex={}
        offset=0
        #Associate a position with the keywords which maps to the dimension on the vector used to represent this word
        for word in uniqueVocabularyList:
            vectorIndex[word]=offset
            offset+=1
        return vectorIndex  #(keyword:position)


if __name__ == '__main__':

    doc = {}

    #Read file
    print("\n\nReading files and Building vectors")
    print("Please wait...")

    for file in os.listdir("../lyrics_process"):
        f = open("../lyrics_process/" + file, 'r')
        doc[file] = f.read()
        f.close()
    
    t1 = datetime.now()

    vectorSpace = VectorSpace(doc)
    
    t2 = datetime.now()
    
    t3 = t2 - t1

    #print(vectorSpace.vectorKeywordIndex)
    #print(len(vectorSpace.vectorKeywordIndex))
    
    print("Process Time: " + str(t3.seconds/60))
    
    print("Dump json file....")
    f = open("./Word.json", "w")
    jsonarray = json.dumps(vectorSpace.vectorKeywordIndex)
    json.dump(jsonarray, f)
    f.close()

    #print(len(vectorSpace.documentVectors))

    #pprint(vectorSpace.related(1))

###################################################
