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
#define MAXN 3500
#define MAXM 13000
#define MOD 1000000000
using namespace std;
#define LL long long
#define ULL unsigned long long
#define LD long double

int T;
int n, m;

int W[MAXN], D[MAXN];
int dp[MAXM];

int main() {
	while (scanf("%d%d", &n, &m) != EOF && n != 0 && m != 0) {
		for (int i = 1; i <= n; i++)
		{
			scanf("%d%d", &W[i], &D[i]);
		}
		memset(dp, 0, sizeof dp);
		for (int i = 1; i <= n; i++)
		{
			for (int j = m; j >= 0; j--)
			{
				if (j - W[i] < 0) {
					dp[j] = dp[j];
				}
				else {
					dp[j] = max(dp[j], dp[j - W[i]] + D[i]);
				}
			}
		}
		printf("%d\n", dp[m]);
	}
#ifdef __ACM
	// system("pause");
#endif
}