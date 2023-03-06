import hashlib
import sys
import time


def found(s: str, start: float):
    print("\nThe code is " + s)
    end = time.time()
    print("Elapsed time:", end - start, "s")
    raise StopIteration


def not_found():
    print("\nUnnable to find the code.")


def six():
    start_time = time.time()
    try:
        search = input("Hashcode: ")
        for a in range(10):
            for b in range(10):
                for c in range(10):
                    for d in range(10):
                        for e in range(10):
                            for f in range(10):
                                s = str(a) + str(b) + str(c) + str(d) + str(e) + str(f)
                                hash = hashlib.md5(s.encode('utf-8')).hexdigest()
                                sys.stdout.write("\rProgress: " + s + " - " + hash)

                                if search == hash:
                                    found(s, start_time)

                                if s == "999999":
                                    not_found()

                                sys.stdout.flush()
    except StopIteration:
        pass


def four():
    start_time = time.time()
    try:
        search = input("Hashcode: ")
        for a in range(10):
            for b in range(10):
                for c in range(10):
                    for d in range(10):
                        s = str(a) + str(b) + str(c) + str(d)
                        hash = hashlib.md5(s.encode('utf-8')).hexdigest()
                        sys.stdout.write("\rProgress: " + s + " - " + hash)

                        if search == hash:
                            found(s, start_time)

                        if s == "9999":
                            not_found()

                        sys.stdout.flush()
    except StopIteration:
        pass


def start():
    active = True
    while active:
        s = input("Do you want to decode 4 or 6 digits code? ")
        if s in ("q", "Q"):
            active = False
            break
        if s == "4":
            active = False
            four()
        elif s == "6":
            active = False
            six()
        else:
            print("---")
            print("Error: 4 and 6 are only available options.")
            print("Type Q to exit.")
            print("---")

if __name__ == "__main__":
    start()
