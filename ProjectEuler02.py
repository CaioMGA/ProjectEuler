limit = 4000000
i = 2
oldi = 1
soma = 2
while (i+oldi)< limit:
	x = i
	i+=oldi
	oldi = x
	if(i%2==0):
		soma+=i;
print soma
