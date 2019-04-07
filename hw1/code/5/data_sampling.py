import random
import time
import base64

def main():
    random.seed(int(time.time()))
    key_index = random.randint(0,(2**64)-1)
    encrypted = input()
    print('{:064b}'.format(key_index))
    print(encrypted)

if __name__ == "__main__":
    main()
