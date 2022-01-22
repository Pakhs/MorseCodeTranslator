import json
import sys

#file that includes all morse code representations
#do not change
FILENAME = 'morse_list.json'
FILENAME_REVERSED = 'morse_list_reversed.json'

#Functions to load the morse representations
def open_morse_list(fname, fname_reversed):
    try:
        with open(fname,'r') as f:
            morse = json.load(f)
    except:
        print('Error, cannot open morse file')
    try:
        with open(fname_reversed,'r') as f:
            morse_reversed = json.load(f)
    except:
        print('Error, cannot open morse file')
    return morse, morse_reversed

#Initialise the dictionaries
morse, morse_reversed = open_morse_list(FILENAME, FILENAME_REVERSED)

#Function that encodes an entered string
def encode_morse():
    print("> Encoding selected, each letter will be seperated with a space and each word with a slash")
    inp = input("> Enter the string you want to convert to morse code: ")
    print('\nOutput:')
    inp = inp.split(' ')
    for word in range(len(inp)):
        for c in inp[word]:
            try:
                print(morse[c.lower()], end = ' ')
            except:
                print("\nError, new lines not accepted in encode string mode")
                quit()
        print(' / ', end = ' ')
    print('\n')

#Function that decodes an entered string
def decode_morse():
    print("> Decoding selected, enter each letter seperated with one space and each word with two spaces from each other")
    inp = input("> Enter the morse code you want to convert to ASCII: ")
    print('\nOutput:')
    inp = inp.split(' ')
    for word in inp:
        try:
            print(morse_reversed[word], end = '')
        except KeyError:
            print("Error, no morse representation for " + word)
    print('\n')

#Function that encodes a file
def encode_file():
    with open(sys.argv[3], 'r') as f:
        contents = f.read()
    f = open('output', 'w')
    output = ''

    contents = contents.split('\n')
    for line in range(len(contents)):
        contents[line] = contents[line].split(' ')
    
    for line in range(len(contents)):
        for word in range(len(contents[line])):
            for c in contents[line][word]:
                try:
                    output += morse[c.lower()] + ' '
                except:
                    print("\nError")
                    quit()
            output += ' /  '
        output += '\n\n'
    f.write(output)
    f.close()
    print("> File encoded, each letter is seperated with a space and each word with a slash")
    print("> Lines are kept as the original file")
        
def decode_file():
    print("> Not yet implemented")


#Function that handles the arguments passed by the user
def argumentsHandler():
    if len(sys.argv) == 4:
        arg = sys.argv[1]
        if sys.argv[2] != '-f':
            print("> Incorrect ammount of arguments, correct usage:")
            print("> ./translator.py -e (for encode)")
            print("> ./translator.py -d (for decode)")
            print("> ./translator.py -e -f [filename] (for encoding files)")
            print("> ./translator.py -d -f [filename] (for decoding files)")
            quit()
        else:
            if arg == '-e':
                encode_file()
            elif arg == '-d':
                decode_file()
            else:
                print("> Unknown command, correct usage:")
                print("> ./translator.py -e (for encode)")
                print("> ./translator.py -d (for decode)")
                print("> ./translator.py -e -f [filename] (for encoding files)")
                print("> ./translator.py -d -f [filename] (for decoding files)")
                quit()
    elif len(sys.argv) != 2:
        print("> Incorrect ammount of arguments, correct usage:")
        print("> ./translator.py -e (for encode)")
        print("> ./translator.py -d (for decode)")
        print("> ./translator.py -e -f [filename] (for encoding files)")
        print("> ./translator.py -d -f [filename] (for decoding files)")
        quit()
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg == '-e':
            encode_morse()
        elif arg == '-d':
            decode_morse()
        else:
            print("> Unknown command, correct usage:")
            print("> ./translator.py -e (for encode)")
            print("> ./translator.py -d (for decode)")
            print("> ./translator.py -e -f [filename] (for encoding files)")
            print("> ./translator.py -d -f [filename] (for decoding files)")
            quit()

#Main function of the script
def main():
    argumentsHandler()

#Running main function
if __name__ == '__main__':
    main()
