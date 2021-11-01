s1 = "spam\n"   # single-DELIMITED
s2 = 'spam\n'
s3 = """spam\n"""  # triple-DELIMITED
s4 = '''spam\n'''
s5 = r"spam\n"   # raw string

print("It's a good thing")
print('It is the "Python Way"')
# print(""foo"")
print(''''Wow!' It's the "Python Way"''')

query = """
select *
from accounts
where customer_id = '123abc'
order by balance desc
"""

s = '''
help me
'''


print(len(s1), len(s2), len(s5))