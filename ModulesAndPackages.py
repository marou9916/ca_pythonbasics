import re
find_members = []
for function in dir(re):
    if "find" in function:
        find_members.append(function)

print(find_members)
