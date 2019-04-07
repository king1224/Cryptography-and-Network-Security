import base64

def main():
    c = raw_input()
    m = base64.b64decode(c)
    print m

if __name__ == '__main__':
    main()
