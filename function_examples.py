
def get_message():
    return "Hello, JPMC world"

m = get_message()
print(m, '\n')

def display_message():
    msg = get_message()
    print(msg)

result = display_message()
print(result)

# google:  "python type hinting"
def greet(whom: str) -> None:   # optional type checking
    # check param(s)
    print(f"Hello, {whom}")

greet("world")
greet("Mom")
greet("New York")
greet(23903)
greet(1.3432)
greet(None)

def concat(a, b):
    return str(a) + str(b)

print(concat('spam', 'ham'))
print(concat(10, 20))

x = ['a', 'b', 'c']

def spam(f):
    f.append("wombat")

spam(x)
print(x)

def find_word(file_name, *terms):
    with open(file_name) as file_in:
        for raw_line in file_in:
            for term in terms:
                if term in raw_line:
                    line = raw_line.rstrip()
                    print(line)
                    break

find_word('DATA/alice.txt', 'Lizard', 'pig', 'Queen')
find_word('DATA/words.txt')


def config(**kwargs):
    print(kwargs)

config(file_name='wombats.txt', country='Australia', beer="Fosters")

# 4th type: keyword-only
# 5th type: positional-only

def count_lines(file_name, term):
    with open(file_name) as file_in:
        count = 0
        for line in file_in:
            if term in line:
                count += 1
    return count

print(count_lines('DATA/alice.txt', 'Alice'))
print(count_lines('DATA/words.txt', 'python'))

def ham(foo, *bar):
    pass
ham(1)
ham(1, 2, 3, 4, 5, 6, 7)

def toast(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

toast()
toast(1, 2, 3)
toast(1, 2, 3, a=4, b=22, animal='wombat')

def myprint(*objs, end='\n', sep=' ')
    pass

a = 5
b = "banana"
myprint(a, b)
myprint(a, end='foo')
myprint(a, b, sep="/")
















