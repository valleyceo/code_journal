// Join Ranks

/*
Question
- New deck of card (1-R rank, 1-S suit)
- Total cards of R x S (each card rep. (r,s))
- Card is sorted by ranks -> (1,1),(2,1),..(r,1),(1,2),(2,2)...(r,2), and so on...
- reorder deck to be sorted by rank (suit order does not matter)


*/
// my solution
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int T, n;
    T = 1;
    
    std::cin >> n;

    while (T <= n)
    {
        int R, S;
        std::cin >> R >> S;

        int count = 0;
        int inc = 0;
        vector<string> s;

        for (int j = R; j > 1; --j) {
            inc = 0;
            for (int i = S - 1; i > 0; --i) {
                s.push_back(to_string(inc + j * i) +  " " + to_string(j - 1));
                inc += j - 1;
                count++;
            }
        }

        cout << "Case #" << to_string(T++) << ": " << count << '\n';

        for (auto s1 : s) {
            cout << s1 << endl;
        }
    }
    
    return 0;
}