n,m,a=map(int,input().split())

if m%a==0:
    value1=n//a
else:
    value1=n//a+1

if m%a==0:
    value2=m//a
else:
    value2=m//a+1

print(value1*value2)
