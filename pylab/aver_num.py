#!/usr/bin/python

print("몇개의 숫자를 입력할거임?")
n=int(input())
sum=0
for i in range(0,n,1):
	num=int(input())
	sum+=num

average=float(sum/n)
print(average)
 
