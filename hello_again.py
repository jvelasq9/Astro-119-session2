#include the Numpy library 
import numpy as np

#define the main() function
def main():
	i = 0
	x=119.0
	
	for i in range(120): #loops i from 0 through 190.0
		if((i%2)==0):    # % is the remainder. if i is even
			x += 3.0   	# += x equals x+3
		else:			#if i odd
			x -=5.0        #x = x-5
	s = "%3.2e" % x  #make a string that shows x with scientific notation
	
	print(s)
	
	
#now the rest of the program
if __name__ == "__main__":
	main()
	

#continue 