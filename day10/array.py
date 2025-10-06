sample = "how are you ?"
l = []

# sample2 = sample.split()


for i in sample.split():
    print(i.capitalize())
    l.append(i.capitalize())

print(" ".join(l))

email = "acb@gmail"

print(email[:email.find("@")])