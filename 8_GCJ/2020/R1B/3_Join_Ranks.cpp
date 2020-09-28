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
#include <stack>

using namespace std;

// This function return the sorted stack 
stack<int> sortStack(stack<int> &input) 
{ 
    stack<int> tmpStack; 
  
    while (!input.empty()) 
    { 
        // pop out the first element 
        int tmp = input.top(); 
        input.pop(); 
  
        // while temporary stack is not empty and top 
        // of stack is greater than temp 
        while (!tmpStack.empty() && tmpStack.top() < tmp) 
        { 
            // pop from temporary stack and push 
            // it to the input stack 
            input.push(tmpStack.top()); 
            tmpStack.pop(); 
        } 
  
        // push temp in tempory of stack 
        tmpStack.push(tmp); 
    } 
  
    return tmpStack; 
} 

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
        stack<int> s;

        for (int i = 1; i <= S; ++i) {
            for (int j = 1; j <= R; ++j) {
                s.push_back(j);
            }
        }

        
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