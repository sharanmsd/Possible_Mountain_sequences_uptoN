n=int(input())
if(n==0):
    print("0")
elif(n==1):
    print("0")
elif(n==2):
    print("0")
else:
    s=0
    for i in range(1,n-1):
        s=(s*2)+2
    print(s)
