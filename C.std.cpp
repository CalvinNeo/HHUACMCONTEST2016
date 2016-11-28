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
const int MAXN = 205;

int n, m;

int px[MAXN], py[MAXN];
vector<int> online[1005];
double mp[MAXN][MAXN];
double dist[MAXN][MAXN];
int path[MAXN], pre[MAXN][MAXN];
double minc = INF;
int num;

bool point_on_segment(int x, int y, int x1, int y1, int x2, int y2) {
	int lx = min(x1, x2), ux = max(x1, x2);
	int ly = min(y1, y2), uy = max(y1, y2);
	if (x < lx || x > ux || y < ly || y > uy) {
		return false;
	}
	if ((y1 - y2) *  (x - x1) == (y - y1) * (x1 - x2)) {
		return true;
	}
	return false;
}

double floyd() {
	minc = INF;
	for (int k = 1; k <= n; k++)
	{
		for (int i = 1; i < k; i++)
			for (int j = i + 1; j < k; j++)
			{
				double ans = dist[i][j] + mp[i][k] + mp[k][j];
				if (ans < minc) 
				{
					minc = ans;
					num = 0;
					int p = j;
					while (p != i) 
					{
						path[num++] = p;
						p = pre[i][p];
					}
					path[num++] = i;
					path[num++] = k;
				}
			}
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= n; j++)
			{
				if (dist[i][j] > dist[i][k] + dist[k][j] )
				{
					dist[i][j] = dist[i][k] + dist[k][j];
					pre[i][j] = pre[k][j];
				}
			}
		}
	}
	double ans = 0;
	path[num] = path[0];
	for (int i = 0; i <= num - 1; i++) {
		//printf("link %d %d\n", path[i], path[i + 1]);
		ans += mp[path[i]][path[i + 1]];
	}
	//ans += mp[path[num - 1]][path[1]];
	return ans;
}

int sqrs(int x, int y) {
	return x * x + y * y;
}

bool point_cmp(const int & i, const int & j) {
	if (px[i] == px[j]) {
		return py[i] < py[j];
	}
	return px[i] < px[j];
}

int main() {
	while (scanf("%d%d", &n, &m) != EOF) {
		for (int i = 1; i <= m; i++)
		{
			online[i].clear();
		}
		memset(dist, 0, sizeof dist);
		memset(mp, 0, sizeof mp);
		memset(path, 0, sizeof path);
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++)
			{
				dist[i][j] = mp[i][j] = INF;
				pre[i][j] = i;
			}
		}
		for (int i = 1; i <= n; i++)
		{
			scanf("%d%d", &px[i], &py[i]);
		}
		for (int i = 1; i <= m; i++)
		{
			int u, v;
			scanf("%d%d", &u, &v);
			for (int j = 1; j <= n; j++)
			{
				if (point_on_segment(px[j], py[j], px[u], py[u], px[v], py[v])) {
					online[i].push_back(j);
				}
			}
		}
		for (int i = 1; i <= m; i++)
		{
			sort(online[i].begin(), online[i].end(), point_cmp);
		}
		for (int i = 1; i <= m; i++)
		{
			for (int j = 0; j < online[i].size() - 1; j++)
			{
				int pt1 = online[i][j], pt2 = online[i][j + 1];
				double cost = sqrt(sqrs(px[pt1] - px[pt2], py[pt1] - py[pt2]));
				//printf("%d %d %d \n", pt1, pt2, (int)cost);
				if (dist[pt1][pt2]>cost)
					dist[pt1][pt2] = dist[pt2][pt1] = mp[pt1][pt2] = mp[pt2][pt1] = cost;
			}
		}
		//for (int i = 1; i <= n; i++)
		//{
		//	for (int j = 1; j <= n; j++)
		//	{
		//		printf("%11.2f ", mp[i][j]);
		//	}
		//	puts("");
		//}
		double ans = floyd();
		if (minc > INF - 1) {
			puts("impossible");
		}
		else {
			printf("%.2f\n", ans);
		}
	}
#ifdef __ACM
	// system("pause");
#endif
}