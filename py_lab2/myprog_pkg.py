#!/usr/bin/python

import my_pkg

if __name__=="__main__":
	while True:
		choice =input("select menu: 1)conversion 2)union/intersection 3)exit")
		if choice=='1' : 
			num=input('이진수?')
			my_pkg.bto(num)
			my_pkg.tooct(num)
			my_pkg.tohex(num)
		elif choice=='2': 
			my_pkg.ui()
		elif choice=='3': 
			exit()
