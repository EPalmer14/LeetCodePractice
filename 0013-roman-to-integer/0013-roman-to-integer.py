class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def getValue(character):
            temp = 0
            if (character == 'I'):
                temp = 1
                return temp
            elif (character == 'V'):
                temp = 5
                return temp
            elif (character == 'X'):
                temp = 10
                return temp
            elif (character == 'L'):
                temp = 50
                return temp
            elif (character == 'C'):
                temp = 100
                return temp
            elif (character == 'D'):
                temp = 500
                return temp
            elif (character == 'M'):
                temp = 1000
                return temp
            else:
                print("Invalid character")
                return temp
                
        if (len(s) == 1):
            total = getValue(s[0])
            return total
        if (len(s) == 2):
            val = getValue(s[0])
            valNext = getValue(s[1])
            if (valNext > val):
                total = valNext - val
                return total
            else:
                total = val + valNext
                return total
                
        total = 0
        skip = 0
        for i in range(len(s)-2):
            if (skip != 0):
                skip -= 1
                continue
            else:
                val = getValue(s[i])
                valNext = getValue(s[i+1])
                valNextNext = getValue(s[i+2])
                if (valNext > val):
                    total = total + (valNext - val)
                    skip = 1
                elif (valNextNext > val):
                    total = total +(valNextNext - (valNext + val))
                    skip = 2
                else:
                    total += val
            
        if (skip == 1):
            val = getValue(s[-1])
            total = total + val
            return total
        elif (skip == 0):
            val = getValue(s[-2])
            valNext = getValue(s[-1])
            if(valNext > val):
                total = total + (valNext - val)
            else:
                total = total + val + valNext
            return total
        else:
            return total

        
        