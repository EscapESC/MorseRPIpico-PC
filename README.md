# MorseRPIpico-PC

> [!Note]
> This program was originally designed for the game [Wolfpack](https://store.steampowered.com/app/490920/Wolfpack/) and it works with it by default.
## Introdution
MorseRPIz-PC is a program for Raspberry Pi pico / w for reading the output of a Morse Key and transfering it into key presses of a designated key / decoding morse into keyboard presses. (Modes and keys you can change in the `code.py` file on the 16,18,19th row.)
> [!Note]
> The default key is RIGHT_CONTROL

> [!Tip]
> The build in LED will visualise the morse signal recived. 

### Modes
The program has two output modes. 
   - morse(0) this outputs a morse signal to a single button.
   - keyboard(1) this mode outputs keyboard presses.
> [!Note]
> The keyboard mode depends on yours keyboard layout. ( changes z and y for QWERTZ layouts etc...)

## Installation

1. Pick the right version of the .UF2 file, depending on your Raspberry Pi pico version.
> Your RPI pico will then reboot and show as `CIRCUITPY`.

2. Copy `code.py` and `lib` folder into the root directory of the `CIRCUITPY`.

3. Depending on your key: 
   - If you have a standard morse key, then connect it to the `3.3v(OUT)` and `GP0` pin.
   - If you have a self powered key with output, then connect it to the `GND` and `GP0` pin.
   
5. Have fun.

### Raspberry Pi pico layout :
![Official Raspberry Pi pico layout](https://www.raspberrypi.com/documentation/microcontrollers/images/pico-pinout.svg)


### Raspberry Pi pico W layout :
![Official Raspberry Pi pico layout](https://www.raspberrypi.com/documentation/microcontrollers/images/picow-pinout.svg)


> [!Tip]
> 1. GP0 - Sinal reciver, 3. GND - Common ground pin, 36. 3.3v(OUT) - 3.3v DC power source pin


## Keycode list

[Source code for adafruit_hid.keycode](https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html)

## How to reset your Raspberry Pi.
Follow these instructions if your Pico ends up in an odd state

1. Download the reset firmware from [flash_nuke.uf2](https://datasheets.raspberrypi.com/soft/flash_nuke.uf2)
2. While holding the BOOTSEL button on the Pico, plug in the USB cable to your computer.
3. When the RPI-RP2 drive shows up on your computer, copy the flash_nuke.uf2 file to the Pico
4. After the device reboots, follow the Install instructions [here](https://github.com/dbisu/pico-ducky/blob/main/README.md)

