l=list(map(int,input().split()))
n=len(l)
for i in range(0,n):
    for j in range(0,n):
        if l[i]<l[j]:
            t=l[i]
            l[i]=l[j]
            l[j]=t
print(l)