import hashlib
import hashpumpy
import base64
from netcat import Netcat

def sha256(data):
    m = hashlib.sha256()
    m.updata(data)
    return m.hexdigest()

def main():
    nc = Netcat('140.112.31.96', 10154)

    nc.read_until('>')

    nc.write('2\n')
    nc.read_until('>')
    nc.read_until('>')

    nc.write('1\n')
    token = nc.read_until('>')
    token = token.split('Token: ')[1].split('===')[0][:-1]

    ori_data = '&BALSN_Coin=1'
    app_data = '&BALSN_Coin=100000000000'
    is_invalid = ''
    length = 44
    while 'Here is your flag!' not in is_invalid:
        nc.write('3\n')
        nc.read_until('>')
        nc.read_until('>')
        tmp = hashpumpy.hashpump(token, ori_data, app_data, length)
        nc.write(base64.b64encode(tmp[1].split('Coin=', 1)[1]) + '\n')
        nc.read_until('>')
        nc.write(tmp[0]+'\n')
        is_invalid = nc.read_until('>')
        if 'Here is your flag!' in is_invalid:
            print is_invalid.split('Here is your flag!')[1][1:].split('\n===')[0]
            exit(1)
        length += 1
        if length > 54:
            break
    exit(0)

if __name__ == '__main__':
    main()
