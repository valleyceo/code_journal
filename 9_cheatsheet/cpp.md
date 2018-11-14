# C++ Cheatsheet
--
## Type conversion
```cpp
// char to int
int a = char - 'A'

// string to int
stoi(s) // to int
stof(s) // to float
stold(s) // to long double

// int to string
string s = to_string(int);
```

## Bits
```cpp
// flip bits between 0 and 1
x ^= 1;

// lowest bit
n = x & (x-1); // erase lowest bit (ex. 1100 -> 1000)
n = x & ~(x-1); // extract lowest set bit
```

## Array
```cpp
// create matrix
vector<vector<int>> matrix(ROW, vector<int>(COL));

// resize vector
matrix.resize(ROW);
matrix[i].resize(COL);

/* stacks */
stack<int> stck;
// insert
stck.push(num)
stck.emplace(string)

// accumulation - accumulate(begin, end, acc_var, [variables used in fcn](int ThisValAccumulates, char ThisIsInput) {return ReturnValueAccumulates});
string col = "ZZ";
int acc = accumulate(begin(col), end(col), 0, [](int result, char c) {
            return result * 26 + c - 'A' + 1;});
```

## Enum
```cpp
// enumerating graph
struct GraphVertex {
    enum Color { kWhite, kGray, kBlack } color = kWhite;
    vector<GraphVertex*> edges;
};

```

## Queue
```cpp
// assigning 2d queue
queue<pair<int, int>> q;
queue<pair<int, int>> q(deque<pair<int, int>>(1, {i, j})); // another way of direct inititialization
cont auto [x, y] = q.front();
q.pop() // take out the front queue
q.emplace(x, y); // add new queue
```

## String
```cpp
// string checkers
isalnum(int c);
isalpha(int c);
isdigit(int c);
```

## String manipulation
```cpp
reverse(s.begin(), s.end());
sort(s.begin(), s.end());

// split string into half
string cmd = "HELLO WORLD";
string arg;
string::size_type pos = cmd.find(' ');
if(cmd.npos != pos) {
    arg = cmd.substr(pos + 1);
    cmd = cmd.substr(0, pos);
}
//=> cmd:"HELLO", arg:"WORLD"

// search
size_t found = str.find_first_not_of("abcdefghijklmnopqrstuvwxyz ")
if (found!=std::string::npos)
	cout << "The first non-alphabetic character is " << str[found] << endl;
```

## Linked List
```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };

// create node
ListNode *odds = new ListNode(0);

// STL library
// - list (doubly-linked list): emplace_front, pop_front, push_back, push_front, emplace_back, pop_back
// - forward_list (c++11 singly-linked list): pop_front, insert_after, emplace_after, erase_after
```

## Queue
```cpp
// reverse priority queue
priority_queue<int, vector<int>, greater<int> > pq; // takes <type, datatype, comparison>

```

## Hashing
```cpp
/*** unordered map ***/

```cpp
// add n delete
umap[num1] = num2
umap.erase(num);
// search
if(umap.find(numx) == umap.end()){...};
if(auto it = umap.find(c); it != cend(umap)){...}; // alternate
// look up
val = umap.at(numx)

// iterate and find
for (auto a : umap){
    if (a.second == count)...;
}
```

## Function calls
```cpp
// using pointer and address
vector<int> A;
function(&A);
void function(vector<int> *A_ptr) {
    vector<int> &A = *A_ptr; // creates copy
}
```

## Class/Struct
```cpp
// colon initialization (works like regular init with type removed)
TicTacToe(int n): b_size(n), rows(n, 0), cols(n, 0), diag1(0), diag2(0) {}

```

```cpp
// linked list node
template <typename T>
struct ListNode {
    T data;
    shared_ptr<ListNode<T>> next;
}

// init
ListNode<int> new_node;
// create node pointer
auto dummy_head = make_shared<ListNode<int>>(ListNode<int>{0, L});
```

## Heaps
```cpp
// max heap
priority_queue<int> max_heap// default less
priority_queue<int, vector<int>, less<>> max_heap;

// min heap
priority_queue<int, vector<int>, greater<>> min_heap;

// custom heap
priority_queue<string, vector<string>, function<bool(string, string)>>
            min_heap([](const string& a, const string& b) { return size(a) >= size(b); })

```

## Regular Expression
```cpp
#include <regex>
string s = "subject";
regex e = "(sub)(.*)";
if (regex_match(s, e))
    cout << "string matched\n";
```

## Random
```cpp
static uniform_int_distribution<int> choice(0, chart.size() - 1);
(f){
    // create new hash function
    auto gen_hash = [&, this] () {
        for (int i = 0; i < hash_len; ++i)
            new_url[i] = chart[choice(rand_eng)];
    };
    gen_hash();
}
default_random_engine rand_eng;
```

## Algorithm
```cpp
// binary search on array
#include <algorithm>
if(binary_search(arr, arr + size, val)) {tries++; return false;}

```

## Functions
<details>
<summary> Lambda function</summary>

---
- using capture-clause []:
    [=] capture all variables within scope by value  
    [&] capture all variables within scope by reference  
    [&var] capture var by reference  
    [&, var] specify that the default way of capturing is by reference and we want to capture var  
    [=, &var] capture the variables in scope by value by default, but capture var using reference instead  

---

```cpp
// example
any_of(begin(A), end(A), [&](int a) {return HasTwoSum(A, t-a); });
```
</details>

## Templates

<details>
<summary> Substring Problem </summary>

```cpp
int findSubstring(string s){
        vector<int> map(128,0);
        int counter; // check whether the substring is valid
        int begin=0, end=0; //two pointers, one point to tail and one  head
        int d; //the length of substring

        for() { /* initialize the hash map here */ }

        while(end<s.size()){

            if(map[s[end++]]-- ?){  /* modify counter here */ }

            while(/* counter condition */){

                 /* update d here if finding minimum*/

                //increase begin to make it invalid/valid again

                if(map[s[begin++]]++ ?){ /*modify counter here*/ }
            }

            /* update d here if finding maximum*/
        }
        return d;
  }

// Source: https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
```
</details>
