import base64

def GFadd(a, b):
    if a==1 and b==1:
        return 0
    if a==0 and b==0:
        return 0
    return 1

def main():
    arr = []
    index = []
    for i in range(64):
        arr.append([])
        with open('LIdata/D'+str(i+1), 'r') as R:
            arr[i].append(R.readline().split('\n')[0])
            arr[i].append(R.readline().split('\n')[0])
            arr[i][1] = list(base64.b64decode(arr[i][1]))

    for i in range(64):
        index.append([])
        for j in range(len(arr[i][0])):
            index[i].append(int(arr[i][0][j]))
        index[i].append(1)
        arr[i][0] = index[i]

    for i in range(64):
        if (arr[i][0][i] != 1):
            for k in range(i+1, 64):
                if (arr[k][0][i] == 1):
                    tmp = arr[k]
                    arr[k] = arr[i]
                    arr[i] = tmp
        for j in range(64):
            if i == j:
                continue
            if (arr[j][0][i] == 1):
                for k in range(65):
                    arr[j][0][k] = GFadd(arr[j][0][k], arr[i][0][k])
                for k in range(48):
                    arr[j][1][k] = arr[j][1][k] ^ arr[i][1][k]

    for i in range(64):
        ans = ''
        for j in range(65):
            ans += str(arr[i][0][j])

    for i in range(100):
        encrypted = []
        with open('data/D'+str(i+1), 'r') as R:
            encrypted.append(R.readline().split('\n')[0])
            encrypted.append(R.readline().split('\n')[0])
            encrypted[1] = list(base64.b64decode(encrypted[1]))

        tmp = []
        for j in range(len(encrypted[0])):
            tmp.append(int(encrypted[0][j]))
        tmp.append(1)
        encrypted[0] = tmp

        for j in range(64):
            if encrypted[0][j] == 1:
                for k in range(65):
                    encrypted[0][k] = GFadd(encrypted[0][k], arr[j][0][k])
                for k in range(48):
                    encrypted[1][k] = encrypted[1][k] ^ arr[j][1][k]

        if encrypted[0][64] == 1:
            tmp = [chr(encrypted[1][j]) for j in range(48)]
        ans = ''
        if(tmp[0] != 0):
            for j in range(len(tmp)):
                ans += tmp[j]
            print (ans)
            break



if __name__ == '__main__':
    main()
