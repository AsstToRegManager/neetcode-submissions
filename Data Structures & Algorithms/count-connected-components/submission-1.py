class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgeMap = {i:[] for i in range(n)}
        for n1, n2 in edges:
            edgeMap[n1].append(n2)
            edgeMap[n2].append(n1)

        visit = set()
        def dfs(curr, prev):
            if curr in visit:
                return 
            
            visit.add(curr)
            for neigh in edgeMap[curr]:
                dfs(neigh, curr)
        
        count = 0
        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i, -1)
        return count


        