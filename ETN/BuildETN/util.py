import sys
#http://www.scipy.org/
try:
	from numpy import dot
	from numpy.linalg import norm
	import numpy
except:
	print("Error: Requires numpy from http://www.scipy.org/. Have you installed scipy?")
	sys.exit() 

def removeDuplicates(list):
	""" remove duplicates from a list """
	return set((item for item in list))


def cosine(vector1, vector2):
	""" related documents j and q are in the concept space by comparing the vectors :
		cosine  = ( V1 * V2 ) / ||V1|| x ||V2|| """
	return float(dot(vector1,vector2) / (norm(vector1) * norm(vector2)))

def euclideanDist(vector1, vector2):
	return numpy.sqrt(sum([numpy.power(a - b,2) for a, b in zip(vector1, vector2)]))
