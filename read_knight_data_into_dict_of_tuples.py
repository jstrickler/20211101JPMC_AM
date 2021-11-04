from pprint import pprint

knight_data = {}
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment

pprint(knight_data, sort_dicts=False)
# pprint("Hello world")
# x = 5
# pprint(f"Value is {x}")
