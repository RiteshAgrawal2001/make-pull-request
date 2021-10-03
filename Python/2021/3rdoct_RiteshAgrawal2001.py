# Python 3 program to print
# string obtained by
# concatenation of different
# rows of Zig-Zag fashion

# Prints concatenation of all
# rows of str's Zig-Zag fashion
def printZigZagConcat(str, n):
	
	# Corner Case (Only one row)
	if n == 1:
		print(str)	
		return

	# Find length of string
	l = len(str)

	# Create an array of
	# strings for all n rows
	arr=["" for x in range(l)]

	# Initialize index for
	# array of strings arr[]
	row = 0
	
	# Traverse through
	# given string
	for i in range(l):
		
		# append current character
		# to current row
		arr[row] += str[i]

		# If last row is reached,
		# change direction to 'up'
		if row == n - 1:
			down = False

		# If 1st row is reached,
		# change direction to 'down'
		elif row == 0:
			down = True

		# If direction is down,
		# increment, else decrement
		if down:
			row += 1
		else:
			row -= 1

	# Print concatenation
	# of all rows
	for i in range(n):
		print(arr[i], end = "")
# Driver Code

str = "RITESHJAGRAWAL"

n = 3

printZigZagConcat(str, n)

 
