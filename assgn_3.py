n=int(input("Enter the number of terms you want to print"))
a=0
b=1
c=0

if n<=0:
    print("incorrect input")
elif n==1:
    print("0")
elif n==2:
    print("0, 1")
else:
    print(a)
    print(b)
    for i in range (n-2):
        c=a+b
        print(c)
        a=b
        b=c
    