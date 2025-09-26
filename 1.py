def issys(n,a,b):
    if b>a and b%2==n%2:
        return 'YES'
    elif b%2==n%2 and a%2==n%2:
        return 'YES'
    else:
        return 'NO'
t=int(input())
ans=[]
for i in range(t):
    n,a,b=map(int,input().split())
    ans.append(issys(n,a,b))
for i in range(t):
    print(ans[i])