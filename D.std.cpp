#include <iostream> 
#include <fstream>
#include <vector>
#include <queue>
#include <cstring>
#include <string>
#include <algorithm>
#include <stack>
#include <functional>
#include "stdlib.h" 
#include "time.h"
#include <set>
#include <map>
#include <numeric>
#include <cctype>
#include <cmath>

#define INF 9999999
#define MOD 10000007
const double eps = 1e-4;
using namespace std;
#define LL long long
#define ULL unsigned long long
#define LD long double


int main() {
double n;
while (scanf("%lf", &n) == 1) {
    while (n>18) n /= 18;
    if (n <= 9) puts("yes");
    else puts("no");
}
#ifdef __ACM
#endif
}