file = open("text_input.txt")
text_input = file.read()

file = open("text_output.txt")
text_output = file.read()

print(text_input == text_output)