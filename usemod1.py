import sys
# from pkg.pkg import module
from john.math import geo

print(geo.circle_area(25))
print(geo.square_area(7.9))
print(geo.ANIMAL)

# module search:
#  1. current folder
#  2. folders in PYTHONPATH
#  3. builtin folders from install

for path in sys.path:
    print(path)


