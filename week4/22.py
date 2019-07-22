from copy import deepcopy

def generateParenthesis(n):
    ans = []
    backtrack("",0,0,ans,n)
    return ans

def backtrack(s,left,right,ans,n):
    if len(s) == 2 * n:
        ans.append(s)
        return
    if left < n:
        backtrack(s+'(',left+1,right,ans,n)
    if right < left:
        backtrack(s+')',left,right+1,ans,n)

if __name__ == "__main__":
    n = 3
    print(generateParenthesis(n))