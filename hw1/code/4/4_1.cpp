#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>

using namespace std;

int main(){
    char A[100];
    string S;
    getline(cin, S);
    strcpy(A, S.c_str());
    for(int k=1; k<26; ++k){
        for(int i=0; i<strlen(A); ++i){
            if(A[i]<=122 && A[i]>=97)
                printf("%c", A[i]+k>122?A[i]+k-26:A[i]+k);
            else if(A[i]<='Z' && A[i]>='A')
                printf("%c", A[i]+k>'Z'?A[i]+k-26:A[i]+k);
            else
                printf("%c", A[i]);
        }
        printf("\n");
    }
    return 0;
}
