import hasher

key, salt = hasher.hash("fs144")

strkey = str(key)
strsalt = str(salt)

print(salt.encode('utf-8'))

print(strkey)
print(strsalt)

print(hasher.dehash(key, salt, "fs144"))
