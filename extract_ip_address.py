import os
import re

url=input("Enter website URL : ")
os.system("ping "+url+">site.txt")
f=open("site.txt")

pat="\d+\.\d+\.\d+\.\d"
match=re.search(pat,f.read())
if match==None:
    pass
else:
    print(match.group())
f.close()