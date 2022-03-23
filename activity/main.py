# Example of an attribute error:
x = "hello"
def add_to_string(word):
    new_word = word.append()
    return new_word

add_to_string(x)


# Attempting to get another attibute error, howevering failing (instead getting a TypeError)

# list_of_dictionaries = [{'ice cream': ['chocolate', 'vanilla']}]

# def pop_from_list(list_dicts):
#     for i in range(len(list_dicts)):
#         list_dicts.pop(list_dicts[i])
#     return list_dicts
# pop_from_list(list_of_dictionaries)