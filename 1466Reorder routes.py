class Solution:
    def minReorder(self, n, connections):
        graph=[[] for _ in range(n)]
        for line in connections:
            graph[line[0]].append(line[1])
            graph[line[1]].append(-line[0])
        queue=[]
        queue.append(0)
        change=0
        p=[False]*n
        print(graph)
        while len(queue)>0:
            print(queue)
            cur=queue.pop(0)
            p[cur]=True
            for ver in graph[cur]:
                if p[cur]==False and ver<0:
                    queue.append(abs(ver))
                    change+=1
        return change
