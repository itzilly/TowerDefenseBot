import logging
import pyautogui as screen


def next_wave():
    # Click the 'Next Wave' button
    screen.leftClick(x=269, y=918)
    logging.info("Skipping to next wave of enemies")


def start_waves():
    # Click the 'Start Waves' button
    screen.leftClick(x=269, y=918)
    logging.info("Starting waves")


def select_level(level_number):
    if level_number == 1.1:
        x = 115
        y = 520
    elif level_number == 1.2:
        x = 182
        y = 520
    elif level_number == 2:
        x = 115
        y = 400
    elif level_number == 3:
        x = 115
        y = 655
    elif level_number == 4:
        x = 258
        y = 266
    elif level_number == 5:
        x = 258
        y = 319
    elif level_number == 6:
        x = 258
        y = 400
    elif level_number == 7:
        x = 258
        y = 515
    elif level_number == 8:
        x = 258
        y = 637
    # elif level_number == 9:
    #     x = 258
    #     y = 755
    else:
        x = 258
        y = 755
    screen.leftClick(x=x, y=y)
    logging.info("Selected stage {}".format(level_number))
