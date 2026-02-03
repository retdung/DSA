#include <bits/stdc++.h>

using namespace std;

int main() {
    double total = 0;
    cout << fixed << setprecision(2); 

    for (int i = 1; i <= 10; ++i) {
        string name = "data" + string(i < 10 ? "0" : "") + to_string(i) + ".txt";

        ifstream f(name);
        if (!f) continue;
        vector<double> v; double d;
        while (f >> d) v.push_back(d);

        auto start = chrono::high_resolution_clock::now();
        sort(v.begin(), v.end());
        double ms = chrono::duration<double, milli>(chrono::high_resolution_clock::now() - start).count();

        cout << name << " | " << ms << "\n";
        total += ms;
    }
    cout << "AVERAGE    | " << total / 10 << "\n";
    return 0;
}
