def get_positive_int(prompt: str) -> int:
    """Prompt the user for a positive integer and return it."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid positive integer!")


def get_yes_no(prompt: str, default: bool = False) -> bool:
    """Prompt the user to enter 'Y' for Yes or 'N' for No and return the corresponding boolean value."""
    while True:
        default_text = "Yes" if default else "No"
        answer = input(f"{prompt} (Y/N) [default is {default_text}]: ").strip().upper()
        if answer in {"Y", "YES", "N", "NO"}:
            return answer == "Y" or answer == "YES"
        elif answer == "":
            return default
        else:
            print("Please enter 'Y' for Yes or 'N' for No!")