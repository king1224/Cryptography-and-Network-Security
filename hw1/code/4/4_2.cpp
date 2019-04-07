#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>

using namespace std;

int main(){
    char A[100];
    char B[100];
    char C[100];
    char table[7];
    string S;
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
    for(int i=0; i<strlen(A); ++i){
        if(A[i]<=122 && A[i]>=97){
            table[i%7] = A[i]-B[i]+'a'<97?A[i]-B[i]+'a'+26:A[i]-B[i]+'a';
        }
        else if(A[i]<=90 && A[i]>=65){
            table[i%7] = A[i]-B[i]+'A'<65?A[i]-B[i]+'A'+26:A[i]-B[i]+'A';
        }
    }

    for(int i=0; i<strlen(C); ++i){
        if(C[i]<=122 && C[i]>=97)
            printf("%c",C[i]-table[i%7]+'a'<97?C[i]-table[i%7]+'a'+26:C[i]-table[i%7]+'a');
        else if(C[i]<='Z' && C[i]>='A')
            printf("%c",C[i]-table[i%7]+'a'<'A'?C[i]-table[i%7]+'a'+26:C[i]-table[i%7]+'a');
        else
            printf("%c",C[i]);
    }
    printf("\n");
    return 0;
}
