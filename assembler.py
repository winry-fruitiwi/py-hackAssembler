# @author winry
# @date 2022.03.06
#
# coding plan
#   read file → output file using f-strings f'{}'
#   remove whitespace and full-line comments
#   remove inline comments
#   implement decimal_to_binary
#   translate A-instructions
#       take the substring from past the @ to the end of the string
#       translate the substring with decimal_to_binary
#   add comp-dest-jump table
#   translate C-instructions
#       tokenize the instruction
#       translate each part with symbol table
#       add each part to a result string
#   add symbol table
#   remove labels

# adds a new line after the C:\... file path
print()

lines = open("asm/Max.asm", "r")
for line in lines:
    stripped_line = line.strip("\n").strip(" ")

    # where have we searched for comments?
    current_comment_index = 0

    # find if there is a comment and where it starts.
    for char in stripped_line:
        if char == "/":
            break
        current_comment_index += 1

    # we should take the substring to the current comment index to remove any
    # unnecessary comments.
    stripped_line = stripped_line[0:current_comment_index]

    # if the line is whitespace, don't print it.
    if stripped_line != "":
        print(f'{stripped_line}')
