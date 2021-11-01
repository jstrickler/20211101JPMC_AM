actor = "Chris Hemsworth"  # strings are IMMUTABLE
print(actor, type(actor))
print(actor.upper())  # call method on str object
print(actor)
print(len(actor), type(actor))
a = actor.upper()

# x.a  use value of attribute a
# x.a() use RETURN value after calling function/method a
print(actor.count('h'))
print(actor.lower().count('h'))  # method chaining
print(actor.startswith('Chris'))
print(actor.startswith('Liam'))
print(actor.find('Chris'))
print(actor.find('Liam'))
print(actor.find('worth'))
print(actor)
print(actor.replace('Chris', 'Liam'))

print("is" in actor)
print("was" in actor)

s = "     All my exes live in Texas       "
print('|' + s.lstrip() + '|')
print('|' + s.rstrip() + '|')  # remove trailing \n on file input
print('|' + s.strip() + '|')
print()

s = "xxxyyyx  yxxyyxxxxxxxAll my exes live in Texasyyyyyyyyyxyyyyyyyy"
print('|' + s.lstrip('xy ') + '|')  # 'x' or 'y' or ' '
print('|' + s.rstrip('xy ') + '|')  # 'x' or 'y' not both
print('|' + s.strip('xy ') + '|')
print()
print(s.replace('xy', ''))

raw_line = 'Houston TX JPMC'
fields = raw_line.split()
print(fields)

raw_line = 'foo:bar:blah'
values = raw_line.split(':')
print(values)

#  Don't split CSV data:
#   "Smith, Joe", "Durham, NC", 27705



