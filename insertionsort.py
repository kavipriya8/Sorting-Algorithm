s=list(map(int,input().split()))
for i in range(1,len(s)):
    for j in range(i-1,-1,-1):
        if s[j]>s[i]:
            t=s[i]
            s[i]=s[j]
            s[j]=t
        i=j
print(s)
