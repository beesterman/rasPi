from gpiozero import LED
from gpiozero import Button
from time import sleep

red = LED(17)
button = button(2)




while True:
    if button.is_pressed:
        red.off()
    else:
        red.on()






    # red.on()
    # sleep(1)
    # red.off()
    # sleep(1)