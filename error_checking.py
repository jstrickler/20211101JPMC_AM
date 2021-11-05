file_name = "DATA/wombats.txt"
try:
    with open(file_name) as file_in:
        pass
except (FileNotFoundError, PermissionError) as err:  # like 'catch'
    print(err)

data = [1, 5, 19, 47]
index = 12
try:
    print(data[index])
except IndexError as err:
    print(err)


number = 23
for value in 5, 8, 0, 12, 19:
    try:
        result = number / value
    except ZeroDivisionError as err:
        print(err)
    else:  # no exception
        print(result)
    finally:  # only needed to
        pass  # clean up resources

print("Done.")