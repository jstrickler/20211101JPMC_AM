fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]    # map()/apply()
print("f1:", f1, '\n')

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [p[1] for p in people]
print("last_names:", last_names, '\n')

last_names_since_1970 = [p[1] for p in people if p[-1] > '1970']
print("last_names_since_1970:", last_names_since_1970, '\n')

x = []
for p in people:
    if (p[-1] > '1970') or (p[-1] < '1960'):
        x.append(p[1])


x = [p[1] for p in people if (p[-1] > '1970') or (p[-1] < '1960')]
print("x:", x, '\n')

x = [p[1] for p in people]
print("x:", x, '\n')

lngen = (p[1] for p in people)  # create generator
print("lngen:", lngen, '\n')
for last_name in lngen:
    print(last_name)
print()
