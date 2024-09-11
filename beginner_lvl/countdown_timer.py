import time


def countdown(seconds):
    print("Countdown started:")
    for i in range(seconds, 0, -1):
        print(f"{i}..")
        time.sleep(1)
    print("Time's up!")

countdown(int(input("Set a timer: ")))

