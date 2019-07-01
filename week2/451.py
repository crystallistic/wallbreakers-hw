class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        
        ans = ""
        for w,count in count.most_common():
            ans += w*count
        return ans

"""

Less efficient one-liner solution

class Solution(object):
    def frequencySort(self, s):   
        return "".join(w*count for w,count in collections.Counter(s).most_common())
"""