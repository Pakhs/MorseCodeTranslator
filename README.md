# Morse Code Translator

A very simple python morese code that can encode and decode morse code

## Installation

Download the [zip file](https://github.com/Pakhs/MorseCodeTranslator/archive/refs/heads/main.zip) or clone the repository on your specified directory

```bash
git clone https://github.com/Pakhs/MorseCodeTranslator.git
```

# Usage
## Encoding string

```bash
./translator.py -e
```
Example:
 
![Example](https://github.com/Pakhs/MorseCodeTranslator/blob/main/img/encode.png)

## Decoding string

```bash
./translator.py -d
```
Example:
 
![Example](https://github.com/Pakhs/MorseCodeTranslator/blob/main/img/decode.png)

## Encoding File
You can only encode a file that contains alphanumeric characters\
Each line of the file will be kept as is, each word and letter follows the rules of the basic encoding
```bash
./translator.py -e -f "filename"
```

## Decoding file
Not yet implemented
