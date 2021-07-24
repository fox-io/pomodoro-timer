"""
1. Decide on the task to be done.
2. Set the timer to 25 minutes.
3. Work on task until timer ends.
4. Take 5 minute break.
5. Repeat 1-4 4 times.
6. Take 15-30 minute break.
"""
import time


def start_timer(minutes, label):
    seconds = minutes * 60
    while seconds > 0:
        print(f"{label} for {minutes} minutes. {seconds}")
        time.sleep(1)
        seconds -= 1


def main():
    for round_num in range(1, 4):
        start_timer(25, "Work")
        start_timer(5, "Break")
    start_timer(15, "Break")


if __name__ == "__main__":
    main()
