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

LL quickpow(LL m, LL n, LL k)
{
	int b = 1ll;
	while (n > 0)
	{
		if (n & 1)
			b = (b*m) % k;
		n = n >> 1ll;
		m = (m*m) % k;
	}
	return b;
}

int main() {
	while (scanf("%d", &n) != EOF && n != 0) {
		LL ans = quickpow(3ll, n, MOD) - 1;
		printf("%lld\n", ans);
	}
#ifdef __ACM
	// system("pause");
#endif
}