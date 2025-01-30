import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import board
import digitalio

#Created by VR aka EscapESC aka Freddy

print("Initiating MorseRPIz-PC ...")

keyboard = Keyboard(usb_hid.devices)
layout = Keycode(keyboard)

###### Edit "Button" to your designated button ######
button = layout.RIGHT_CONTROL
###### Output mode. 0  #######
mode = 0
wpm = 20
#####################################################

#Get LED for morse visualtion
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

led.value = True

#Get input pins from the morseKey
input = digitalio.DigitalInOut(board.GP0)
input.direction = digitalio.Direction.INPUT
input.pull = digitalio.Pull.UP

led.value = False

morse = False

print("... Initiated Sucessfully.")

while mode == 0 :

    if morse != input.value :
        morse = input.value
        if morse == True :
            keyboard.release(button)
            led.value = False
        elif morse == False :
            keyboard.press(button)
            led.value = True
            
    time.sleep(0.01)

morseChar = ""
wordStart = False

def decodeMorse(encodedChar):
    MORSE_CODE_DICT = {
  '.-': layout.A, '-...': layout.B, '-.-.': layout.C, '-..': layout.D, '.': layout.E,
  '..-.': layout.F, '--.': layout.G, '....': layout.H, '..': layout.I, '.---': layout.J,
  '-.-': layout.K, '.-..': layout.L, '--': layout.M, '-.': layout.N, '---': layout.O,
  '.--.': layout.P, '--.-': layout.Q, '.-.': layout.R, '...': layout.S, '-': layout.T,
  '..-': layout.U, '...-': layout.V, '.--': layout.W, '-..-': layout.X, '-.--': layout.Y,
  '--..': layout.Z, '.----': layout.ONE, '..---': layout.TWO, '...--': layout.THREE,
  '....-': layout.FOUR, '.....': layout.FIVE, '-....': layout.SIX, '--...': layout.SEVEN,
  '---..': layout.EIGHT, '----.': layout.NINE, '-----': layout.ZERO, '--..--': layout.COMMA,
  '.-.-.-': layout.PERIOD, '..--..': layout.FORWARD_SLASH, '-..-.': layout.BACKSLASH,
  '-....-': layout.MINUS, '-.--.': layout.LEFT_BRACKET, '-.--.-': layout.RIGHT_BRACKET
}
    return MORSE_CODE_DICT.get(encodedChar, -1)

pauseStart : float
pauseEnd : float
keyStart : float
keyEnd : float

while input.value == True:
    pauseStart = 0
pauseStart = time.monotonic()
while mode == 1 :

    if time.monotonic()-pauseStart > 60/(50*wpm)*3:
        buttonKey = decodeMorse(morseChar)
        if(buttonKey != -1):
            keyboard.press(buttonKey)
            keyboard.release(buttonKey)
        morseChar = ""

    if input.value == False:
        pauseEnd = time.monotonic()
        keyStart = time.monotonic()
        if pauseEnd-pauseStart < 60/(50*wpm)*3:
            morseChar = morseChar
        elif pauseEnd-pauseStart < 60/(50*wpm)*7:
            morseChar = ""
        elif pauseEnd-pauseStart > 60/(50*wpm)*7:
            keyboard.press(layout.SPACEBAR)
            keyboard.release(layout.SPACEBAR)
            morseChar = ""

        while input.value == False:
            led.value = True
        led.value = False
        keyEnd = time.monotonic()
        if keyEnd - keyStart < 60/(50*wpm)*2.5 :
            morseChar = morseChar + "."
        else:
            morseChar = morseChar + "-"
        pauseStart = time.monotonic()
