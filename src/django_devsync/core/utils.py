def confirm():
    while True:
        check = (
            input("⚠️ Are you sure you want to continue? [yes/no]: ")
            .strip()
            .lower()
        )
        if check in ("yes", "no"):
            return check == "yes"

        print("Please enter 'yes' or 'no'...")
