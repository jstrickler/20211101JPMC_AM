#  int float bool complex

i1 = 1234

i2 = 1000
i3 = 0x1000
i4 = 0b1000
i5 = 0o1000
print(i2, i3, i4, i5)
#  INVALID: x = 002

x = 2398092835029385203958203958203958203958203958203958203598203958203598203958203958203958203958209358209385029358209582095802985029850298502985029850298502985092850
print(x + 1)

y = 1_000_000_000
y = 10_00_00_00_00
print(y)

f1 = 123.456
f2 = .456
f3 = 123.
f4 = 0.0
f5 = 1_238_937.493_930
print(f5)

a = 23
b = 6
print(a + b, a - b)
print(a * b, a / b, a // b, a // -b)
print(a ** b, a % b)
print(divmod(a, b))

a += 2  # a = a +  2     # also in C, C++, Java, C#, Perl, etc etc
a *= 3
a /= 5
print(a)

#  a++ ++a  etc  NOT IMPLEMENTED

# PEMDAS  Please Excuse My Dear Aunt Sally
#         Parens Exponent Mult/Div Add/Subtract




