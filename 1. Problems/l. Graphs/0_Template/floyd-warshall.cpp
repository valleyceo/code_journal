// map[i][j]=infinity at start
void floyd()
{
	for (int k=1; k<=n; k++)
		for (int i=1; i<=n; i++)
			for (int j=1; j<=n; j++)
				if (i!=j && j!=k && i!=k)
					if (map[i][k]+map[k][j]<map[i][j])
						map[i][j]=map[i][k]+map[k][j];
}