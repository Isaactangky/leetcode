# dfs all the computer connected to the same network
# mark an edge as extra if we visit the same computer again
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        link = collections.defaultdict(list)
        # mark edges
        for start, end in connections:
            link[start].append(end)
            link[end].append(start)
       
        visited = [False] * n
        diff_network = 0
        extra_edges = [0]
        
        def dfs(i, pre):
            visited[i] = True
            for comp in link[i]:
                # comp > i: avoid double counting the cables
                # we start from 0, 1, 2..., an entra link between i and j will be marked at i's bfs
                # at j's bfs, as j > i, we dont count this edge as extra
                # e.g. 0 -> 1 - > 2 -> 0:  at 0 ,we mark 1, 2 as visited, 
                # at 1, the link to 2 is redundant (an extra edge) 
                # at 2, the link to 1 has already be counted, no need to rise extra_edges
                if comp != pre and visited[comp] and comp > i:
                    extra_edges[0] += 1
                elif comp != pre and not visited[comp]:
                    dfs(comp,pre)
            return
        
        for i in range(n):
            if not visited[i]:
                dfs(i, -1)
                diff_network += 1
        # diff_network - 1 edges is needed to connect all networks
        if diff_network - 1 > extra_edges[0]:
            return -1
        return diff_network - 1
    
    # Modified: To connect n computers, we need at least n - 1 connections 
    # simplyfied to a classic graph problem
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n - 1: return -1
        
        link = collections.defaultdict(list)
        for start, end in connections:
            link[start].append(end)
            link[end].append(start)
        visited = [False] * n
        diff_network = 0

        def dfs(i):
            visited[i] = True
            for comp in link[i]:
                if not visited[comp]:
                    dfs(comp)
                    
        for i in range(n):
            if not visited[i]:
                dfs(i)
                diff_network += 1
        #print(diff_network, extra_cables)
        return diff_network - 1
        
            
        
        
            
        
