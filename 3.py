def solve(m,a):
    #print(a)
    if m==2:
        return max(0,a[0]-a[1])
    ans=0
    for i in range(1,m-1,2):
        ans+=max(0,a[i-1]+a[i+1]-a[i])
        if a[i-1]+a[i+1]-a[i]<=0:
            continue
        if a[i+1]>=a[i-1]+a[i+1]-a[i]:
            a[i+1]-=a[i-1]+a[i+1]-a[i]
        else:
            a[i+1]=0
    if m%2==0:
        ans+=max(a[m-2]-a[m-1],0)
    return ans
n=int(input())
ans=[]
for i in range(n):
    m=int(input())
    a=list(map(int,input().split()))
    min_num=solve(m,a)
    ans.append(min_num)
for i in ans:
    print(i)