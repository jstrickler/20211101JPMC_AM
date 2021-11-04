d1 = dict()
d2 = {'NC': 'Raleigh', 'NY': 'Albany', 'TX': 'Austin'}
print(d2['NC'])
d3 = {}  # empty dict
# d4 = dict(key=value, key=value)
# d5 = dict(iterable-of-pairs)
# {value, value, value, ...}   is a set
airports = {
    # KEY: VALUE, KEY: VALUE, ...
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(airports['RDU'], airports['YOW'])
airports['GLA'] = 'Glasgow'
airports['TLV'] = 'Tel Aviv/Jerusalem'
print(airports)
print(airports['GLA'])

codes = ['TLV', 'RDU', 'XYZ', 'WOMBAT', 'ABQ']

for code in codes:
    print(code, code in airports)
print()

x = dict()
x['spam'] = []
x['spam'].append('foo')
x['spam'].append('bar')
print(x, '\n')

print(airports.keys())
print(airports.values())
print(airports.items())

print(airports['TLV'])

for code in codes:
    print(code, airports.get(code, 'WOMBAT!!'))
print()

new_airports = [
    ('LHR', 'Heathrow'),
    ('LTN', 'Luton'),
    ('EDI', 'Edinburgh'),
    ('TLV', 'Tel Aviv'),
]

print("before:", airports)
for code, name in new_airports:
    print(airports.setdefault(code, name))
print("after:", airports, '\n')

for code, name in airports.items():
    print(code, name)
print()
print('-' * 60)
for code, name in sorted(airports.items()):
    print(code, name)
print()

def by_value(item):
    return item[1], item[0]

for code, name in sorted(airports.items(), key=by_value, reverse=True):
    print(code, name)
print()

# for key, value in dict.items():
#    ...
