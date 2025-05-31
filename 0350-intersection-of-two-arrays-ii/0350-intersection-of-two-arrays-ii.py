class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictt = {}
        res = []

        for num in nums1:
            if num in dictt:
                dictt[num] += 1
            else:
                dictt[num] = 1

        for num in nums2:
            if num in dictt and dictt[num] != 0:
                dictt[num] -=1
                res.append(num)
        return res