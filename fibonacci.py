fibonacci = [1,2] #beggining of Fibonacci's sequence
s = 0 # sum starts at 0

while fibonacci[-1]<4000000: #repeat this while we don't hit 4,000,000
	if fibonacci[-1]%2 == 0: 
		s = s + fibonacci[-1] #if the number is divisible by two (even), we add it to he sum
	newfibonacci = fibonacci[-1] + fibonacci[-2] # the new element in the list is the sum of the last two
	fibonacci.append(newfibonacci) #adds the new element to the list

print(s) #prints the sum
