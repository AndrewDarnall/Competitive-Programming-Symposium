""" Group Anagrams 35ms exec time """
class Solution(object):
    def groupAnagrams(self, strs):
        """
        Groups anagrams using a character count tuple as the hash map key.
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            anagram_map[tuple(count)].append(s)

        return list(anagram_map.values())