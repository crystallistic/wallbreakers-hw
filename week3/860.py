class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        # keep track of bills I have
        myBills = collections.defaultdict(int)
        
        # go through each customer
        for bill in bills:   
            
            # keep track of total amount
            amount = bill 
            
            # while I have at least 1 bill and the amount > 5
            while myBills and amount > 5:        
                          
                # find the biggest bill that is < ammount
                myMaxBill = 0
                for myBill in myBills:
                    if myBill > myMaxBill and myBill < amount:
                        myMaxBill = myBill
                
                # subtract from amount
                amount -= myMaxBill
                
                # decrease count of this bill
                if myBills[myMaxBill] > 0:    
                    myBills[myMaxBill] -= 1
                    if myBills[myMaxBill] == 0:
                        del myBills[myMaxBill]
                else:
                    return False # return False if no bill available
            
            # if there's no exact change, return False
            if amount != 5:
                return False
            
            # add bill to my bills
            myBills[bill] += 1
    
        return True