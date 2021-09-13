#mine
def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        xstring = str(x)
        if x<0:
            xneg= -x
            xnegstring= str(xneg)
            rev = int(xnegstring[::-1])
            if rev> 2**31 -1 or rev< -2**31:
                return 0
               return -rev
        else:
            rev = int(xstring[::-1])
            if rev> 2**31 -1 or rev< -2**31:
                return 0
            else:
                return rev
#right one:
"""
def reverse(self, x: int) -> int:
    result = 0 - int(str(x)[::-1][:-1]) if x < 0 else int(str(x)[::-1])
    return result if -2 ** 31 <= result <= 2 ** 31 - 1 else 0
"""