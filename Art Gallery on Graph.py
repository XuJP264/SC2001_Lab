class graph:
    def __init__(self,n):
        self.size=n
        self.nodes=[node(i+1) for i in range(n)]
    def addEdge(self,a,b):
        self.nodes[a-1].neighbor.append(self.nodes[b-1])
        self.nodes[b-1].neighbor.append(self.nodes[a-1])
    def addH(self,a,h):
        self.nodes[a-1].h=h
class node:
    def __init__(self,id):
        self.id=id
        self.neighbor=[]
        self.h=-1
    def add_neighbor(self,n):
        self.neighbor.append(n)
def bfs(node,graph):
    memory=[False for _ in range(graph.size)]
   # print(memory)
    queue=[]
    head=tail=0
    queue.append([node,0])
    tail+=1
    #print("node:",node.id)
    while tail-head>0:
        cur=queue[head]
        #print(cur[0].id,cur[0].h)
        #print(queue)
        memory[cur[0].id-1]=True
        head+=1
        if cur[0].h>=cur[1]:
            return True
        for neighbor in cur[0].neighbor:
            if memory[neighbor.id-1] == False:
                queue.append([neighbor,cur[1]+1])
                tail+=1
    return False
def solve(graph1):
    ans=[]
    for i in range(graph1.size):
        if bfs(graph1.nodes[i],graph1):
            ans.append(i+1)
    print(len(ans))
    for node in ans:
        print(node,end=' ')
n, m, k = map(int, input().split())
graph1=graph(n)
for i in range(m):
    a,b=map(int,input().split())
    graph1.addEdge(a,b)
for i in range(k):
    a,h=map(int,input().split())
    graph1.addH(a,h)
solve(graph1)