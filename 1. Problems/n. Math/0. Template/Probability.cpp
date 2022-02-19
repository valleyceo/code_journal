// Probability

/*
Description
*/

// code
int permutation(int n, int k) {
    long res = 1;
    
    if (k > n - k)
        k = n - k;
    
    for (int i = 0; i < k; ++i) {
        res *= (n - i);
    }
    
    return (int)res;
}

int combination(int n, int k) {
    long res = 1;
    
    if (k > n - k)
        k = n - k;
    
    for (int i = 0; i < k; ++i) {
        res *= (n - i);
        res /= (i + 1);
    }
    
    return (int)res;
}