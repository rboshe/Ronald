import ccircle
from math import *


window = ccircle.Window("Let's just get it working!")
time = 0
while window.isOpen():
    window.clear(0, 0, 1)
   # window.drawRect( 16,16, 128, 32 + 32 * (0.5 + 0.5 * cos(time)))
    height = 16 + 16  *(1 + 1 *cos(time))
    time += 0.01
    window.drawCircle(150, 150, 38)
    window.drawCircle(450, 150, 38)
    window.drawCircle(300, 300, 76)

    window.update()