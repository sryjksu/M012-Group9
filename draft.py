def code(long_string, long_bit, short_string, short_bit, text):
    index = 0  # track index number
    answer = ""  # record translation
    while index < len(text):  # check index
        for i in range(len(short_string)):  # iterate through the list
            if text[index:index + len(short_string[i])] == short_string[i]:  # checks if text matches items in the list
                answer += short_bit[i]  # append translated bits
                index += len(short_bit[i])  # keep track of index number
                continue  # return to the beginning of the while loop
        for i in range(len(long_string)):
            if text[index:index + len(long_string[i])] == long_string[i]:
                answer += long_bit[i]
                index += len(long_bit[i])
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
                    index += len(short_string[i])
                    continue
            for i in range(len(long_bit)):
                if text[index:index + len(long_bit[i])] == long_bit[i]:
                    answer += long_string[i]
                    index += len(long_string[i])
                    continue
    return answer