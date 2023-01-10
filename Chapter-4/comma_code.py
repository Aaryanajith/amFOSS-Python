spam = ['apples', 'bananas', 'tofu', 'cats', 'bike', 'car']
L=len(spam)

def list1(spam):
    for i in range(L-1) :
        print(spam[i], end=", ")
    spam[-1]="and"+" "+spam[-1]
    print(spam[-1])
    
list1(spam)