// Count Primes

/*
Description:

Count the number of prime numbers less than a non-negative number, n.
*/

// my solution
class Solution {
public:
    
    bool is_prime(int n) {
        if (n == 2) {
            return true;
        }
        
        if (n % 2 == 0){
            return false;
        }
        
        for (int i = 3; i <= sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
    
    int countPrimes(int n) {
        int c = 0;
        for (int i = 2; i < n; i++) {
            if (is_prime(i)) {
                c += 1;
            }
        }
        
        return c;
    }
};