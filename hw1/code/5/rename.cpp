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
    int count=1;
    for(int ca=1; ca<=500; ++ca){
        ss.str("");
        ss << ca;
        string oldname = "data/D" + ss.str();

        ss.str("");
        ss << count;
        string newname = "data/D" + ss.str();

        if(rename(oldname.c_str(), newname.c_str())==0)
            ++count;
    }
    return 0;
}
