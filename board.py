class board:
    def __init__(self, rowSize, colSize):
        self.rowSize = rowSize
		self.colSize = colSize
        self.hits = [[]]
        self.misses = [[]]
		
    def isMiss(self, xPos, yPos):
        if(self.misses[xPos][yPos] == True):
            return True
        
        return False
		
    def isHitt(self, xPos, yPos):
        if(self.hits[xPos][yPos] == True):
            return True
        
        return False
        
    def getSize(self):
        return (self.rowSize, self.colSize)
