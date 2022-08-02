class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        n = t = 0
        length_name = len(name)
        length_typed = len(typed)
        
        while True:
            if n == length_name:
                last_char = name[n-1]
                while t < length_typed:
                    if last_char != typed[t]:
                        return False
                    else:
                        t += 1
                return True

            if t == length_typed:
                return False

            if name[n] == typed[t]:
                n += 1
                t += 1
            else:
                prev_n_index = n - 1
                if (prev_n_index) < 0:
                    return False

                if name[prev_n_index] == typed[t]:
                    t += 1
                else:
                    return False