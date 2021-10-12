#def code(long_string, long_bit, short_string, short_bit, text):
#    index = 0  # track index number
#    answer = ""  # record translation
#    while index < len(text):  # check index
#        for i in range(len(short_string)):  # iterate through the list
#            if text[index:index + len(short_string[i])] == short_string[i]:  # checks if text matches items in the list
#                answer += short_bit[i]  # append translated bits
#                index += len(short_string[i])  # keep track of index number
#                continue  # return to the beginning of the while loop
#        for i in range(len(long_string)):
#            if text[index:index + len(long_string[i])] == long_string[i]:
#                answer += long_bit[i]
#                index += len(long_string[i])
#                continue
#    return answer

def code(string, bit, text):
    index = 0
    answer = ""
    while index < len(text):
        for i in range(len(string)):
            if text[index:index + len(string[i])] == string[i]:
                answer += bit[i]
                index += len(string[i])
                continue
    return answer

def decode(long_string, long_bit, short_string, short_bit, text):
    index = 0
    answer = ""
    while index < len(text):
        if text[index] == "0":
            for i in range(len(short_bit)):
                if text[index:index + len(short_bit[i])] == short_bit[i]:
                    answer += short_string[i]
                    index += len(short_bit[i])
                    continue
        if text[index] == "1":
            for i in range(len(long_bit)):
                if text[index:index + len(long_bit[i])] == long_bit[i]:
                    answer += long_string[i]
                    index += len(long_bit[i])
                    continue
    return answer

def sort_list(long_string, long_bit, short_string, short_bit):
    string = []
    bits = []
    for i in len(long_string):
        if len(long_string[i]) == 4:
            string.append(long_string[i])
            bits.append(long_bit[i])
    for i in len(short_string):
        if len(short_string[i]) == 4:
            string.append(short_string[i])
            bits.append(short_bit[i])
    for i in len(long_string):
        if len(long_string[i]) == 3:
            string.append(long_string[i])
            bits.append(long_bit[i])
    for i in len(short_string):
        if len(short_string[i]) == 3:
            string.append(short_string[i])
            bits.append(short_bit[i])
    for i in len(long_string):
        if len(long_string[i]) == 2:
            string.append(long_string[i])
            bits.append(long_bit[i])
    for i in len(short_string):
        if len(short_string[i]) == 2:
            string.append(short_string[i])
            bits.append(short_bit[i])
    for i in len(long_string):
        if len(long_string[i]) == 1:
            string.append(long_string[i])
            bits.append(long_bit[i])
    for i in len(short_string):
        if len(short_string[i]) == 1:
            string.append(short_string[i])
            bits.append(short_bit[i])
    return (string, bits)
