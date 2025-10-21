def mull(a,b):
    if b == 1:
        return a
    else:
        return a + mull(a,b-1)
    
print(mull(2,5))

def fac(a):
    if a == 1 or a == 0:
        return a
    else:
        return a * fac(a-1)
    
print(fac(5))


def palli(text):
    if len(text) == 1:
        return "pallindrome"
    else:
        if text[0] == text[-1]:
            return palli(text[1:-1])
        else:
            return "Not a Pallindrome"
        
#    palli("madam")
print(palli("madam"))