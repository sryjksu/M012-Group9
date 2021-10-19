def build_dictionary(key, diction):  # combines two lists into a dictionary
    dictionary = {}
    for i in range(len(key)):
        dictionary[key[i]] = diction[i]
    return dictionary


def code(dictionary, text):  # translate words to binaries
    index = 0
    answer = ""
    while index < len(text):
        for i in range(10, 0, -1):
            if text[index:index + i] in dictionary:
                answer += dictionary[text[index:index + i]]
                index += i
    return answer


def decode(dictionary, text):  # translate binaries to words
    index = 0
    answer = ""
    while index < len(text):
        if text[index] == "0":
            answer += dictionary[text[index:index + 5]]
            index += 5
        if text[index] == "1":
            answer += dictionary[text[index:index + 7]]
            index += 7
    return answer
