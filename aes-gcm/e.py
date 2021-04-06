'''
Descripttion:aes-gcm-e
stu_id: 20182132025
stu_name: 苏佳彬
Author: kok-s0s
LastEditTime: 2021-04-06 23:58:47
'''
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

header = b"header"
data = b"secret"
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_GCM)
cipher.update(header)
ciphertext, tag = cipher.encrypt_and_digest(data)

json_k = ['nonce', 'header', 'ciphertext', 'tag']
json_v = [
    b64encode(x).decode('utf-8')
    for x in [cipher.nonce, header, ciphertext, tag]
]
result = json.dumps(dict(zip(json_k, json_v)))
print(result)
