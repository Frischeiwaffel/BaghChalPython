class Point(object):
    """class describes a coordinate point"""
    def __init__(self, x = None, y = None):
        self.X = 0
        self.Y = 0
        if (x!=None):
            self.X = x
        if(y!=None):
            self.Y = y