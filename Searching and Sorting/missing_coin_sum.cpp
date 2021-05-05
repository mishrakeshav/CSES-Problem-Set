#include <bits/stdc++.h>
using namespace std;
int main(){
    int n , xi;
    cin >> n;
    vector<int> arr;
    for(int i=0; i < n; i++){
        cin >> xi;
        arr.push_back(xi);
    }
    /*
    Brute-Force approach 
        Find the sum of subset and sort them
        then find the first smallest number which is 
        not in the list
    Efficient approarch 
        1. Sort the array 
        2. Start with index 0 and res = 1 
        3. if arr[index] > res + 1 return res + 1 
        4. res += 1 
    */
    sort(arr.begin(),arr.end());
    long long res = 1;
    for(int i = 0; i < n ; i++){
        if(arr[i] <= res){
          res += arr[i];  
        } 
        else {
            cout << res << endl;
            return 0;
        }
    }
    cout << res << endl;

    return 0;
}
