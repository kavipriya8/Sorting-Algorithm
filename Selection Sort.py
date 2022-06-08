s=list(map(int,input().split()))
n=len(s)
k=0
for i in range(0,n):
    m,b=s[i],s[i]
    for j in range(i+1,n):
        if m>s[j]:
            m=s[j]
            k=j
    if m!=b:
        t=s[i]
        s[i]=m
        s[k]=t
print(s)