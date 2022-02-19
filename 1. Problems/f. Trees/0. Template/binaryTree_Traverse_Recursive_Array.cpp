int L[100]={0};
int R[100]={0};

void preOrder(int m)
{
	cout << m << " ";
	if (L[m]!=0) preOrder(L[m]);
	if (R[m]!=0) preOrder(R[m]);
}

void inOrder(int m)
{
	if (L[m]!=0) inOrder(L[m]);
	cout << m << " ";
	if (R[m]!=0) inOrder(R[m]);
}

void postOrder(int m)
{
	if (L[m]!=0) postOrder(L[m]);
	if (R[m]!=0) postOrder(R[m]);
	cout << m << " ";
}

int main(void)
{
	cin >> n;
	for (int i=1;i<=n;i++)
		cin >> L[i] >> R[i];
	
	preOrder(1); cout << endl;
	inOrder(1); cout << endl;
	postOrder(1); cout << endl;
	
	return 0;
}