n=0
a=1
num=input("enter number")
while n<len(num):
    a=int(num[n])*a
    n=n+1
print(a)