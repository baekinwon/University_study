class Rect:
    count = 0
    
    def __init__(self):
        self.width, self.height = 1,1
        Rect.count +=1
        
if __name__ == '__main__':
    r1 = Rect()
    print('[1] r1 (width,height,count)=',r1.width,r1.height,r1.count)
    r2 = Rect()
    print('[2] r1 (width,height,count)=',r1.width,r1.height,r1.count)
    print('[2] r2 (width,height,count)=',r2.width,r2.height,r2.count)

#%%

class Rect:
    count = 0
    
    def __init__(self,width,height):
        self.width, self.height = width,height
        Rect.count +=1
        
if __name__ == '__main__':
    r1 = Rect(3,5)
    r2 = Rect(4,7)
    print('r1 (width,height,count)=',r1.width,r1.height,r1.count)
    print('r2 (width,height,count)=',r2.width,r2.height,r2.count)

#%%

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
    
#%%

from rect import *

r1 = Rect(3,5)
print(Rect.count, r1.count, r1.rectid)
r2 = Rect(4,7)
print(Rect.count, r2.count, r2.rectid)
r3 = Rect(6,9)
print(Rect.count, r3.count, r3.rectid)

#%%
from rect import *
r1 = Rect(3,5)
r2 = Rect(4,7)
r3 = Rect(6,9)
print(Rect.count, r1.count, r1.rectid)
print(Rect.count, r2.count, r2.rectid)
print(Rect.count, r3.count, r3.rectid)

#%%

class Rect:
    
    def __init__(self,width,height=-1):
        if height < 0:
            height = width
        self.width, self.height = width,height
    
    def __repr__(self):
        return 'Rect(w='+'%.2f'%self.width+', h='+'%.2f'%self.height+')'
    
    def get_area(self):
        return (self.width*self.height)
    
    def get_peri(self):
        return 2*(self.width*self.height)
    def isSquare(self):
        return (self.width==self.height)

class Square(Rect):
    def __repr__(self):
        return 'Square(width='+'%.2f'%self.width+')'
    
    def isSquare(self):
        return True
        
if __name__ == '__main__':
    r1 = Rect(3,5)
    print(r1,', 면적:',r1.get_area())
    r2 = Square(7)
    print(r2,', 면적:',r2.get_area())
    r3 = Rect(6,6)
    print(r3,', 면적:',r3.get_area())
    print(r1.isSquare(),r2.isSquare(),r3.isSquare())