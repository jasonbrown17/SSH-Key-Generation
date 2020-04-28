from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from shutil import copy
from platform import system
import getpass, os, sys

'''
	Generate SSH key
'''
def ssh():

    # Detect operating system type and assign the correct directory
    osplat = system()
    try:
        if osplat == 'Linux':
            homedir = '/home/'
        elif osplat == 'Darwin':
            homedir = '/Users/'
        else:
            exit
    except:
        sys.exc_info()


    # Get the current username and join it with the home directory
    usrname = getpass.getuser()
    usrdir = ''.join([homedir,usrname])


    # Check if directory and PEM file exists
    if not os.path.isdir(usrdir+'/.ssh'):
        print ('Creating .ssh directory')
        os.system('mkdir '+usrdir+'/.ssh')

    if os.path.isfile(usrdir+'/.ssh/id_'+usrname+'.pem') == True:
        print ('File already exists')
        sys.exit()

    print ('Enter a SSH key passphrase')
    passwd_in = getpass.getpass('Passphrase: ')
    priv_key = ec.generate_private_key(ec.SECP521R1(), default_backend())

    with open(usrdir+'/.ssh/priv_key.pem', 'w') as pk:
	        pk.write(priv_key.private_bytes(
    	        encoding=serialization.Encoding.PEM,
    	        format=serialization.PrivateFormat.TraditionalOpenSSL,
    	        encryption_algorithm=serialization.BestAvailableEncryption(passwd_in)
                ))

    os.rename(usrdir+'/.ssh/priv_key.pem', usrdir+'/.ssh/id_'+usrname+'.pem')
    os.system('chmod 400 '+usrdir+'/.ssh/id_'+usrname+'.pem')
    os.system('ssh-keygen -y -f '+usrdir+'/.ssh/id_'+usrname+'.pem -P '+passwd_in+'> '+usrdir+'/.ssh/id_'+usrname+'.pub')
    copy(usrdir+'/.ssh/id_'+usrname+'.pub', usrdir+'/Desktop/id_'+usrname+'.pub')