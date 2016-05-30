#Program that transform morse code in beeps

#Importing all modules needed
from gpiozero import Button, Buzzer
from time import sleep

#Predefining variables
but = Button(23)
buzz = Buzzer(24)

alphabet = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.','F':'..-.',
            'G':'--.' , 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
            'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
            'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
            'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---',
            '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...',
            '8':'---..', '9':'----.', '.':'.-.-.-', ',':'--..--', '-':'-....-',
            '?':'..--..', '"':'.--..--.', ':':'---...', '@':'.--.-.'}

"""
Funtion that converts text to morse code.
It takes string @text
Returns string @morse
"""
def TextToMorse(text):
    morse = ""
    #spliting into words
    arr = text.split()
    for elem in arr:
        for char in elem:
            morse += alphabet[char.upper()] + "|"
        #noting end of the word
        morse = morse[:-1]
        morse += "||"

    return morse
        
