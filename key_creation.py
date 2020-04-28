#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Import required modules
'''
import sys
from platform import system

'''
    Import external files
'''
import version
from creation import nix

__author__  = "Jason Brown"
__email__   = 'jason@jasonbrown.us'
__version__ = '0.5'
__license__ = 'Apache'
__status__  = 'Test'
__date__    = '20190731'


def main():


# Detect operating system type and assign the correct directory
  osplat = system()

  try:
    if osplat == 'Linux':
      operatingsystem = 'nix'
    elif osplat == 'Darwin':
      operatingsystem = 'nix'
    elif osplat == 'Windows':
      operatingsystem = 'ms'
    else:
      exit
  except:
    sys.exc_info()

  if len(sys.argv) < 2:
    print ('Type ./key_generation.py --help for options')
    sys.exit()
  if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'help':
        print ('Usage ./key_generation.py [option]\n\
            --create\n\
            --version\n\
            ')
    elif option == 'create':
        nix.ssh()
    elif option == 'version':
        version.main()
    else:
        print ('No option provided')


if __name__ == '__main__':
	main()
