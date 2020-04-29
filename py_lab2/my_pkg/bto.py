#!/usr/bin/python



def bto(num):
	L=list(str(num))
	flag=len(L)
	sum=0

	for i in L:
		if int(i)==1:
			sum+=pow(2,flag-1)
		else :
			sum=sum
		flag=flag-1
	print("=>DEC",end="")
     
	print(sum)

def tooct(num):
	L=list(str(num))
	flag=len(L)
	sum=0

	for i in L:
		if int(i)==1:
			sum+=pow(2,flag-1)
		else :
			sum=sum
		flag=flag-1

	print("=>OCT",end="")
	print("%o"%sum)

def tohex(num):
	L=list(str(num))
	flag=len(L)
	sum=0

	for i in L:
		if int(i)==1:
			sum+=pow(2,flag-1)
		else :
			sum=sum
		flag=flag-1

	print("=>HEX",end="" )
	print("%x"%sum)


if __name__== '__main__':
	print('this it bto')
	 

