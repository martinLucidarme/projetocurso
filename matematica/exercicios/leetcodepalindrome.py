#mine
def palindrome(x):
        xstring=str(x)
        L=[]
        palin = False
        for i in range(len(xstring)):
                L += xstring[i]
        for j in range(len(L)):
            if L[j] == L[len(xstring) - j - 1]:
                palin = True
            else:
                palin = False
                return palin
        return palin
print(palindrome(121))

# right one:
def ispalind(pal):
    return pal== pal[::-1]
a= 'alamalo'
b=ispalind(a)
if b :
    print("yes")
else:
    print("no")