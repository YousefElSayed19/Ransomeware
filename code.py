from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter
import os
import os.path


counter = Counter.new(128)   # => 128 bit  = 16 byte  #blocksize  16 byte 

key = b'\xc5f\xe4\xd5F\x88\xbf_\xfc\xc5\xfa\xcd\xe7\xca\x19\xba'
# key = Random.new().read(32)

c = AES.new(key,AES.MODE_CTR,counter=counter)

word = "hi this is encryption"

encrypted_word = c.encrypt(word.encode('ascii'))




#### decrypt with c.decrypt

# cipher = b'\xcd\x8e!]\xa0\x19\xddc\xe3=)\xd7\x02\xbe:\xca\x1f\xbe\xa8\xcd\xc4'
# test = c.decrypt(cipher)
# print(test)