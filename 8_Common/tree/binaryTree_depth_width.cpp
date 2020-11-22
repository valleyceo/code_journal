#include <iostream>
#include <queue>
#include <stack>

using namespace std;

int l[100]={0};
int r[100]={0};
stack<int> mystack;
int n=0;
int w=0;
int d=0;

int depth(int n)
{
	if (l[n]==0 && r[n]==0)
	return 1;
	int depthl=depth(l[n]);
	int depthr=depth(r[n]);
	int dep=depthl>depthr ? depthl:depthr;
	return dep+1;
}

void width(int n)
{
	if (n<=d)
	{
		int t=0,x;
		stack<int> tmpstack;

		while (!mystack.empty())
		{
			x=mystack.top();
			mystack.pop();
			if (x!=0)
			{
				t++;
				tmpstack.push(l[x]);
				tmpstack.push(r[x]);
			}
		}

		w=w>t?w:t;
		mystack=tmpstack;
		width(n+1);
	}
}

int main(void)
{
	cin >> n;
	
	for (int i=1;i<=n;i++)
		cin >> l[i] >> r[i];
	
	d=depth(1);
	mystack.push(1);
	width(1);
	cout << w << " " << d << endl;
	
	return 0;
}