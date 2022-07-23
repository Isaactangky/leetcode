# same as grid traveler problem
# move right -> gridtravel(r, c -1 )
# move down -> gridtravel(r - 1, c )
# base case: r == 1 or c == 1: only one way
# memoization: r,c as key, since gridtravel(r, c ) = gridtravel(c, r)
#              reduce the time by half
# time complexity: m values for r val and n values for c val -> m*n combinations and calls of the 
#		   gridtraveler function,  -> O(m*n)
# space: we run m recusion and stores around n valus -> O(m+n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def gridtraveler(r, c, d = {}):
            if r > c:
                key = str(c) + ',' + str(r)
            else:
                key = str(r) + ',' + str(c)
            if key in d:
                return d[key]
            if r == 0 or c == 0 :
                return 0
            if c == 1 or r == 1:
                return 1
            right = gridtraveler(r, c - 1, d)
            down = gridtraveler(r - 1,c, d)
            d[key] = right + down
            return d[key]
        
        return gridtraveler(m,n)


        