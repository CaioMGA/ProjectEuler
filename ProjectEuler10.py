total = 2
primes = [2]
for i in range(3, 2000000, 2):
	isPrime = True
	for j in primes:
		if(i % j == 0):
			isPrime = False
			break
	if isPrime:
		total+=i
		primes.append(i)
		print i
print total
