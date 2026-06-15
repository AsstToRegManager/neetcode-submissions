class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = {i:[] for i in range(n)}
        for c, p in edges:
            edgeMap[c].append(p)
            edgeMap[p].append(c)

        visit = set()
        def dfs(curr, prev):
            if curr in visit:
                return False
            
            visit.add(curr)
            for i in edgeMap[curr]:
                if i == prev:
                    continue
                if not dfs(i, curr):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)
