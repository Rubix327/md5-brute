import hashlib
import sys
import time


def found(code: str, start_time: float):
    end_time = time.time()
    elapsed = end_time - start_time
    print("\nThe code is " + code + " (found in " + f'{elapsed:.2f}' + "s)")


def not_found():
    print("\nUnnable to find the code.")


def uni(d: int):
    start_time = time.time()
    search = input("Hashcode: ")
    max_n = 10 ** d
    last_s = str(max_n - 1).zfill(d)

    for i in range(max_n):
        code = str(i).zfill(d)
        hsh = hashlib.md5(code.encode('utf-8')).hexdigest()
        progress = "{:.2f}".format(i / (max_n - 1) * 100)
        sys.stdout.write("\rProgress (" + progress + "%): " + code + " - " + hsh)

        if search == hsh:
            found(code, start_time)
            break

        if code == last_s:
            not_found()

        sys.stdout.flush()


def start():
    active = True
    while active:
        amount = input("How many digits are in the code? ")
        if amount in ("q", "Q"):
            active = False
            break

        if amount.isdigit():
            uni(int(amount))
            active = False
        else:
            print("---")
            print("Error: only integer digits are available.")
            print("Type Q to exit.")
            print("---")

if __name__ == "__main__":
    start()
