strPalindromo = ""
intPalindromo = 0
Palindromo = 0
testetmp = 0
sair = False
for a in range(999, 100, -1):
#for a in range(99, 9, -1):
	strPalindromo = ""
	for b in range(999, 100, -1):
#	for b in range(99, 9, -1):
		teste = a*b
		strPalindromo = ""
		print "a: "+ str(a)
		print "b: "+ str(b)
		print "teste: "+str(teste)+"---\n"
		testetmp = teste
#		h = raw_input("")
		while(testetmp > 0):
			print "testetmp: "+ str(testetmp)
			strPalindromo += str(testetmp%10)
			testetmp = (testetmp - testetmp % 10) /10
		intPalindromo = int(strPalindromo)
		print "teste :"+str(teste)+"\nintPalindromo: "+strPalindromo
		if(intPalindromo == teste):
			if (teste > Palindromo):
				Palindromo = teste
			else:
				sair = True
			break
			strPalindromo = ""

	if(sair):
		break
print Palindromo
