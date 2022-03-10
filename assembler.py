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

compDict = {
    "0":    "0101010",
    "1":    "0111111",
    "-1":   "0111010",
    "D":    "0001100",
    "A":    "0110000",
    "M":    "1110000",
    "!D":   "0001101",
    "!A":   "0110001",
    "!M":   "1110001",
    "-D":   "0001111",
    "-A":   "0110011",
    "-M":   "1110011",
    "D+1":  "0011111",
    "A+1":  "0110111",
    "M+1":  "1110111",
    "D-1":  "0001110",
    "A-1":  "0110010",
    "M-1":  "1110010",
    "D+A":  "0000010",
    "D+M":  "1000010",
    "D-A":  "0010011",
    "D-M":  "1010011",
    "A-D":  "0000111",
    "M-D":  "1000111",
    "D&A":  "0000000",
    "D&M":  "1000000",
    "D|A":  "0010101",
    "D|M":  "1010101"
}
destDict = {
    "null":  "000",
    "M":     "001",
    "D":     "010",
    "MD":    "011",
    "A":     "100",
    "AM":    "101",
    "AD":    "110",
    "AMD":   "111",
}
jumpDict = {
    "null":  "000",
    "JGT":   "001",
    "JEQ":   "010",
    "JGE":   "011",
    "JLT":   "100",
    "JNE":   "101",
    "JLE":   "110",
    "JMP":   "111",
}

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


# decides whether you have an A- or C-instruction
def a_or_c_instruction(instruction):
    # if there's an @ symbol, you have an A-instruction. Otherwise, it's a
    # C-instruction. We call the respective translations there.
    if instruction[0] == "@":
        return translate_a_instructions(instruction)
    else:
        return translate_c_instructions(instruction)


# translates a-instructions after being called from a_or_c_instruction
def translate_a_instructions(instruction):
    number = int(instruction[1:])

    # turn the number into a binary word string and add it to a 0!
    binary_word = dec_to_binary(number, 15)

    return "0" + binary_word


'''
actually I'm not sure if this works, I'll need to use my old approach
    Pseudocode for translating c-instructions
    Arguments: instruction
    
    define comp as the substring from the position of the equals sign
    if valueError, find comp again
    
    define jump as the substring from the position of the semicolon
    if valueError, make jump equal to "000"
    
    define dest as the substring to the position of the equals sign
    if valueError


    define posOfEquals = line.indexOf("=")
    define posOfSemicolon = line.index(";")
    define ifDest = (posOfEquals !== -1) as a flag
    define ifJump = (posOfSemicolon !== -1) as a flag
    result = "111"
    
    if (ifDest && ifJump):
        define dest = line.substring(0, posOfEquals)
        result += destDict[dest]
        define comp = line.substring(posOfEquals, posOfSemicolon)
        result += compDict[comp]
        define jump = line.substring(posOfSemicolon)
        result += jumpDict[jump]
    
    else if (ifDest):
        define dest = line.substring(0, posOfEquals)
        result += destDict[dest]
        define comp = line.substring(posOfEquals, posOfSemicolon)
        result += compDict[comp]
        result += jumpDict["null"]
    
    else if (ifJump):
        result += destDict["null"]
        define comp = line.substring(posOfEquals, posOfSemicolon)
        result += compDict[comp]
        define jump = line.substring(posOfSemicolon)
        result += jumpDict[jump]
    
    return the result
'''

'''
    define "111" as machineCode
    binary_dest = ""
    binary_comp = ""
    binary_jump = ""
    
    
    try:
        dest = instruction[0:indexOfEquals]
    except:
        dest = "null"
    
    retrieve dest from dictionary and store it in binary_dest
    
    
    try:
        comp = instruction[indexOfEquals:indexOfSemicolon]
    except:
        try:
            comp = instruction[indexOfEquals:]
        except:
            comp = instruction[:indexOfSemicolon]
    
    retrieve comp from dictionary and store it in binary_comp
    
    
    try:
        jump = instruction[indexOfSemicolon:]
    except:
        jump = "null"
    
    retrieve jump from dictionary and store it in binary_jump
    
    
    return machineCode + binary_comp + binary_dest + binary_jump
'''


def translate_c_instructions(instruction):
    machine_code = "111"

    # find the destination
    try:
        dest = instruction[0:instruction.index("=")]
    except ValueError:
        dest = "null"

    # find the computation
    try:
        comp = instruction[instruction.index("=") + 1:instruction.index(";")]
    except ValueError:
        try:
            comp = instruction[instruction.index("=") + 1:]
        except ValueError:
            comp = instruction[:instruction.index(";")]

    # find the jump
    try:
        jump = instruction[instruction.index(";") + 1:]
    except ValueError:
        jump = "null"

    binary_dest = destDict[dest]
    binary_comp = compDict[comp]
    binary_jump = jumpDict[jump]

    return machine_code + binary_comp + binary_dest + binary_jump


lines = open("asm/PongL.asm", "r")
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
        print(f'{a_or_c_instruction(whitespace_stripped_line)}')

# now that I'm done with the file, I can close it.
lines.close()

# TODO testing area
'''
for i in range(17):
    print(f"{i}: {dec_to_binary(i, 5)}")

print(f"{16384}: {dec_to_binary(16384, 15)}")
'''
