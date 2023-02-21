#number of even digits in a given number
n = int(input("Enter a number: "))
while (n>0):
    e=0
    o=0
    r = n%10
    if r%2==0:
        e=e+1
    else:
        o=o+1
    n = int(n/10)
print(e)
print(o)
        

        
        
