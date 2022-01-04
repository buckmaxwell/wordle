import time
import json
from solver import Solver
puzzle = Solver()

from playwright.sync_api import sync_playwright

def convert_feedback_to_solver_format(feedback):
    feedback_new_format = ""

    for i in feedback:
        if (i == 'absent'):
            feedback_new_format += '-'
        elif (i == 'present'):
            feedback_new_format += '!'
        elif (i == 'correct'):
            feedback_new_format += 'x'

    return feedback_new_format

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.powerlanguage.co.uk/wordle/")

    # Dismiss instructions popup
    page.click("game-modal svg")

    feedback_solver_format = '-----'
    remaining_guesses = 6

    while (feedback_solver_format != 'xxxxx' or remaining_guesses > 0):

        # Enter guess
        page.keyboard.type(puzzle.guess)
        page.keyboard.press('Enter')

        # Check guess feedback
        browser_state_path = "state.json"
        context.storage_state(path=browser_state_path)
        browser_state = open(browser_state_path)
        browser_state_json = json.load(browser_state)
        all_guess_feedback = json.loads(browser_state_json['origins'][0]['localStorage'][0]['value'])['evaluations']
        recent_guess_feedback = [i for i in all_guess_feedback if i][-1]
        feedback_solver_format = convert_feedback_to_solver_format(recent_guess_feedback)
        print(feedback_solver_format)

        # Find remaining guesses
        remaining_guesses = len([i for i in all_guess_feedback if not i])

        # Generate the next guess
        puzzle.set_next_guess(feedback_solver_format)

        # Some time between tries to appreciate the visuals
        # (also not doing this causes it to progress too fast and crash)
        time.sleep(5)

    # Keep browser open long enough to see results
    time.sleep(20)

    context.close()
