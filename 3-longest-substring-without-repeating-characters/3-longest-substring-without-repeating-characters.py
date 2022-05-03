class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        bucket, max_length = [], 0

        for char in s:
            if char not in bucket:
                bucket.append(char)
            else:
                idx = bucket.index(char) + 1
                while idx:
                    bucket.pop(0)
                    idx -= 1
                bucket.append(char)
            max_length = max(max_length, len(bucket))
            
        return max_length