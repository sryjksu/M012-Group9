from characters import characters
from characters import char_binary

my_file = open("binary_output.txt")
my_string = my_file.read()
my_string = my_string.split(".")[1]


# combines two lists into a dictionary
def build_dictionary(key, diction):
    dictionary = {}
    for i in range(len(key)):
        dictionary[key[i]] = diction[i]
    return dictionary


# translate binaries to words
def decode(dictionary, text):
    index = 0
    answer = ""
    while index < len(text):
        if text[index] == "0":
            answer += dictionary[text[index:index + 5]]
            index += 5
            continue
        if text[index] == "1":
            answer += dictionary[text[index:index + 7]]
            index += 7
    return answer


dict_decode = build_dictionary(char_binary, characters)

text = decode(dict_decode, my_string)

output = open("text_output.txt", "w")
output.write(text)
output.close()
