import logging

import pyautogui as screen


def upgrade(upgrade_number):
    screen.press(str(upgrade_number))
    logging.debug("Upgraded tower - Slot: {}".format(upgrade_number))


def select(x, y):
    screen.leftClick(x=x, y=y)


def build(x, y):
    screen.moveTo(x=x, y=y)
    screen.leftClick()
