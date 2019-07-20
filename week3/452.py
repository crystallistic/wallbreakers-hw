import math
    
def findMinArrowShots(points):
    pairs = dict()
    for pair in points:
        pairs[pair[0]] = pair[1]
    arrows = 0
    while pairs.copy().items():
        minBegin = None
        minEnd = math.inf
        for begin,end in pairs.items():  
            if minEnd > end: 
                minEnd = end
                minBegin = begin
        arrows += 1
        print(arrows)
        for begin,end in pairs.copy().items(): 
            if begin <= minEnd:
                print(begin,end)
                del pairs[begin]
    return arrows

if __name__ == "__main__":
    points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
    points = [[0,9],[1,8],[7,8],[1,6],[9,16],[7,13],[7,10],[6,11],[6,9],[9,13]]
    print(findMinArrowShots(points))
            