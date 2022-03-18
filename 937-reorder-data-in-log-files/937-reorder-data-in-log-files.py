class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        result = []
        digitList, strList = [], []

        for id in logs:
            # if this is a number log
            if id[len(id) - 1].isdigit():
                digitList.append(id)
            # if this is a string log
            else:
                strList.append(id)

        # sort
        strList.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return strList + digitList