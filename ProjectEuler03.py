num = 600851475143

i = 3;
while i <= num:
	if(num %i == 0):
		divisores_i = 0
		for j in range(1, i):
			if(i%j ==0):
				divisores_i+=1
		if(divisores_i >2):
				break;
		else:
			prime = i
	i+=2
		
print prime
