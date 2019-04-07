import os
import shutil

def main():
    arr = []
    for i in range(64):
        with open('data/D'+str(i+1), 'r') as R:
            arr.append(R.readline().split('\n')[0])

    arr.sort()

    re_arr = []
    for i in range(64):
        with open('data/D'+str(i+1), 'r') as R:
            tmp = R.readline().split('\n')[0]
            for j in range(64):
                if(tmp == arr[j]):
                    re_arr.append(j)
                    break;

    for i in range(64):
        shutil.copyfile('data/D'+str(i+1), 'LIdata/D'+str(re_arr[i]+1))

if __name__ == '__main__':
    main()
