


def maximum(a, b, c):

	if (a >= b) and (a >= c):
		largest = a

	elif (b >= a) and (b >= c):
		largest = b
	else:
		largest = c
		
	return largest



a = int(input("enter the number: "))
b = int(input("enter the number: "))
c = int(input("enter the number:"))
print(maximum(a, b, c))
