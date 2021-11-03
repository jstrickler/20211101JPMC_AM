person = 'Bill', 'Gates', 'Microsoft', '1955-10-25'
print(type(person), len(person))

#  namedtuple   dataclass
print(person[0], person[1])

first_name, last_name, product, dob = person   # iterable unpacking
print(first_name, last_name)

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
print(people[0], type(people[0]))
print(people[0][0])
print(people[0][0][0])
print()
for person in people:
    print(person)  # person[0], ...
print("-" * 60)

for first_name, last_name, *_ in people:
    print(first_name, last_name)
print("-" * 60)

data = [('a', 5), ('m', 32), ('x', 8), ('b', 14)]
for letter, number in data:
    print(letter * number)
print()




