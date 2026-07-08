file = open("simple.txt", "r")
content = file.read()
print(content)

import os
import shutil
import os.path

os.mkdir("test")
# var=os.path.exists("test")
# print(var)
os.rmdir("test")
# shutil.rmtree('')  // use to delete complete folder remove tree