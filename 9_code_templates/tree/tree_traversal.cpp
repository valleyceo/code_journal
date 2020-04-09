int L[100]={0};
int R[100]={0};

void DLR(int m)
{
	cout << m << " ";
	if (L[m]!=0) DLR(L[m]);
	if (R[m]!=0) DLR(R[m]);
}

void LDR(int m)
{
	if (L[m]!=0) LDR(L[m]);
	cout << m << " ";
	if (R[m]!=0) LDR(R[m]);
}

void LRD(int m)
{
	if (L[m]!=0) LRD(L[m]);
	if (R[m]!=0) LRD(R[m]);
	cout << m << " ";
}

int main(void)
{
	cin >> n;
	for (int i=1;i<=n;i++)
		cin >> L[i] >> R[i];
	
	DLR(1); cout << endl;
	LDR(1); cout << endl;
	LRD(1); cout << endl;
	
	return 0;
}