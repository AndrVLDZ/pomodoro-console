# TODO: Add docstrings
# TODO: Add comments
# TODO: Add type hints
# TODO: Add Try/Except for user input
# TODO: Add a function to check if the user wants to continue
# 

import time
import argparse


class TimeCounter():
    def __init__(self, minutes: int):
        self.minutes = minutes

    def start_count(self, test_mode: bool = False):
        while self.minutes != 0:
            time.sleep(1 if test_mode else 60)
            self.minutes -= 1
            print(f"Time left: {self.minutes} min")
        print("Time's up!\n")
        print("\a")  # Beep sound


class Pomodoro():
    def __init__(
            self,
            cycles: int,
            work_minutes: int,
            rest_minutes: int,
            test_mode: bool = False,
        ):
        self.cycles = cycles
        self.work_minutes = work_minutes
        self.rest_minutes = rest_minutes
        self.test_mode = test_mode

    def start(self):
        print("Test Mode ON!\n") if self.test_mode else None
        try:
            for i in range(self.cycles):
                print(f"Cycle {i + 1}/{self.cycles} started!\n")
                self._work()
                if i != self.cycles - 1:
                    self._rest()
            print("Pomodoro session complete!\n")
            print("\a")
        except KeyboardInterrupt:
            print("Session stopped manually!\n")
            print("\a")

    def _work(self):
        print(f"It's WORK TIME! ==> [{self.work_minutes} min]\n")
        tc_work = TimeCounter(self.work_minutes)
        tc_work.start_count(test_mode=self.test_mode)

    def _rest(self):
        print(f"It's REST TIME! ==> [{self.rest_minutes} min]\n")
        tc_rest = TimeCounter(self.rest_minutes)
        tc_rest.start_count(test_mode=self.test_mode)


def main():
    parser = argparse.ArgumentParser(description="Pomodoro Timer")
    parser.add_argument("cycles", type=int, nargs="?", help="Number of cycles [int]")
    parser.add_argument("work_minutes", type=int, nargs="?", help="Work time in minutes [int]")
    parser.add_argument("rest_minutes", type=int, nargs="?", help="Rest time in minutes [int]")
    parser.add_argument("--test", action="store_true", help="Enable test mode with short time intervals")
    args = parser.parse_args()

    if args.cycles and args.work_minutes and args.rest_minutes:
        cycles = args.cycles
        work_minutes = args.work_minutes
        rest_minutes = args.rest_minutes
        test_mode = args.test
    else:
        print("You can specify parameters when running the script:")
        print("==> python pomodoro.py 4 40 20\n")
        print("And run help to check parameters:")
        print("==> python pomodoro.py -h\n")
        print("Or enter parameters manually:")
        cycles = int(input("1. Enter the number of cycles: "))
        work_minutes = int(input("2. Enter the work time in minutes: "))
        rest_minutes = int(input("3. Enter the rest time in minutes: "))
        test_mode = True if (input("4. Test Mode (Y/N), default is False: ")).upper() == "Y" else False

    pm = Pomodoro(cycles, work_minutes, rest_minutes, test_mode)
    pm.start()


if __name__ == "__main__":
    main()