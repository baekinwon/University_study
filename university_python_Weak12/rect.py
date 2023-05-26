class Rect:
    count = 0
    
    def __init__(self,width,height):
        self.width, self.height = width,height
        Rect.count +=1
        self.rectid = 'rectid_'+str(Rect.count)
    
    def get_area(self):
        return (self.width*self.height)
    
    def get_peri(self):
        return 2*(self.width+self.height)
        
if __name__ == '__main__':
    r1 = Rect(3,5)
    r2 = Rect(4,7)
    print('r1 (width,height,count)=',r1.width,r1.height,r1.count)
    print('r2 (width,height,count)=',r2.width,r2.height,r2.count)
    
    
    print(r1.get_area())
    print(r1.get_peri())
    print(r2.get_area())
    print(r2.get_peri())