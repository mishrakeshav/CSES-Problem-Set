#include <bits/stdc++.h>
#include <sys/resource.h>

int main() {
    rlimit cpu_time{.rlim_cur = 1, .rlim_max = 5}; 
    setrlimit(RLIMIT_CPU, &cpu_time);
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    int n, c;
    cin >> n >> x;
    vector<int> arr(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    sort(arr.begin(), arr.end())
    int i = 0;
    int j = n -1;
    int s, k;
    while(i < j){
        s = arr[i] + arr[j];
        k = 
    }
}
