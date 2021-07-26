import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.consts import UnicodeMode
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()
layers = Layers()
modtap = ModTap()
keyboard.modules = [layers, modtap, encoder]

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, /
                     board.GP8, board.GP0, board.GP10, board.GP11, board.GP12, board.GP13)
keyboard.row_pins = (board.GP28, board.GP27, board.GP22, board.GP26, board.GP21)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

keyboard.tap_time = 250
keyboard.debug_enabled = False


# Filler keys
_______ = KC.TRANS
xxxxxxx = KC.NO
tbdtbd = KC.NO

# Custom keys


# Layers
LYR_STD, LYT_EXT, LYR_NUM, LYR_GAME = 0,1,2,3

TO_STD = KC.DF(LYR_STD)
MT_EXT = KC.MT(LYR_EXT)
TO_NUM = KC.DF(LYR_NUM)
TO_GAME = KC.DF(LYR_GAME)


# Keycaps

keyboard.keymap = [
    # Standard Layer
    [
    KC.ESC , KC.1   , KC.2   , KC.3   , KC.4   , KC.5   , KC.6   , KC.7   , KC.8   , KC.9   , KC.0   , KC.MINS, KC.EQL , KC.BSPC,
    KC.TAB , KC.Q   , KC.W   , KC.E   , KC.R   , KC.T   , KC.Y   , KC.U   , KC.I   , KC.O   , KC.P   , KC.LBRC, KC.RBRC, KC.DEL ,
    xxxxxxx, KC.A   , KC.S   , KC.D   , KC.F   , KC.G   , KC.H   , KC.J   , KC.K   , KC.L   , KC.SCLN, KC.QUOT, KC.BSLS, xxxxxxx,
    KC.LSFT, tbdtbd , KC.Z   , KC.X   , KC.C   , KC.V   , KC.B   , KC.N   , KC.M   , KC.COMM, KC.DOT , KC.SLSH, KC.UP  , KC.ENT ,
    KC.LCTL, KC.LGUI, xxxxxxx, KC.LALT, MT_EXT , xxxxxxx, KC.SPC , xxxxxxx, KC.RALT, KC.tbd , KC.RSFT, KC.LEFT, KC.DOWN, KC.RGHT,
    ],
    # Extra Keys Layer
    [
    TO_STD , KC.F1  , KC.F2  , KC.F3  , KC.F4  , KC.F5  , KC.F6  , KC.F7  , KC.F8  , KC.F9  , KC.F10 , KC.F11 , KC.F12 , TO_NUM ,
    xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, _______, 
    xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, 
    KC.LSFT, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, KC.PGUP, xxxxxxx, 
    KC.LCTL, KC.LGUI, xxxxxxx, KC.LALT, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, KC.HOME, KC.PGDN, KC.END , 
    ],
    # NumPad Layer
    [
    TO_STD , xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, KP.P7  , KC.P8  , KC.P9  , KC.PSLS, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, 
    xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, KP.P4  , KC.P5  , KC.P6  , KC.PAST, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, 
    xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, KC.N5  , KC.P1  , KC.P2  , KC.P3  , KC.PPLS, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, 
    xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, KC.MINS, KC.P0  , KC.PDOT, _______, KC.PMNS, xxxxxxx, xxxxxxx, xxxxxxx, KC.PENT, 
    xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, 
    ],
    # Gaming Layer
    [
    TO_STD , xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, 
    xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, 
    xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, 
    xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, 
    xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, 
    ],
]

# Rotary Encoder (1 encoder / 1 definition per layer
encoder_map = [
  # Standard
  [(KC.tbd, KC.tbd, 1),],
  # Extra
  [(KC.tbd, KC.tbd, 1),],
  # NumPad
  [(KC.tbd, KC.tbd, 1),],
  # Gaming
  [(KC.tbd, KC.tbd, 1),],
] 
encoder = Encoder([board.GP22, board.GP15, button_pin = 14)
encoder.encoders[0].is_inverted = True


if __name__ == '__main__':
    keyboard.go()



"""
import os
import time
import board
import busio
import displayio
import terminalio
import rotaryio
import adafruit_displayio_ssd1306
from adafruit_display_text import label

displayio.release_displays()
print()
print("Machine: \t\t\t" + os.uname()[4])
print("CircuitPython: \t\t\t" + os.uname()[3])
print()
print("Machine: \t\t\t" + os.uname()[4])
print("CircuitPython: \t\t\t" + os.uname()[3])


SDA = board.GP8
SCL = board.GP9
i2c = busio.I2C(SCL, SDA)

if(i2c.try_lock()):
    print("i2c.scan(): " + str(i2c.scan()))
    i2c.unlock()
print()

ssd1306_i2c_addr = 60
display_width =128
display_height = 32
NUM_OF_COLOR = 2
display_bus = displayio.I2CDisplay(i2c, device_address=ssd1306_i2c_addr)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=display_width, height=display_height)


group = displayio.Group(max_size=10)


bitmap = displayio.Bitmap(display_width, display_height, NUM_OF_COLOR)
bitmap_palette = displayio.Palette(NUM_OF_COLOR)
bitmap_palette[0] = 0x000000
bitmap_palette[1] = 0xFFFFFF

tileGrid = displayio.TileGrid(bitmap,
                              pixel_shader=bitmap_palette,
                              x=0, y=0)
group.append(tileGrid)

# Draw a label
text_group = displayio.Group(max_size=10, scale=2)

text_position = label.Label(terminalio.FONT, text="temperature:", color=0xFFFFFF)
text_position.anchor_point = (0.0, 0.0)
text_position.anchored_position = (0, 0)

text_group.append(text_position)
group.append(text_group)

display.show(group)


encoder = rotaryio.IncrementalEncoder(board.GP15, board.GP16)
last_position = None


while True:
    position = encoder.position
    if last_position is None or position != last_position:
        print(position)
        text_position.text = "%s" % position
    last_position = position
"""
