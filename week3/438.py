class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
    
        ls, lp = len(s),len(p)
        if ls < lp: return []

        ans = []
        charP = sorted([c for c in p])
        charS = sorted([c for c in s[:lp]])

        if charP == charS: ans.append(0)

        for i in range(lp,ls):
            # if character to be deleted and inserted 
            # are the same then do nothing, else BAU
            if (s[i-lp] != s[i]):   
                
                # remove and add ops using binary search
                self.binaryRemove(charS,s[i-lp])
                self.binaryInsert(charS,s[i])
            
            # if anagram found, record starting index
            if charP == charS:
                ans.append(i-lp+1)
        return ans

    def binaryRemove(self,charS,letter):
        begin,end = 0, len(charS)-1
        while begin <= end:
            mid = (begin + end) // 2
            if charS[mid] == letter:
                del charS[mid]
                return
            elif charS[mid] < letter:
                begin = mid + 1
            else:
                end = mid - 1

    def binaryInsert(self,charS, letter):
        begin,end = 0,len(charS)-1

        if not charS or charS[begin] >= letter:
            charS.insert(begin,letter)
            return
        if not charS or charS[end] <= letter:
            charS.insert(end + 1,letter)
            return 

        while begin <= end:
            mid = (begin+end)//2
            if charS[mid-1] <= letter and letter <= charS[mid]:
                charS.insert(mid,letter)
                return
            elif charS[mid] < letter:
                begin = mid+1
            else:
                end = mid-1