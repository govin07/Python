str_input = input('Enter your prompt  ').upper()
print(str_input)

count = 0

for i in str_input:
     if i in ("A", "E", "I", "O", "U"):
          count += 1

print (count)



