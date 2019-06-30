class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
        occurrences = dict()
        
        # join two strings and count word occurrences
        s = A + " " + B
        for word in s.split():
            if word in occurrences:
                occurrences[word] += 1
            else:
                occurrences[word] = 1

        # return words that only occur once in the joined string      
        return [word for word in occurrences if occurrences[word] == 1]