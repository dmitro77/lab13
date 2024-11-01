class Lake(object):
    name = ""
    continent = ""
    surfaceArea = 0
    depth = 0
    
    def __init__(self, name, continent, surfaceArea, depth):
        self.name = name
        self.continent = continent
        self.surfaceArea = surfaceArea
        self.depth = depth
    
    def __del__(self):
        print(self.name + " deleted")
        
    def setSurfaceArea(self, surfaceArea):
        self.surfaceArea = surfaceArea
    
    def setDepth(self, depth):
        self.depth = depth
