import time
import logging
import pyautogui as screen

from levels import T1_1
from utils import gamegui


def setup_logger():
    logging_format = '[%(asctime)s %(levelname)s] %(message)s'
    date_strftime_format = "%H:%M:%S"
    logging.basicConfig(level=logging.INFO, datefmt=date_strftime_format, format=logging_format)


def run():
    logging.info("Loading bot...")
    time.sleep(9)
    logging.info("Bot loading complete!")

    logging.info("Loading game...")
    screen.PAUSE = .35
    screen.leftClick(x=472, y=665)  # Continue button
    time.sleep(7)  # Wait for animation to finish
    logging.info("Game load complete!")
    screen.leftClick(x=255, y=395)  # Click Play button to get to Stage Select

    # Select Level
    gamegui.select_level(1.1)  # Tutorial 1.1

    # Play The Tutorial
    T1_1.play()


if __name__ == "__main__":
    setup_logger()
    run()
    print("Done!")
