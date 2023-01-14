import re

def datedetection(date):
    l=[]
    datereg=re.compile(r'(\d{2})\/(\d{2})\/(\d{4})')
    date_reg=datereg.search(date)
    date_reg_data=date_reg.groups()
    print('Date Found:' + str(date_reg_data))
    for i in date_reg_data:
        l.append(int(i))
    if l[0]>0 and l[0]<=31:
        return True
    else:
        return False
    if l[1]>0 and l[1]<=12:
        return True
    else:
        return False
    if l[2]<2000 and l[2]<=3000:
        return True
    else:
        return False
    
    

d=input("enter date")
print(datedetection(d))