// Trouble Sort

/*
Problem link:
https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cb
*/

// my solution
#include <iostream>
#include <algorithm>    // std::sort
#include <vector>

int main()
{
    int T, n;
    T = 1;
    
    std::cin >> n;

    while (T <= n)
    {
        int L; // Arr length
        long int n_in; // input
        
        std::cin >> L;
        int a2_len = L/2;
        int a1_len = L - a2_len;
        int idx1 = 0, idx2 = 0;
        std::vector<long int> arr1(a1_len, 0), arr2(a2_len, 0); // 2 arrays

        for (int i = 0; i < L; i++) {
            std::cin >> n_in;
            if (i % 2 == 0)
                arr1[idx1++] = n_in;
            else
                arr2[idx2++] = n_in;
        }
        
        sort(arr1.begin(), arr1.end());
        sort(arr2.begin(), arr2.end());
        
        idx1 = 0;
        idx2 = 0;
        int idx_check;
        long int prev = -1;

        for (idx_check = 0; idx_check < L; idx_check++) {
            if (idx_check % 2 == 0) {
                if (arr1[idx1] < prev)
                    break;

                prev = arr1[idx1++];
            } else {
                if (arr2[idx2] < prev)
                    break;

                prev = arr2[idx2++];
            }
        }

        if (idx_check == L) {
            std::cout << "Case #" << std::to_string(T) << ": " << "OK" << '\n';
        } else {
            std::cout << "Case #" << std::to_string(T) << ": " << idx_check - 1 << '\n';
        }
        
        T++;
    }
    
    return 0;
}