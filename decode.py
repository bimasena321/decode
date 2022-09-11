import os
import base64


print("=================decode===========================")

bbn = input("decode: ")
ed = base64.b64decode(bbn).decode('utf-8')
print (ed)
