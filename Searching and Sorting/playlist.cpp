#include <bits/stdc++.h>
#include <sys/resource.h>
#define mod 1000000007
#define pb push_back
#define ff first
#define ss second
#define ii pair<int,int>
#define vi vector<int>
#define vii vector<ii>
#define lli long long int
#define INF 1000000000
#define endl '\n'
#define ar array
const double PI = 3.141592653589793238460;
const int mxN = 2e5;
typedef std::complex<double> Complex;
typedef std::valarray<Complex> CArray;
using namespace std;
int arr[mxN];
void solve() {
   unordered_map<int,int> mymap;
   int n;
   cin >> n;
   for(int i = 0; i < n; i++){
       cin >> arr[i];
   }
   int mx = 0;
   int count = 0;
   int j = 0;
   for(int i = 0; i < n; i++){
       if(mymap.count(arr[i])){
           mx = max(mx,count);
           while (j < n && mymap.count(arr[i]) && mymap[arr[i]] > 0){
               mymap[arr[j]] -= 1;
               j++;
               count--;
           }
           mymap[arr[i]] = 1;
           count++;
           mx = max(count,mx);
       }
       else{
           mymap[arr[i]] = 1;
           count++;
           mx = max(count,mx);
       }
   }
   cout << mx << endl;
}
 
int main() {
    rlimit cpu_time{.rlim_cur = 1, .rlim_max = 5}; 
    setrlimit(RLIMIT_CPU, &cpu_time);
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    
    solve();
}