#to check palindrome number
def palindrome(a):
    b=a
    s=''
    while b!=0:
        c=b%10
        s=s+str(c)
        b=int(b/10)
    return s

num=int(input("Enter your number "))
res=palindrome(num)
result=int(res)
if result==num:
    print("The entered number is palindrome ")
else:
    print("The entered number is not palindrome")
