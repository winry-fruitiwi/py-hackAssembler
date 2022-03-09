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

'''

    Pseudocode for dec_to_binary:
        Implementation: iterative
        Args: int num, int wordLength
        max_power_of_2_fits_in_num = 0
        loop until 2**max_power_of_2_fits_in_num > num
            increment max_power_of_2_fits_in_num
        decrement max_power_of_2_fits_in_num
        define empty string word
        while max_power_of_2_fits_in_num is greater than 0:
            if 2**max_power_of_2_fits_in_num <= num:
                word += "1"
                num -= 2**max_power_of_2_fits_in_num
            else:
                word += "0"
            decrement max_power_of_2_fits_in_num
        while len(word) < wordLength:
            word = "0" + word
        return word

'''


def dec_to_binary(num, word_length):
    # this is the binary word
    word = ""

    if (num == 0) or (num > 2):
        # the maximum number of times 2 fits into the argument num
        max_power_of_2_fits_in_num = 0
        while 2 ** max_power_of_2_fits_in_num <= num:
            max_power_of_2_fits_in_num += 1

        # we always go one power too far, so we need to decrement this variable
        # after we finish finding its value.
        max_power_of_2_fits_in_num -= 1

        # now we can calculate the binary word's value!
        while max_power_of_2_fits_in_num >= 0:
            if 2 ** max_power_of_2_fits_in_num <= num:
                word += "1"
                num -= 2 ** max_power_of_2_fits_in_num
            else:
                word += "0"

            # always make sure to decrement your counters!
            max_power_of_2_fits_in_num -= 1
    elif num == 1:
        word = "1"
    elif num == 2:
        word = "10"

    # if our word is too short, we can make it bigger now.
    while len(word) < word_length:
        word = "0" + word

    return word


def a_or_c_instruction():
    # decides whether you have an A- or C-instruction
    pass


def translate_a_instructions(instruction):
    # translates a-instructions after being called from a_or_c_instruction
    number = int(instruction[1:])

    # turn the number into a binary word string and add it to a 0!
    binary_word = dec_to_binary(number, 15)

    return "0" + binary_word


lines = open("asm/AInstructions.asm", "r")
for line in lines:
    stripped_line = line.strip("\n")

    '''
    # where have we searched for comments?
    current_comment_index = 0


    This can be simplified to using stripped_line.indexOf("//") and a try-except
    block
    # find if there is a comment and where it starts.
    for char in stripped_line:
        if char == "/":
            break
        current_comment_index += 1

    # we should take the substring to the current comment index to remove any
    # unnecessary comments.
    '''

    # see if there is a comment and where it is
    try:
        comment_index = stripped_line.index("//")
        stripped_line = stripped_line[0:comment_index]
    except ValueError:
        pass

    whitespace_stripped_line = stripped_line.strip(" ")

    # if the line is whitespace, don't print it.
    if stripped_line != "":
        print(f'{translate_a_instructions(whitespace_stripped_line)}')

# now that I'm done with the file, I can close it.
lines.close()

# TODO testing area
'''
for i in range(17):
    print(f"{i}: {dec_to_binary(i, 5)}")

print(f"{16384}: {dec_to_binary(16384, 15)}")
'''
