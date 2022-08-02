class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        n, t = 0, 0
        len_name, len_typed = len(name) - 1, len(typed) - 1
        
        while t <= len_typed:
            
            if name[n] == typed[t]:
                if n < len_name and t < len_typed:
                    n += 1
                    
                t += 1
            
            else:
                if n == len_name and t == len_typed:
                    return False
                
                elif t > 0 and typed[t] == typed[t-1]:
                    t += 1
                    
                else:
                    return False
          
        
        return n == len_name