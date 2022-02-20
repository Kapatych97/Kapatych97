
def setup():
    size (1000,1000)
def draw():
    cvet=255
    for y in range (0,900,50):
        
        for x in range (0,1000,50):
            fill (cvet) 
            rect (x,y,70,70)
            if cvet == 255:
                cvet = 0
            else:
                cvet = 255
                
        if cvet == 255:
            cvet = 0 
        else:
            cvet = 255           
                        
           
                
            
        
                    
