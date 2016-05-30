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
#one unit in seconds
UNITSEC = 0.25

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

def Beep(units):
    buzz.on()
    sleep(units * UNITSEC)
    buzz.off()

def MorseToBeep(morse):
    for i in range(len(morse)):
        #New word
        if(i < len(morse) - 1 and '|' == morse[i] and '|' == morse[i+1]):
            sleep(7 * UNITSEC)
        #new character
        elif('|' == morse[i]):
            sleep(3 * UNITSEC)
        #Dash
        elif('-' == morse[i]):
            Beep(3 * UNITSEC)
            sleep(1 * UNITSEC)
        #dot
        elif('.' == morse[i]):
            Beep(1 * UNITSEC)
            sleep(1 * UNITSEC)

    print ("Morse complete")

MorseToBeep(TextToMorse('SOS'))
MorseToBeep(TextToMorse('Rok Kos'))
        
