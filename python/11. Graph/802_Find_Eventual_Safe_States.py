class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        safe = {}
        def dfs(i):
            if  i in safe:
                return safe[i]
            safe[i] = False
            
            for node in graph[i]:
                if not dfs(node):
                    return False
            
            safe[i] = True
            
            return True

        for i in range(len(graph)):

            if  dfs(i):
                res.append(i)
        return res
            
