
a = "123"
b = 456

print(int(a) + b)
print(a + str(b))

# str(any)  bool(any)
# int(num-or-str)  float(num-or-str)
# list(any-iterable) tuple(any-iterable) set(any-iterable)
# dict(iterable-of-pairs)

x = "abc"
try:
    value = float(x)
except ValueError as err:
    print(err)
else:
    print(value)

