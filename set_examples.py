data1 = ['red', 'blue', 'purple', 'pink', 'blue', 'blue', 'mauve']
data2 = ['green', 'pink', 'blue', 'black', 'brown']

s1 = set(data1)
s2 = set(data2)
s2.add('orange')
s1.add('green')
s1.add('brown')

print('black' in s1, 'black' in s2)

print("s1:", s1)
print("s2:", s2)
print()

print("common:", s1 & s2)  # intersection
print("not common:", s1 ^ s2)  # xor
print("all:", s1 | s2)  # union
print("just s1:", s1 - s2)
print("just s2:", s2 - s1)


