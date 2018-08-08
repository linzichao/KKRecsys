#http://tartarus.org/~martin/PorterStemmer/python.txt
import re
import nltk

class Parser:

    #A processor for removing the commoner morphological and inflexional endings from words in English

        stemmer = None

        lemmatizer = None

        stopwords=[]

        def __init__(self,):

                self.stemmer = nltk.stem.LancasterStemmer()

                self.lemmatizer = nltk.stem.WordNetLemmatizer()

                #English stopwords from ftp://ftp.cs.cornell.edu/pub/smart/english.stop
                self.stopwords = open('english.stop', 'r').read().split()


        def removeStopWords(self,list):
            """ Remove common words which have no search value """
            return [word for word in list if word not in self.stopwords ]


        def tokenise(self, string):
            """ break string up into tokens and stem words """
            string = re.sub(r"\s+", " ", string)

            words = [ self.stemmer.stem(self.lemmatizer.lemmatize(word)) for word in string.split(" ") ]

            return words
