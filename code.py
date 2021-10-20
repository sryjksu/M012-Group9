from characters import characters
from characters import char_binary

my_file = open("text_input.txt")
my_string = my_file.read()


# combines two lists into a dictionary
def build_dictionary(key, diction):
    dictionary = {}
    for i in range(len(key)):
        dictionary[key[i]] = diction[i]
    return dictionary


# translate words to binaries
def code(dictionary, text):
    index = 0
    answer = ""
    while index < len(text):
        for i in range(10, 0, -1):
            if text[index:index + i] in dictionary:
                answer += dictionary[text[index:index + i]]
                index += i
                break
    return answer


dict_code = build_dictionary(characters, char_binary)

binary = code(dict_code, my_string)
binary = str(len(binary)) + "." + binary

output = open("binary_output.txt", "w")
output.write(binary)
output.close()
