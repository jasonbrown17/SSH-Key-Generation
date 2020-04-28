#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def main()

	try:
		import pip
	except ImportError:
		print ('Installing pip\n\
			Enter in your login credentials')
		os.system('sudo easy_install pip')


	print ('Installing required modules')
	os.system('pip install -r requirements.txt')

if __name__ == '__main__':
	main()