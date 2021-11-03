#!/usr/bin/env python

name = input("What is your name: ")
quest = input("What is your quest? ")
print(f"{name} seeks {quest}")

raw_num = input("Enter number: ")  # <1>
num = float(raw_num)  # <2>

f = ((9 * num) / 5) + 32

print(f"2 times {num} is {2 * num}")

#  \u00B0  degree symbol
