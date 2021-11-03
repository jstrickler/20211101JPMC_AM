
i = 0
while i < 3:
    print(i)
    i += 1
print()

i = 0
while True:
    print(i)
    if i == 2:
        break
    i += 1
print()

while True:
    name = input("What is your name (or q to quit)? ")
    if name == 'q':
        break
    if name == '':
        print("Please enter your name")
        continue  # go to top
    color = input("What is your favorite color? ")
    if color == '':
        print("You must enter a color")
        continue
    print(name, color)
