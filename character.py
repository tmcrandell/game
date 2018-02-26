Class Character(self,x,y):
    def __init__(self):
        # la di da di da
        self.x=x
        self.y=y
        pass
    # def ...
    def move(self,xdir,ydir):
        self.x+=xdir
        self.y+=ydir
    def draw(self, surf):
        pygame.draw.rect(surf,RED,self.x,self.y,10,10)
