class Solution:
    
    def merge(self, intervals):
        

        if len(intervals) == 0: return []
        
        # sort intervals based on the start of each interval
        intervals.sort(key= lambda x: x[0])
        
        merged = [intervals[0]]

        for i in intervals:
            # if begin of current interval <= end of last interval in merged list, merge them
            if i[0] <= merged[-1][-1]:
                merged[-1] = [merged[-1][0], max(i[-1],merged[-1][-1])]
            # else append current interval to merged list
            else: 
                merged.append(i)
                
        return merged