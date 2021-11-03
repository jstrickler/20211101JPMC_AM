list1 = list()    # List list1 = new List();
list2 = ['a', 'b', 'c']
list3 = [1, 2, 3, 5.9, 'foo', None, 'bar', ['more', 'stuff']]
list4 = []
list5 = ['a', 'b', 'c']

print(list1 == list4, list2 == list5)

cities = ['Bangalore', 'Glasgow', 'Herzliya', 'Columbus']
print(cities)
print(len(cities))
print(cities[0])
print(cities[-1], cities[3])   # cities[len(cities)-1]
cities.append("Durham")
print(cities)
cities.insert(0, "Houston")
print(cities)
cities.insert(4, 'Dallas')
print(cities)
more_cities = ['London', 'Paris', 'Mumbai']

cities.extend(more_cities)
print(cities)
print(len(cities))

del cities[8]
print(cities)

c = cities.pop()
print(c, cities)

c = cities.pop(4)
print(c, cities)

cities.remove('Durham')
print(cities)

# del LIST[pos]   LIST.pop(pos=-1)   LIST.remove(value)
x = 5
del x

print(cities[0:3])
print(cities[2:5])
print(cities[0:3], cities[3:len(cities)])
print(cities[3:])
print(cities[:3])
print(cities[::])   #   start:stop:step
print(cities[::2])  # every other city
print(cities[1:-1]) # skip ends
s = '"spam"'
print(s, s[1:-1])
print(cities[1][:4])
name = "Alfred E. Newman"
print(name[::2])

print(cities)
for city in cities:   # similar to foreach in some languages
    print(city)
print()

# for VAR in ITERABLE:
#     VAR = next(ITERABLE)
#     ...

# Ross: please ignore:
# for (i = 0; i < 10; i++) { }
a1 = ['a', 'b', 'c']
a2 = 'a', 'b', 'c'
a3 = 'abc'

print(len(a1), len(a2), len(a3))
print(min(a1), min(a2), min(a3))
print(max(a1), max(a2), max(a3))
print(sorted(a1), sorted(a2), sorted(a3))
print(reversed(a1))
for x in reversed(a1):
    print(x)
r = reversed(a1)
print(type(r))
print(list(r))
print(list(r))
r = reversed(a2)
for letter in r:
    print(letter)

print(a1)
for letter in a1:   # foreach
    print(letter)
print()

for i, letter in enumerate(a1, 1):
    print(i, letter)
print()
print(list(enumerate(a1)))

j = "abc"
k = "def"
print(j + k)

print("-" * 60)
print("abc" * 10)

print([1, 2, 3] * 5)
print([0] * 25)













