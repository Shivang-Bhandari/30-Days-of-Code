#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int num;
    cin >> num;
    for(int j=0;j<num;j++){
        string str;
        cin >> str;
        int strLength = str.length();
        for(int i=0;i<strLength;i+=2){
            cout << str[i];
        }
        cout << " ";
        for(int i=1;i<strLength;i+=2){
            cout << str[i];
        }
        cout<<'\n';
    }
    
    return 0;
}
