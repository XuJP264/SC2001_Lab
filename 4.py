class Node:
    def __init__(self,id):
        self.id=id
        self.degree=0
        self.nei=[]
class Graph:
    def __init__(self,n):
        self.size=n
        self.graph=[Node(i+1) for i in range(n)]
t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    g=Graph(n)
    for i in range(n-1):
        u,v=map(int,input().split())
        g.graph[u-1].nei.append(g.graph[v-1])
        g.graph[v - 1].nei.append(g.graph[u - 1])
        g.graph[u - 1].degree+=1
        g.graph[v - 1].degree += 1
    maxN=Node(-1)
    p=True
    for node in g.graph:
        if node.degree>2:
            p=False
            break
    if p==True:
        ans.append(-1)
        continue
    for i in range(n):
      #  print(type(g.graph[0].degree))
      #  print(type(maxN.degree))
        if g.graph[i].degree > maxN.degree:
            maxN=g.graph[i]
    first=Node(-1)
    first.degree=10**10
    second=Node(-1)
    second.degree = 10 ** 10
    for nei in maxN.nei:
        if nei.degree<first.degree:
            second=first
            first=nei
        elif nei.degree<second.degree:
            second=nei
    ans.append([second.id,maxN.id,first.id])
for item in ans:
    if type(item) is int:
        print(item)
    else:
        for i in item:
            print(i,end=' ')
        print('')
