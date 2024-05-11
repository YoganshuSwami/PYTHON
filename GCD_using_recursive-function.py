def GCD(x,y):
    rem = x%y
    if (rem==0):
        return y
    else:
        return GCD(y,rem)
    
a = int (input ("Enter the first number: "))
b = int (input ("Enter the second number: "))
print("The GCD of numbers is :  ", GCD(a,b))