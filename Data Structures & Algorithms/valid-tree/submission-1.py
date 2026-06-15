class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node, par):
            if node in visited:
                return True

            visited.add(node)
            for child in adj[node]:
                if child == par:
                    continue
                if dfs(child, node) == False:
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
