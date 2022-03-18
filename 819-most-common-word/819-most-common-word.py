class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        newParagraph, result = "", ""
        
        # unification delimeter
        paragraph = paragraph.replace(',',' ')

        # remove special character
        for char in paragraph:
            if char.isalnum() or char == ' ':
                newParagraph += char

        # split paragraph
        words = newParagraph.split()

        # except banned
        for ban in banned:
            for char in words:
                if ban == char:
                    words.remove(char)
                elif ban == char.lower():
                    words.remove(char)

        # from upper to lower
        for i in range(len(words)):
            words[i] = words[i].lower()

        result = collections.Counter(words).most_common(1)
        return result[0][0]