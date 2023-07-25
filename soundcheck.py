import random
import time

import pyautogui


PLAY_TIME_SECONDS = 10
TRIES = 3
SOURCES = [
    ('evo4', 400),
    ('cyrus', 420),
]


def play(source_name, source_position):
    pyautogui.click(873, 372)
    pyautogui.click(873, source_position)

    print(f'Playing for {PLAY_TIME_SECONDS} seconds...')
    pyautogui.click(216, 295)
    time.sleep(PLAY_TIME_SECONDS)
    pyautogui.click(264, 295)

    return source_name


def test_loop():
    results = []
    for _ in range(TRIES):
        played = []

        if random.randint(0, 1):
            played.append(play(*SOURCES[0]))
            played.append(play(*SOURCES[1]))
        else:
            played.append(play(*SOURCES[1]))
            played.append(play(*SOURCES[0]))

        chosen = input(f"Which one you liked better? [0, 1] ")
        results.append((played, f"liked {chosen}"))

    for play_order, result in results:
        print(f"{' > '.join(play_order)}, {result}")


if __name__ == '__main__':
    # while True:
    #     print(pyautogui.position())

    test_loop()
