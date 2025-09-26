class node:
    def __init__(self,id):
        self.id=id
        self.kids=[]
class Tree:
    def __init__(self,n):
        self.nodes=[node(i+1) for i in range(n)]
def solve(n,parent):
    tree=Tree(n)
    for i in range(n-1):
        tree.nodes[parent[i]-1].kids.append(tree.nodes[i+1])
    ans=[0 for _ in range(n)]
    queue=[]
    head=tail=0
    queue.append(tree.nodes[0])
    tail+=1
    while head<tail:
        cur=queue[head]
        head+=1
        ans[len(cur.kids)]+=1
        for kid in cur.kids:
            queue.append(kid)
            tail+=1
    for item in ans:
        print(item,end=' ')
    return ans
n=int(input())
parent=list(map(int,input().split()))
solve(n,parent)