#!/usr/bin/python

n=int(input("생성할 피보나치 수?"))


fibo=[0,1,1]
sum=0
f1=1
f2=1
if n==1:
	print(fibo[1])
elif n==2:
	print(fibo[2])	
else:
	for i in range(3,n+1):
		sum=f1+f2
		f1=f2
		f2=sum
		fibo.append(sum)

print('Fn피보나치수 출력%d'%(sum))
	
for j in range(1,n+1):
	print("%d " %fibo[j] ,end="" )
