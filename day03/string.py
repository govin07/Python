name = "govind"
i = 0
j = len(name) - 1   # yaha galti thi n-1 

name = list(name)   # string ko list banaya (sirf ek hi line add hui) []

def swap(i, j):
    name[i], name[j] = name[j], name[i]   # ab list ke elements swap honge

while i <= j:
    swap(i, j)
    i += 1
    j -= 1

print("".join(name))   # wapas string banaya
