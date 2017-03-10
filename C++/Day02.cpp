#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    float cost,totalCost,tipPercent,taxPercent,tip,tax;
    cin >> cost >> tipPercent >> taxPercent;

    tip = (tipPercent/100)*cost;
    tax = (taxPercent/100)*cost;

    totalCost = tip+tax+cost;

    if (totalCost > int(totalCost) + 0.5) {
        totalCost=int(totalCost)+1;
    }
    else {
        totalCost = int(totalCost);
    }

    cout << "The total meal cost is " << totalCost << " dollars.";
    return 0;
}
