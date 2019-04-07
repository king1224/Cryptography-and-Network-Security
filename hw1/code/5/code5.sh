nc 140.112.31.96 10152 > otp-1
python3 otp-1.py < otp-1

count=1
while [[ $count -le 500 ]]; do
    nc 140.112.31.96 10153 > otp-2
    python3 data_sampling.py < otp-2 >> data/D${count}
    nc 140.112.31.96 10153 > otp-2
    python3 data_sampling.py < otp-2 >> data/D${count}
    nc 140.112.31.96 10153 > otp-2
    python3 data_sampling.py < otp-2 >> data/D${count}
    nc 140.112.31.96 10153 > otp-2
    python3 data_sampling.py < otp-2 >> data/D${count}
    nc 140.112.31.96 10153 > otp-2
    python3 data_sampling.py < otp-2 >> data/D${count}
    ((count++))
done

g++ -o filter filter.cpp
g++ -o rename rename.cpp
./filter
./rename

python2 test.py
python3 LIdatasorter.py
python3 otp-2.py

rm otp-1 otp-2 filter rename
