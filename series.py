def findTerm(n): 
  
    if n == 1 : 
        return n 
    else : 
          
        
        term = 7
  
        
        for i in range(2, n + 1) : 
            term = term * 2 + (i - 1);      
  
    return term; 
  
 
print (findTerm(5))