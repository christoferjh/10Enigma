import sys
alphabet_uppercase = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ.?!01"

#print("Letter\tDec\tBinary")
#print("----------------------------------------------------------")
output_dict = {}
for letter in alphabet_uppercase:
    # Get the ASCII value of the letter
    ascii_value = ord(letter)
    # If the letter is '.', set its binary representation to '000'
    if letter == '_':
        binary_value = '00000'
    elif letter == '.':
        binary_value = '11011'
    elif letter == '?':
        binary_value = '11100'
    elif letter == '!':
        binary_value = '11101'
    elif letter == '0':
        binary_value = '11110'
    elif letter == '1':
        binary_value = '11111'          
    else:
        # Convert the ASCII value to binary and format it to 8 bits
        binary_value = format(ascii_value, '08b')[3:]
    # Convert binary to decimal
    decimal_value = int(binary_value, 2)
    #print(f"{letter}\t{decimal_value}\t{binary_value}")
    # Save the output into the dictionary
    output_dict[letter] = (binary_value, decimal_value)

def print_table():
    print("Letter\tDec\tBinary")
    print("-------------------------------")
    for letter in alphabet_uppercase:
        (binary_value, decimal_value) = output_dict[letter] 
        print(f"{letter}\t{decimal_value}\t{binary_value}")

def print_values_for_letter(letter, data_dict):
    if letter in data_dict:
        binary_value, decimal_value = data_dict[letter]
        #print(f"Letter: {letter}")
        #print(f"Binary Representation: {binary_value}")
        #print(f"Decimal Value: {decimal_value}")
        return binary_value
    else:
        #print(f"Letter '{letter}' not found in the dictionary.")
        return "Ö"



def print_binary_values(string, data_dict):
    print("Binary Values for String:",string)
    print("--------------------------")
    res = get_binary_values(string, data_dict)
    print(res)
def get_binary_values(string, data_dict):
    res = ""
    for letter in string:
        val = print_values_for_letter(letter, data_dict)
        res+=val+" "
    return res

def get_letter_from_binary(binary_value, data_dict):
    for letter, (binary, decimal) in data_dict.items():
        if binary == binary_value:
            return letter
    return None
def print_letter_from_binary_values(string, data_dict):
    print("Binary Values for String:",string)
    print("--------------------------")
    res = ""
    for letter in string:
        val = get_letter_from_binary(letter, data_dict)
        res+=val+" "
    print(res)

def get_letters_from_binary(binary_string, data_dict):
    binary_values = binary_string.split()
    res = ""
    for binary_value in binary_values:
        letter = get_letter_from_binary(binary_value, data_dict)
        if letter:
            #print(f"Binary Value: {binary_value} --> Letter: {letter}")
            res+=letter
        else:
            #print(f"No letter found for binary value: {binary_value}")
            res+="Ö"
    return res
def print_letters_from_binary(binary_string, data_dict):
    
    print("Letters corresponding to Binary Values:")
    print("----------------------------------------")
    print(get_letters_from_binary(binary_string, data_dict))
        


def demo():
    print("DEMO")
    #print table
    print_table()
    # Example usage:
    print_binary_values("HELLO", output_dict)
    # Example usage:
    print_values_for_letter('A', output_dict)
    # Example usage:
    binary_string = '01000 00101 01100 01100 01111'
    print_letters_from_binary(binary_string, output_dict)

    binary_string = '01101 01110 01000 11000 10101'
    print_letters_from_binary(binary_string, output_dict)


    #hidden 
    print_binary_values("HELLO_WORLD", output_dict)

    binary_string = '01000 00101 01100 01100 01111 00000 10111 01111 10010 01100 00100'
    print_letters_from_binary(binary_string, output_dict)


def handle_argument_A():
    # Code to handle argument "-A"
    #print("Converting to alpha.")
    joined_arguments = ' '.join(sys.argv[2:])
    print(get_letters_from_binary(joined_arguments, output_dict))

def handle_argument_B():
    # Code to handle argument "-B"
    #print("Converting to binary.")
    joined_arguments = ' '.join(sys.argv[2:]).upper().replace(" ", "_")
    #print(joined_arguments)
    print(get_binary_values(joined_arguments, output_dict))

def handle_argument_T():
    # Code to handle argument "-T"
    #print("Printing table")
    print_table()

def check_argument():
    # Check command-line arguments and call appropriate functions
    if len(sys.argv) < 2:
        print("Usage: python script.py <-A/-B/-T> <other_arguments>")
        return False
    elif sys.argv[1] == "-A":
        handle_argument_A()
        return True
    elif sys.argv[1] == "-B":
        handle_argument_B()
        return True
    elif sys.argv[1] == "-T":
        handle_argument_T()
        return True
    else:
        print("Invalid argument. Please use either '-A' or '-B' or '-T'.")
        return False
        


if __name__ == "__main__":
    if (check_argument()==False):
        demo()
    




