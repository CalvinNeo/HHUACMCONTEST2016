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

#define INF 0x3f3f3f3f
#define MOD 10000007
using namespace std;
#define LL long long
#define ULL unsigned long long
#define LD long double

int T;
int n, m;

LL slowpow(LL m, LL n, LL k)
{
	LL ans = 1ll;
	for (LL i = 0; i < n; i++)
	{
		ans *= m;
		ans %= k;
	}
	return ans;
}

int main() {
	while (scanf("%d", &n) != EOF) {
		LL ans = slowpow(3ll, n, MOD) - 1;
		printf("%lld\n", ans);
	}
#ifdef __ACM
	system("pause");
#endif
}