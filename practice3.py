#Function to check armstrong number
def armstrong(a):
    sum=0
    num=a
    b=a
    while b!=0:
        a=b%10
        sum+=a**3
        b=int(b/10)
    if sum==num:
        print("armstrong number")
    else:
        print("Not armstrong")
doagain='yes'
while doagain=='yes':
    num=int(input("Enter any num  "))
    armstrong(num)
    doagain=input("Enter your choice")
