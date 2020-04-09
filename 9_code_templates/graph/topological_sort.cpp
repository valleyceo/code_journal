// Find any solution of topological sort.
#include<iostream>

using namespace std;

int f[100]={0}, ans[100]={0};
bool g[100][100]={0}, v[100]={0};
int n=0, m=0;

void dfs(int k)
{
	int i=0;
	v[k]=true;
	for (int i=1;i<=n;i++)
	if (g[k][i] && !v[i]) dfs(i);
	m++;
	ans[m]=k;
}

int main(void)
{
	cin >> n >> m;

	for (int i=1;i<=m;i++)
	{
		int x=0, y=0;
		cin >> x >> y;
		g[y][x]=true;
	}

	m=0;
	for (int i=1;i<=n;i++)
		if (!v[i]) dfs(i);

	for (int i=1;i<=n;i++) 
		cout << ans[i] << endl;

	return 0;
}


// Find the order of topological sort is dictionary minimum
int f[100]={0}, ans[100]={0};
bool g[100][100]={0}, v[100]={0};
int n=0, m=0;

int main(void)
{
	cin >> n >> m;
	
	for (int i=1;i<=m;i++)
	{
		int x=0, y=0;
		cin >> x >> y;
		g[x][y]=true;
		f[y]++;
	}

	for (int i=1;i<=n;i++)
	{
		for (int j=1;j<=n;j++)
		{
			if (f[j]==0 && !v[j]) break;
			
			if (f[j]!=0)
			{
				cout << "error" << endl;
				return 0;
			}
			
			ans[i]=j;
			v[j]=true;

			for (int k=1;k<=n;k++)
				if (g[j][k]) 
					f[k]--;
		}
	}

	for (int i=1;i<=n;i++) 
		cout << ans[i] << endl;
	
	return 0;
}