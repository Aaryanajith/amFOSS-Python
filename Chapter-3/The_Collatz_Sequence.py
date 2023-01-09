def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2

    elif number%2!=0:
        print(3*number+1)
        return 3*number+1

try:
    num=int(input("Enter a number"))
    print(collatz(num))
    
except ValueError:
    print("The number must be an integer")