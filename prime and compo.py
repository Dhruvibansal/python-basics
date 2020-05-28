# DHRUVI BANSAL 

prime = []
compo = []

for num in range(2,101):
	flag = 1
	for i in range (2,num):
		if num%i == 0:
			flag = 0
			break
	if flag == 1:
		prime.append(num)
	else:
		compo.append(num)


for i in range (len(prime)):
	print (prime[i] , '	' , compo[i])

for i in range(len(prime),len(compo)):
	print ('  	' , compo[i])


