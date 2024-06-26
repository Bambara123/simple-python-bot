import pyautogui
import time
import random
import string
import ctypes


# make the time delay between key presses. between (0.2, 0.5) seconds -> 80%, (0.5, 1) seconds -> 10%, (1, 10) seconds -> 10%
def make_time_delay_normal():
    delay_ranges = [(0, 0.3), (0.3, 1), (1, 10)]
    chosen_range = random.choices(delay_ranges, weights=[85, 10, 5], k=1)[0]

    sleep_time = random.uniform(*chosen_range)

    return sleep_time


# make the time delay between wrong key presses. between (0.2, 0.5) seconds -> 90%, (0.5, 5) seconds -> 10%
def make_time_delay_wrong():
    delay_ranges = [(0.2, 0.5), (0.5, 5)]
    chosen_range = random.choices(delay_ranges, weights=[90, 10], k=1)[0]

    sleep_time = random.uniform(*chosen_range)

    return sleep_time


# imitate mistakes in typing.
def make_mistakes(last_letter):

    last_letter_upper = last_letter.isupper()

    # Will type letters wrongly between 1 to 3.
    amount_of_mistakes = random.randint(1, 3)

    for x in range(amount_of_mistakes):
        mistaken_char = random.choice(
            string.ascii_uppercase if last_letter_upper else string.ascii_lowercase
        )

        pyautogui.typewrite(mistaken_char)
        time.sleep(make_time_delay_wrong())

    for x in range(amount_of_mistakes):
        pyautogui.press("backspace")
        time.sleep(random.uniform(0, 0.1))


def type_char_x(x):
    # Check if the letter is uppercase
    if x.isupper():
        # Check if Caps Lock is off
        if not is_capslock_on():
            # If it's off, turn it on
            pyautogui.press("capslock")
        # Type the letter
        pyautogui.press(x.lower())
    else:
        # Check if Caps Lock is on
        if is_capslock_on():
            # If it's on, turn it off
            pyautogui.press("capslock")
        # Type the letter
        pyautogui.press(x)


def is_capslock_on():
    hllDll = ctypes.WinDLL("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL)


# type a word.
def type_word(word):

    for x in word:

        type_char_x(x)
        time.sleep(make_time_delay_normal())

        mistakes = do_mistakes_or_not()

        if mistakes:
            make_mistakes(x)


def do_mistakes_or_not():
    return random.choices([True, False], weights=[5, 95], k=1)[0]


# make_mistakes("r")
# type_word(
#     "Growing up as the child of a librarian, I was surrounded by books. Pulitzer finalist Lucille Clifton’s affirming words, Gwendolyn Brooks’ tales of Chicago, and Langston Hughes’ lush letters figured prominently in my home. We had quite a bit of Rumi, Shel Silverstein, and Carl Sandburg added in for good measure."
# )
