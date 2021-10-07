import openpyxl

binary_table = openpyxl.load_workbook("BinaryLetterTable(1).xlsx")
ws = binary_table.active


rows = ws.iter_rows(min_row=1, max_row=80, min_col=1, max_col=2)

characters = []
binary = []

# adds every value into a list
for a,b in rows:
    characters.append(a.value)
    binary.append(b.value)

# converts all integers into string for binary numbers. Need strings so there can be zeros before any ones 001 != 1
char_binary = [str(x) for x in binary]

# adds the correct amount of zeros and formats every list
for x in range(0,15):
    str = ''
    if len(char_binary[x]) < 5:
        for y in range(5 - len(char_binary[x])):
            str = str + '0'
        char_binary[x] = str + char_binary[x]

for z in range(16,len(char_binary)):
    str = ''
    if len(char_binary[z]) <= 6:
        for y in range(6 - len(char_binary[z])):
            str = str + '0'
        char_binary[z] = "1" + str + char_binary[z]

print(characters)
print(char_binary)

binary_dict = {}
binary_dict = dict(zip(characters, char_binary))


