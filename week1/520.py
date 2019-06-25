class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        beg,end = 65, 65+25
        
        allCaps = True
        allLow = True
        camel = True
        
        for i in range(len(word)):
            if ord(word[i])<beg or ord(word[i]) >  end:
                allCaps = False   
            else:
                if i > 0:
                    camel = False
                allLow = False
                
        return (allCaps or allLow or camel)