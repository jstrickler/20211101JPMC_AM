import collections

x = 100  # GLOBAL variable (visible to end of script)

def spam():
#     print("in spam(): global x:", globals()['x'])  # sketchy!
    x = "wolverine"  # LOCAL
    y = 42  # LOCAL variable (visible to end of function)
    print(f"in spam(): x is {x}")

spam()

print(f"in main: x is {x}")
# print(f"in main: y is {y}")

# local -> nonlocal -> global -> builtin

def foo(a, b):
    x = 42  # a and x are local to foo()

    def bar():
        print(a, x)  # a and x are nonlocal to bar()

