🔍 re.sub r -> escape 처리(\만 넣어도 \ 2개 넣은 효과)

참고 : https://yganalyst.github.io/data_handling/memo_6/#4-%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D-r%EC%9D%98-%EC%9D%98%EB%AF%B8

# solution 1


 class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = [word for word in re.sub('[^\w]', ' ', paragraph)
                 .lower().split() if word not in banned]

        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
