#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int main(){
    fstream fs;
    stringstream ss;
    string s[10];
    for(int ca=1; ca<=500; ++ca){
        ss.str("");
        ss << ca;
        string filename = "data/D" + ss.str();
        fs.open(filename.c_str(), fstream::in);
        for(int i=0; i<10; ++i)
            fs >> s[i];
        fs.close();

        for(int i=0; i<8; i+=2){
            if( (s[i] != s[i+2]) || (s[i+1] != s[i+3])){
                remove(filename.c_str());
                break;
            }
        }
    }
    return 0;
}
