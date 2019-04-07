from netcat import Netcat

def main():
    for i in range(3):
        nc = Netcat('140.112.31.96', 10155)
        N = nc.read().split('N = ')[1]
        c = N.split('c = ')[1][:-1]
        N = N.split('c = ')[0][:-1]
        with open('data/ciphertext.'+str(i+1), 'w') as W:
            W.write(c)
        with open('data/modulus.'+str(i+1), 'w') as W:
            W.write(N)

if __name__ == '__main__':
    main()
