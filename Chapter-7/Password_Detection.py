import re

def strongpassword(password):
    passregx=re.compile(r'(\w{8})')
    passregx.findall(password)
    return True

password=input(">")
a=len(password)
if a<8:
    print("False")
else:
    print(strongpassword(password))