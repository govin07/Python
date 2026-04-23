name = input("Enter any string character : ")
count  = 0

for i in name:
    count +=1
print(count)

Email = input("Enter your email : ")

pos  = Email.index('@')

print(Email[:pos])

pra = input("Enter your para")

term = input('what would like to search in para')
counter=0
for i in pra:
    if i == term:
        counter+=1
print(counter)


pra = input("Enter your para")

term = input('what would like to remove in para')

result = ''

for i in pra:
    if i != term:
        result += i
print(result)

name = input("Enter any string :").upper()

s = ''

for i in range(len(name)-1,-1,-1):
    s += name[i]
if s == name:
    print("pellendrome")
else:
    print("Not a pellendrome")

value = input("write a line in string")
l = []
temp = ''

for i in value:
    if i != ' ':
        temp += i
    else:
        l.append(temp)
        temp = ''
print(l)
