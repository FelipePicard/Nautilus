s = 0

for x in range(1000): #x goes from 0 to 1000 (always adding 1 to x)
	if x%3 == 0:
		s = s + x #if x is divisible by 3, add x to the sum
	elif x%5 == 0:
		s = s + x #if x is divisible by 5, add x to the sum

print (s) #prints the sum
