# TODO: Fix time left after KeyboardInterrupt

import time
import argparse
from tools import get_positive_int, get_yes_no


class TimeCounter():
    """Class to handle the countdown timer."""
    def __init__(self, minutes: int) -> None:
        self.minutes = minutes

    def start_count(self, test_mode: bool = False) -> None:
        """Start the countdown timer."""
        while self.minutes != 0:
            time.sleep(1 if test_mode else 60)
            self.minutes -= 1
            print(f"Time left: {self.minutes} min")
        print("Time's up!\n")
        print("\a")  # Beep sound


class Pomodoro():
    """Class to handle the Pomodoro sessions."""
    def __init__(
            self,
            cycles: int,
            work_minutes: int,
            rest_minutes: int,
            test_mode: bool = False,
        ) -> None:
        self.cycles = cycles
        self.work_minutes = work_minutes
        self.rest_minutes = rest_minutes
        self.test_mode = test_mode

    def start(self) -> None:
        """Start the Pomodoro session."""
        print("Test Mode ON!\n") if self.test_mode else None
        while True:
            try:
                for i in range(self.cycles):
                    print(f"Cycle {i + 1}/{self.cycles} started!\n")
                    self._work()
                    if i != self.cycles - 1:
                        self._rest()
                print("Pomodoro session complete!\n")
                print("\a")
                next_session = get_yes_no("\nDo you want to start another session?", default=False)
                if not next_session:
                    break
            except KeyboardInterrupt:
                confirm_exit = get_yes_no("\nDo you want to stop the session?", default=False)
                if confirm_exit:
                    print("Session stopped manually!\n")
                    print("\a")
                    break
                else:
                    continue

    def _work(self) -> None:
        """Handle the work period."""
        print(f"It's WORK TIME! ==> [{self.work_minutes} min]\n")
        tc_work = TimeCounter(self.work_minutes)
        tc_work.start_count(test_mode=self.test_mode)

    def _rest(self) -> None:
        """Handle the rest period."""
        print(f"It's REST TIME! ==> [{self.rest_minutes} min]\n")
        tc_rest = TimeCounter(self.rest_minutes)
        tc_rest.start_count(test_mode=self.test_mode)


def start_pomodoro_from_user_input() -> None:
    """Prompt user for input and start the Pomodoro session."""
    cycles = get_positive_int("1. Enter the number of cycles: ")
    work_minutes = get_positive_int("2. Enter the work time in minutes: ")
    rest_minutes = get_positive_int("3. Enter the rest time in minutes: ")
    test_mode = get_yes_no("4. Test Mode", default=False)
    pm = Pomodoro(cycles, work_minutes, rest_minutes, test_mode)
    pm.start()


def main() -> None:
    """Main function to parse args and start the Pomodoro session."""
    parser = argparse.ArgumentParser(description="Pomodoro Timer")
    parser.add_argument("cycles", type=int, nargs="?", help="Number of cycles [int]")
    parser.add_argument("work_minutes", type=int, nargs="?", help="Work time in minutes [int]")
    parser.add_argument("rest_minutes", type=int, nargs="?", help="Rest time in minutes [int]")
    parser.add_argument("--test", action="store_true", help="Enable test mode with short time intervals")
    args = parser.parse_args()

    if all((args.cycles, args.work_minutes, args.rest_minutes)):
        cycles = args.cycles
        work_minutes = args.work_minutes
        rest_minutes = args.rest_minutes
        test_mode = args.test
        pm = Pomodoro(cycles, work_minutes, rest_minutes, test_mode)
        pm.start()
    else:
        print("\nRun the script with arguments, e.g., 'python pomodoro.py 4 40 20 --test'")
        print("Use 'python pomodoro.py --help' to see available options\n")
        print("Or enter parameters manually below:\n")
        start_pomodoro_from_user_input()

if __name__ == "__main__":
    main()