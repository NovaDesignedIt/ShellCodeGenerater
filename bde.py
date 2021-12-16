from cryptography.fernet import Fernet
from itertools import zip_longest
import binascii
import filecmp

#DEBUG
#testtext = "test.exe"
#testtextcpy = "test-copy.exe"
#ACC

#test files
testtext = ""  
#Test files copies
testtextcpy = ""

mfile = open(testtext,'rb')
lines = mfile.read()
linecmp = lines
	#mfile.seek(0)
	#print (mfile.read())
key = Fernet.generate_key()
fernet = Fernet(key)

def _encrypt(_bytes_):
        #bytes to string then encrypt [ string ]
        encMessage = fernet.encrypt(_bytes_)
             #print("original string: ",line)
        print("[*] encrypting string")
        #string back into bytes  
        return encMessage

def _decrypt(_enc_):
        #bytes backinto string for decryption
        dencMessage = fernet.decrypt(_enc_)
             #print("encrypted string: ",line)
        print("[*] decrypted string ")
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

def flatten(t):
    return [item for sublist in t for item in sublist]

def write_raw(_str_bytes,keys):
    length = len(keys)
    fw =open("lego.txt",'w')
    f_encrypted_write = open("naked_lego.txt",'w')
    f_encrypted_write.write(_str_bytes.decode('utf-8'))
    fw.write(str(length)+"!"+_str_bytes.decode('utf-8')+keys.decode('utf-8'))
    fw.close()


def write_definition(_str_bytes_):
    fw = open("lego.txt","w")
    fw.write("_lego_blocks = \"")
    fw.write(_str_bytes_.decode())
    fw.write("\"")


#print (lines)
print ("----")
#save this you might need this for later
enc_msg = _encrypt(lines)
print ("----")
dec_msg = _decrypt(enc_msg)
#write file
 
write_raw(enc_msg,key)
#write_definition(enc_msg)
file_write = open(testtextcpy,'wb')

file_write.write(bytes(dec_msg))

#why does it bass this test but not the 
#if(lines == dec_msg):
#	result = True
mfile.close()
file_write.close()

#result =filecmp.cmp("test.exe","test-copy.exe")    
result = compare_binaries(testtext,testtextcpy)
print ("[*]result: ",result )
print ("[*]key: ",key)
print ("[*]fernet: ",fernet)
#Succesfully encrypted a exe and back and forth.

#phase II 
#to write encrypted to txt file  with definitions
key_file = open("keys.txt",'wb')
key_file.write(key)
f1 = open("enc.exe",'wb')
f1.write(enc_msg)



