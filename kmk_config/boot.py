import supervisor
import board
import storage
import usb_cdc
from digitalio import DigitalInOut,Pull


supervisor.set_next_stack_limit(4096 + 4096)

led = DigitalInOut(board.GP16)
led.switch_to_output()

button = DigitalInOut(board.GP14)
button.switch_to_input(Pull.UP)

led.value = True
supervisor.disable_autoreload()

if button.value is False:
    print("Mode développement activé")
    led.value = False

else:
    print("Mode Standard activé")
    storage.disable_usb_drive()
    usb_cdc.disable()
