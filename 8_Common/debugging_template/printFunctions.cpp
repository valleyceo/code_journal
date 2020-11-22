void PrintVec(vector< vector<cell> >& M) {
    cout << "Printing V" << endl;
    for (int i = 0; i < M.size(); ++i) {
        for (int j = 0; j < M[0].size(); ++j) {
            cout << M[i][j].val << " ";
        }
        cout << endl;
    }
}