#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

int main(){
    char A[100];
    char B[100];
    char C[100];
    char D[100];
    string S;
    int deep=0;
    cin >> S >> S >> S;
    getchar();
    getline(cin, S);
    strcpy(A, S.c_str());
    cin >> S >> S >> S;
    getchar();
    getline(cin, S);
    strcpy(B, S.c_str());
    cin >> S >> S >> S;
    getchar();
    getline(cin, S);
    strcpy(C, S.c_str());
    for(int i=1; i<strlen(A); ++i){
        int pos = 0;
        bool match = true;
        for(int j=0; j<strlen(A); j+=i*2){
            if(A[pos++] != B[j]){
                match = false;
                break;
            }
        }
        for(int j=1; j<i; ++j){
            for(int k=j; k<strlen(A); k+=i*2){
                if(A[pos++] != B[k]){
                    match = false;
                    break;
                }
                if(k+(i-j)*2<strlen(A) && A[pos++] != B[k+(i-j)*2]){
                    match = false;
                    break;
                }
            }
            if(!match)
                break;
        }
        for(int j=i; j<strlen(A); j+=i*2){
            if(A[pos++] != B[j]){
                match = false;
                break;
            }
        }
        if(match){
            deep = i;
            break;
        }
    }
    if(!deep)
        return 0;

    int pos = 0;
    for(int j=0; j<strlen(C); j+=deep*2){
        D[j] = C[pos++];
    }
    for(int j=1; j<deep; ++j){
        for(int k=j; k<strlen(C); k+=deep*2){
            D[k] = C[pos++];
            if(k+(deep-j)*2<strlen(C))
                D[k+(deep-j)*2] = C[pos++];
        }
    }
    for(int j=deep; j<strlen(C); j+=deep*2){
        D[j] = C[pos++];
    }
    D[pos] = '\0';
    printf("%s\n",D);

    return 0;
}
