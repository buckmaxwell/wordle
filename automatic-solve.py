import time
from solver import Solver
puzzle = Solver()

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.powerlanguage.co.uk/wordle/")

    # Dismiss instructions popup
    page.click("game-modal svg")

    # Enter guess
    guess = 'group'
    page.keyboard.type(guess)
    page.keyboard.press('Enter')

    # Keep browser open
    time.sleep(20)
