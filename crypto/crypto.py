from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from time import sleep


salt = b'\xa7\xa5\n\x1e\xfcW\xf8\r\xfd\x9b\x84\x96\xe7\xdbqJ\x9b6\xba\xcb2R\xc1\xf2n\x8b!\xac"\x8d\xf3\x08'
password = "1234"

key = PBKDF2(password, salt, dkLen=32)

message = b"tester one two three"

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

print(ciphered_data)

sleep(3)

with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)



with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)
