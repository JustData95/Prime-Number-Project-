import math 
import numpy
np.set_printoptions(threshold=np.inf)

def sieve(n):
	A = [False, False]+ [True]*(n-1)
	for x in range (2, int(math.sqrt(n)+1)):
		if A[x]: 
			for J in range(x**2, n+1, x):
				A[J] = False


	print(np.where(A)[0])
	
sieve(10)

#SUBLIME TEXT DOES NOT HAVE THE NUMPY MODULE. USE JUPYTER NOTEBOOK OR ANOTHER COMPILER/PROGRAM THAT RUNS PYTHON CODE