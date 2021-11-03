import csv

file_name = "DATA/mary.txt"

mary_in = open(file_name, "r")
print(mary_in)
mary_in.close()

with open(file_name) as mary_in:
    pass
    # mary_in.close()

with open(file_name) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()  # remove \n \r etc
        print(line)
print("-" * 60)

with open(file_name) as mary_in:
    contents = mary_in.read()
    print("raw:")
    print(repr(contents))
    print("normal:")
    print(contents)
print("-" * 60)

with open(file_name) as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print("-" * 60)

with open(file_name) as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)
print("-" * 60)

with open(file_name) as mary_in:
    all_lines_without_nl = (line.rstrip() for line in mary_in)
    print(all_lines_without_nl)
print()

target = 'q'
with open('DATA/words.txt') as words_in:
    output_filename = f"{target}_words.txt"
    count = 0
    with open(output_filename, 'w') as words_out:
        for raw_line in words_in:
            if target in raw_line:
                line = raw_line.rstrip()
                count += 1
                print(line)
                words_out.write(raw_line)  # write to output file
print(f"{count} words contain {target}")

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple, NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux, git', '1969-12-28'),
]

with open('people.csv', 'w') as people_out:
    wtr = csv.writer(people_out, lineterminator='\n')
    for row in people:
        wtr.writerow(row)  # wtr.writerow(any-iterable)
