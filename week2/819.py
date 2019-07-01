class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        r = r"[\b\w\b]+"
        
        words = re.findall(r,paragraph.lower())
        counter = collections.defaultdict(int)
        
        for w in words:
            counter[w] += 1           
        
        word = ""
        maximum = 0
        
        for w in counter:
            if w not in banned and maximum < counter[w]:
                word = w
                maximum = counter[w]
        return word