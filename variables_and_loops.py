import numpy as np #np is short hand for numpy

def main():
	i =0
	n = 10
	x = 119.0	#float x, 
	
#we can use numpy to quickly make arrays
	y = np.zeros(n,dtype=float) #declares 10 zero
	
	for i in range(n):  	#i in range [0,n-1]
		y[i] = 2.0 * float(i) + 1.0	#set  y=2i+1 a
	
	#we can iterate through the y elements one by one
	for y_element in y:
		print(y_element)
		
#excuse the main function
if __name__ == "__main__":
	main()