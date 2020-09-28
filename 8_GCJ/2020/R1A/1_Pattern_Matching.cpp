// Bit Party

/*
Link:
https://codejam.withgoogle.com/2018/challenges/0000000000007883/dashboard/000000000002fff6

- R robot shoppers
- Each buys B "bits" of items
- C cashiers where I-th cashier:
	* Accept max Mi items per customer
	* Take Si seconds to scan each item
	* Spend Pi seconds handling payment
- Interaction time = Si x B + Pi

Q: Try to purchase all as quickly as possible

Input:
1. Test cases T
2. Each begins with three int. R, B, C
3. C lines of ith cashier - each has three int of Mi, Si, Pi

*/

// my solution
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int T, n;
    T = 1;
    
    std::cin >> n;

    while (T <= n)
    {
        int N;
        cin >> N;
        
        vector<string> Words;

        while (N--) {
            string s;
            cin >> s;
            Words.push_back(s);
        }

        string res_front = "", res_back = "", res_mid = "";
        string res;
        
        for (auto word : Words) {

            string temp_res_back = res_back;
            string temp_word = word;
            string temp_word_btw = word;
            string temp_res_front = res_front;

            // front
            while (temp_res_front.length() > 0 && temp_word.front() != '*' && 
                   temp_res_front.front() == temp_word.front()) {
                temp_res_front.erase(0, 1);
                temp_word.erase(0, 1);
                //cout << temp_res_front << " " << temp_word << endl;
            }

            if (temp_word.front() != '*' &&
                temp_res_front.length() > 0 && temp_word.length() > 0 && 
                temp_res_front.front() != temp_word.front())
            {
                res = "*";
                break;
            }

            if (temp_res_front.length() == 0) {
                while (temp_word.front() != '*') {
                    res_front = res_front + temp_word.front();
                    temp_word.erase(0, 1);
                }
            }

            // back
            while (temp_res_back.length() > 0 && temp_word.back() != '*' && 
                   temp_res_back.back() == temp_word.back()) {
                temp_res_back.pop_back();
                temp_word.pop_back();
            }

            if (temp_word.back() != '*' &&
                temp_res_back.length() > 0 && temp_word.length() > 0 && 
                temp_res_back.back() != temp_word.back())
            {
                res = "*";
                break;
            }

            if (temp_res_back.length() == 0) {
                while (temp_word.back() != '*') {
                    res_back = temp_word.back() + res_back;
                    temp_word.pop_back();
                }
            }

            // between
            if (temp_word.length() > 2) {
                temp_word.erase(0, 1);
                temp_word.pop_back();

                temp_word.erase(remove(temp_word.begin(), temp_word.end(), '*'), temp_word.end());
                res_mid = res_mid + temp_word;
            }

            res = res_front + res_mid + res_back;
            //cout << res_front << " - " << res_back << endl;
        }

        cout << "Case #" << to_string(T++) << ": " << res << '\n';
    }
    
    return 0;
}

/* Note:
- * Pattern
- Consist only uppercase english letters and *
- name is a string consisting only english letter (Upper case)
- Find string given the list of patterns
*/