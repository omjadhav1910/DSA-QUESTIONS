#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, d;
    cin >> n >> d;
    
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    vector<int> rotated_arr(n);
    for (int i = 0; i < n; ++i) {
        rotated_arr[(i + n - d) % n] = arr[i];
    }

    for (int i = 0; i < n; ++i) {
        cout << rotated_arr[i] << " ";
    }
    cout << endl;

    return 0;
}
