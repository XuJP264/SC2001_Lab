from math import sqrt
def mp(k,pl):
    for i in pl:
        if k%i!=0:
            return i
def opr(a,k,pl,n):
    max_prime=mp(k,pl)
    r0=k%max_prime
    b=[]
    for i in range(n):
        r=a[i]%max_prime
        n=0
        while (r+n*r0)%max_prime!=0:
            n+=1
        b.append(n*k+a[i])
    #print('b:',b)
    return b
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0和1不是质数
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]
pl=sieve(int(sqrt(10**9)))
#print(pl)
t = int(input())
ans=[]
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = opr(a,k,pl,n)
    ans.append(b)
for i in range(t):
    for j in range(len(ans[i])):
        print(ans[i][j],end=' ')
    print('')
