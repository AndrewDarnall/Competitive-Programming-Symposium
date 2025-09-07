""" Top K Frequent 11ms exec time """
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [item[0] for item in Counter(nums).most_common(k)]