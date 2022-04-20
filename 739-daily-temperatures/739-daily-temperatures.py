class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # initialize the answer list
        answer = [0] * len(T)
        stack = []

        for i, cur in enumerate(T):
            # correct if the current temparature is higher than stack value
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer