class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
        counter = collections.Counter()
        
        for cp in cpdomains:
            split = cp.split()
            count = int(split[0])
            
            address = split[1]
            counter.update({address:count})
            for i in range(len(address)):
                if address[i] == ".":
                    counter.update({address[i+1:]:count})
        
        return [str(counter[sd]) + " " + sd for sd in counter]
        
        
"""
Solution with defaultdict (better overall performance)

class Solution(object):
    def subdomainVisits(self, cpdomains):
        
        
        counter = collections.defaultdict(int)
        
        for cp in cpdomains:
            split = cp.split()
            count = int(split[0])
            
            address = split[1]
            counter[address] += count
            for i in range(len(address)):
                if address[i] == ".":
                    counter[address[i+1:]] += count
        
        return [str(counter[sd]) + " " + sd for sd in counter]
        
        
"""        