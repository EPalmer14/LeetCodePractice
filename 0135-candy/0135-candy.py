class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candies = n  # At least one candy per kid
        i = 1

        while i < n:
            if (ratings[i] == ratings[i - 1]):
                i += 1
                continue

            increasing_neighbors = 0
            while (i < n and ratings[i] > ratings[i - 1]):
                increasing_neighbors += 1
                candies += increasing_neighbors
                i += 1
            
            if (i == n):
                return  candies
            
            decreasing_neighbors = 0
            while (i < n and ratings[i] < ratings[i - 1]):
                decreasing_neighbors += 1
                candies += decreasing_neighbors
                i += 1

            candies -= min(increasing_neighbors, decreasing_neighbors)

        return candies
   
        