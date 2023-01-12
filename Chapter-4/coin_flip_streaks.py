import random
numberOfStreaks = 0
R=['H','T']
L=[]

numberOfStreaks=0
streak=0
for experimentNumber in range(10000):
    for i in range(100):
        a=random.choice(R)
        L.append(a)

    l=len(L)
    for i in range(l-1):
        if L[i]==L[i+1]:
            streak=streak+1
        else:
            streak=0
        if streak==6:
            numberOfStreaks+=1
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
