from characters import characters
from characters import char_binary

my_file = open("text_input.txt")
my_string = my_file.read()
print(my_string)


# looks ar every char and finds its index in characters list. Then prints index from the char_binary list
binary_str = ''
# for char in my_string:
#     for index in range(len(characters)):
#         if characters[index] == char:
#             binary_str = binary_str + char_binary[index]

matching_keys = []
for char in my_string:
    for x in characters:
        if x.startswith(char):
            matching_keys.append(x)

for char in my_string:
    for x in matching_keys:
        for index in range(len(characters)):
             if characters[index] == char:
                   binary_str = binary_str + char_binary[index]


print(matching_keys)

# print(binary_str)
# print(len(binary_str))

