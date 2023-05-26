class Vect2:
    ndim = 2
    
    def __init__(self,x,y):
        self.x,self.y = x,y
    
    def __repr__(self):
        return 'Vector['+'%2.f'%self.x+','+'%2.f'%self.y+']'
    
    def __add__(self,other):
        new = Vect2(0,0)
        new.x = self.x+other.x
        new.y = self.y+other.y
        return new
        
if __name__ == '__main__':
    v1 = Vect2(3,5)
    v2 = Vect2(7,4)
    v3 = v1+v2
    print(v1,v2,v3)

#%%

class Vect2:
    ndim = 2
    
    def __init__(self,x,y=0):
        self.x,self.y = x,y
    
    def __repr__(self):
        return 'Vector['+'%2.f'%self.x+','+'%2.f'%self.y+']'
    
if __name__ == '__main__':
    v1 = Vect2(3,5)
    v2 = Vect2(7)
    print(v1,v2)
    
#%%

class Vect3:
    ndim = 2
    
    def __init__(self,x,y=0):
        self.x,self.y = x,y
    
    def __repr__(self):
        return 'Vector['+'%2.f'%self.x+','+'%2.f'%self.y+']'
    
    def __add__(self,other):
        __new = Vect2(0,0)
        __new.x = self.x+other.x
        __new.y = self.y+other.y
        return __new
    
if __name__ == '__main__':
    v1 = Vect3(3,5)
    v2 = Vect3(7)
    v3 = v1+v2
    print(v1,v2,v3)
    print(v2.x,v2.y)
    print(v2.__new)