'''
Descripttion:des-cbc
stu_id: 20182132025
stu_name: 苏佳彬
Author: kok-s0s
LastEditTime: 2021-04-06 21:50:29
'''
from Crypto.Cipher import DES

key = b'-8B key-'
cipher = DES.new(key, DES.MODE_CBC)
plaintext = b'sona si latine loqueris '
msg = cipher.iv + cipher.encrypt(plaintext)
print(msg)

# import base64
# import hashlib
# from Crypto.Cipher import DES

# passphrase = "123456"  # Key used to encrypt
# # Salt randomly generated at encrypt-time, and stored at
# # the beginning of the encrypted data:
# salt = base64.b64decode("vqmy2fiCipU=")
# enc_b64 = "vqmy2fiCipVBIhiAzDfvTL0301DLgTqd"
# enc_data = base64.b64decode(enc_b64)
# if (salt != enc_data[0:8]):
#     raise Exception("Salt does not match enc_data salt")
# enc_data = enc_data[8:]

# m = hashlib.md5()
# m.update(passphrase.encode())
# m.update(salt)
# result = m.digest()

# print(result)

# for i in range(1, 1000):
#     m = hashlib.md5()
#     m.update(result)
#     result = m.digest()

# # value of result is: md5("123456" + salt) iterated 1,000 times.

# key = result[:8]
# iv = result[8:16]
# des = DES.new(key, DES.MODE_CBC, iv)
# print(des.decrypt(enc_data).decode())
# # > Hello World
