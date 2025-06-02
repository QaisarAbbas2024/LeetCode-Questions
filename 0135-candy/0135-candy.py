class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Make a list 'candy_list' with same length as ratings
        # Each child gets 1 candy at start
        candy_list = [1] * len(ratings)

        # Traverse the ratings from Left to Right
        """ Here, Child on right gets 'one more candy' if they have a higher rating
        than the child on the left """
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy_list[i] = candy_list[i-1] +1

        # Traverse the ratings from Right to Left
        """ Here is to ensure that if a Child has a higher rating than its next Child,
        they get more candies """
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1] and candy_list[i] <= candy_list[i+1]:
                candy_list[i] = candy_list[i+1] +1
        
        # Return the total no. of candies required
        return sum(candy_list)