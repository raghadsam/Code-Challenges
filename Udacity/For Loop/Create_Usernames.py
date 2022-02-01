# Quiz: Create Usernames
# Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:

# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# should create the list:

# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(' ', '_'))

print(usernames)

#-----------------------------------------------------------------------------------

#Instead of creating a new list (append), we want to modify the names in the list directly so we use Range

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(' ', '_')

print(usernames)

#-----------------------------------------------------------------------------------

#THE FOLLOWING CODE WILL CAUSE AN ERROR

# The printed output for the names list will look exactly like it did in the first line. 
# During each iteration, the name variable is set to a string taken from the list. 
# Then the assignment statement creates a new string (name.lower().replace(" ", "_")) 
# and changes the name variable to that string. It doesn't modify the contents of the names list at all. 
# To modify the list we must operate on the list itself, using range, as we saw earlier.

# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# for name in names:
#     name = name.lower().replace(" ", "_")

# print(names)