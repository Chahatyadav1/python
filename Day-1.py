file = open("simple.txt", "r")
content = file.read()
print(content)

import os
import os.path

os.mkdir("test")
# var=os.path.exists("test")
# print(var)
os.rmdir("test")
