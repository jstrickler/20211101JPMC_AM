a = "Fred Flintstone"
b = "Bedrock"
c = 44.31843

print(a, b, c)
# sep = ' '
# end = '\n'
#  print(str(a) + sep + str(b) + sep + str(c) + end)
print("---")
print(a, b, c, sep=":")
print(a, b, c, sep=", ")
print(a, end="=>")
print(b, end="=>")
print(c)

print(a, end=' ')
# if ....
#   print(...)
print()   #  print(end)

print(a, "lives in", b)

s = "{} lives in {:s}".format(a, b)
print(s)

print("value is {}".format(c))
print("value is {:.2f}".format(c))
print(f"{a} lives in {b}")  # f-string 3.6+
print(f"value is {c:.2f}")

a = "Fred"
b = "Flintstone"
print(f"|{a:10s}|{b:12s}|")

x = 2398520938520398520935829383
print(f"{x:,d}")  # f-string
print("{:,d}".format(x))  # normal formatting

x = f"{x:,d}"
print(x)







