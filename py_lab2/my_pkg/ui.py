#!/usr/bin/python


def ui():
	str1=input('1st list:')
	str2=input('2nd list:')

	str1=str1.replace("[","")
	str1=str1.replace("]","")
	str2=str2.replace("[","")
	str2=str2.replace("]","")
	str1=str1.replace(",","")
	str2=str2.replace(",","")
	str1=str1.replace(" ","")
	str2=str2.replace(" ","")

	list1=[]
	list2=[]

	for i in range(0,len(str1)):
		list1.append(str1[i])
	for j in range(0,len(str2)):
                list2.append(str2[j])

	
	intersection=list(set(list1)&set(list2))
	union=list(set(list1)|set(list2))

	for i in range(0,len(union)):
		union[i]=int(union[i])

	for j in range(0,len(intersection)):
		intersection[j]=int(intersection[j])

	union.sort()
	intersection.sort()

		

	print('=>union',end="")
	print(union)
	print('=>intersection',end="")
	print(intersection)

	if __name__=='__main__':
		print("this is union")
	
