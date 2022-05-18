import time
import logging
import pyautogui as screen

from utils import tower
from utils.gamegui import next_wave, start_waves


def play():
    logging.info("Playing 'Tutorial Part 1'")
    time.sleep(.6)
    screen.PAUSE = .05

    # Click though tutorial
    time.sleep(1)
    screen.leftClick(x=713, y=609)
    screen.leftClick(x=713, y=673)
    screen.leftClick(x=713, y=630)
    screen.leftClick(x=716, y=750)
    screen.leftClick(x=742, y=465)
    screen.leftClick(x=600, y=767)

    start_waves()

    # Place starting towers
    screen.PAUSE = .02
    screen.press('t')
    screen.moveTo(x=310, y=400)
    screen.leftClick()
    screen.moveTo(x=310, y=342)
    screen.leftClick()
    screen.moveTo(x=400, y=314)
    screen.leftClick()
    screen.moveTo(x=400, y=370)
    screen.leftClick()
    screen.moveTo(x=400, y=432)
    screen.leftClick()
    screen.moveTo(x=586, y=491)
    screen.leftClick()
    screen.moveTo(x=586, y=600)
    screen.leftClick()

    time.sleep(.2)
    screen.leftClick(x=706, y=616)  # Press 'Continue'
    time.sleep(.2)

    screen.PAUSE = .05
    # Upgrade
    tower.select(283, 570)
    tower.upgrade(1)

    tower.select(283, 517)
    tower.upgrade(1)

    tower.select(313, 454)
    tower.upgrade(1)

    tower.select(582, 485)
    tower.upgrade(1)

    # Wave 2 (Fast)
    next_wave()
    time.sleep(.8)
    screen.leftClick(x=706, y=626)  # Press 'Continue'

    time.sleep(.4)
    tower.select(586, 600)
    tower.upgrade(1)

    time.sleep(2.2)  # Let the level play for 2.2 seconds

    # Wave 3 (Ghost)
    next_wave()
    time.sleep(.7)  # Wait for information screen
    screen.leftClick(x=717, y=703)  # Press 'Continue'
    time.sleep(1.2)  # Play level for 1.2 seconds

    time.sleep(.4)
    tower.select(283, 517)
    tower.upgrade(2)  # Machine Gun

    # Wave 4 (Basic)
    next_wave()
    time.sleep(3.8)  # Play level for 3.8 seconds

    # Wave 5 (Fast)
    next_wave()
    time.sleep(3.9)  # Play level for 3.9 seconds

    # Wave 6
    next_wave()
    time.sleep(3)

    # Wave 7
    next_wave()
    time.sleep(4)

    # Wave 8
    next_wave()
    time.sleep(4)

    # Wave 9
    next_wave()
    time.sleep(3)

    # Wave 10
    next_wave()
    time.sleep(3)

    # Select Stage
    time.sleep(6)

    time.sleep(4)
    screen.leftClick(x=259, y=693)
