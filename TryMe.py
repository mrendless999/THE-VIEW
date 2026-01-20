import random
import sys

def str_xor(secret, key):
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
    return "".join([chr(a ^ ord(b)) for (a,b) in zip(secret,new_key)])

flag_enc =[42, 42, 50, 36, 46, 41, 18, 43, 41, 39, 49, 17, 23, 16, 55, 60, 11, 12, 24, 27]

def print_flag():
    key = "pythonisfun"
    flag = str_xor(flag_enc, key)
    print(flag)

def print_encouragement():
    msgs = [
        "Keep going!",
        "Maybe try something else...",
        "Persistence is key!"
    ]
    print(random.choice(msgs) + "\n")

def main():
    print(r'''
        ==========================
             TryME Challenge
        ==========================
        ''')
    print("Welcome challenger!\n")

    while True:
        print("a) Motivation")
        print("b) Reveal secret")
        print("c) Exit\n")

        choice = input("Choose (a/b/c): ")

        if choice == 'a':
            print_encouragement()

        elif choice == 'b':
            print("\nNot so fast.",
                  "\nInspect the code to uncover the truth...\n")

        elif choice == 'c':
            sys.exit(0)

        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
