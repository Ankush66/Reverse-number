#finding the biggest three number
#big.py
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of C:"))
#logic
big=a
if(b>big):
    big=b
if(c>big):
	big=c
print("big({},{},{})={}".format(a,b,c,big))