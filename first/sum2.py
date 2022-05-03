b=input()
for i in range(a):
    z=int(input())
    l=list(map(int,input().split()))
    c=0
    for j in range(1,z):
        if(l[j-1]!=l[j]):
            if((j-1)==0):
                c=c-1
            c=c+2
    print(c)
