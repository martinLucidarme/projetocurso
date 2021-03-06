class Solution(object):
    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        """
        map={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum=0
        last = 1000
        for l in s:
            nb= map[l]
            if nb <= last:
                sum += nb
            else:
                sum+= nb-2*last
            last = nb
        return sum

    print(romanToInt('MCXIV'))
