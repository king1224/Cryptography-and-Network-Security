import random
import time
import base64

def main():
    t = int(time.time())
    encrypted = input()
    encrypted = list(base64.b64decode(encrypted))
    random.seed(t)
    encrypted = [chr(i ^ random.randint(0, 255)) for i in encrypted]
    result = ''
    for i in encrypted:
        result += i
    print (result)

if __name__ == "__main__":
    main()
