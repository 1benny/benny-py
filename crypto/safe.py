from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


salt = b'\xba\x1c\xd4\xbd\xee]\x1f!-R\x9a\x8c)\xcc\xfd\x08\x00\x8f\xc2J\x9fX\xf4\x13\xe8\x84\xc2\x91r&B\x94'
password = "65537"

key = PBKDF2(password, salt, dkLen=32)

secret = b"user8357400686" 
secret2 = b"ybkacvx39dh9@2"
        

cipher = AES.new(key, AES.MODE_CBC)

ciphered_user = cipher.encrypt(pad(secret, AES.block_size))
ciphered_pass = cipher.encrypt(pad(secret2, AES.block_size))


print(ciphered_user)
print(ciphered_pass)

with open("vault.bin", "wb") as f:
    f.write(cipher.iv)
    f.write(ciphered_user)
    f.write(ciphered_pass)

with open("vault.bin", "rb") as f:
    iv = f.read(16)
    decrypt_user = f.read()
    decrypt_pass = f.read()
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original_p = unpad(cipher.decrypt(decrypt_user), AES.block_size)
original_u = unpad(cipher.decrypt(decrypt_user), AES.block_size)