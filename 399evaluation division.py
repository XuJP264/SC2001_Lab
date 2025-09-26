class Solution:
    def __init__(self):
        self.visits = []

    def calcEquation(self, equations, values, queries):
        edges = {}
        vers = {}

        for i, equation in enumerate(equations):
            a, b = equation
            edges[(a, b)] = values[i]
            edges[(b, a)] = 1 / values[i]

            vers.setdefault(a, set()).add(b)
            vers.setdefault(b, set()).add(a)

        answers = []
        for query in queries:
            start, end = query
            if start not in vers or end not in vers:
                answers.append(-1.0)
                continue
            self.visits = []
            if start == end:
                answers.append(1.0)
                continue
            ans = self.dfs(query, edges, vers, start, 1.0)
            answers.append(ans)
        return answers

    def dfs(self, query, edges, vers, cur, ans):
        if cur == query[1]:
            return ans
        self.visits.append(cur)
        for ver in vers[cur]:
            if ver not in self.visits:
                res = self.dfs(query, edges, vers, ver, ans * edges[(cur, ver)])
                if res != -1:
                    return res
        return -1.0
