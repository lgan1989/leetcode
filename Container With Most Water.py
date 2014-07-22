class Solution:
    # @return an integer
    def maxArea(self, height):
        n = len(height)
        l = [(height[i] , i) for i in range(n)]
        l.sort(reverse=True)
        min_val = l[0][1]
        max_val = l[0][1]
        ans = 0
        for i in range(1 , n):
            ans = max(max( abs(min_val - l[i][1]) * l[i][0] , abs(max_val - l[i][1]) * l[i][0] ) , ans)
            min_val = min(min_val , l[i][1])
            max_val = max(max_val , l[i][1])
        return ans