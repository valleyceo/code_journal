# How to Solve Code Jam Problems

This is an archive of my code jam attempts. I created autoscripts for testing Code Jam competition problems (both regular and interactive). Feel free to use and learn if you are interested!

## Useful links

- Google Code Jam Official Discussion groups [Here](https://groups.google.com/forum/#!forum/google-code)

## How to compile and run
```bash
# Regular problem
g++ -o test test.cpp
./test < test_in.txt > test_out.txt

# Interactive problem
g++ sol.cpp -std=c++14 -pthread -O3 -o sol.o
python testing_tool.py 0 sol.o
```

## How to compile and run using Autoscript

```bash
# Ex: C++
./cj.sh filename.cpp

# Ex: python
./cj.sh filename.py
```

## How to Run Interactive Problems

### Using python autoscript
- Download interactive_runner and testing_tool files from Code Jam website

```bash
python3 interactive_runner.py python3 testing_tool.py 0 -- python3 problem.py
```

### How to Run using Autoscript

```bash
# Rename testing file to X_testing_tool.py
# X is the number of problem and 0 is the test case
./icj.sh X_Problem.py 0
```


### Sample Input/Output in Interactive Problem
```cpp
#include <iostream>

int main() {

  // send
  cout << 10 << endl;
  fflush(stdout);

  // read
  int n;
  cin >> n;

  // complete
  return 0;
}

```

### Debugging Tip
- Interactive runner links stdin and stdout, but leaves stderr. Use it for debugging
