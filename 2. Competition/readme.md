# Competitive Programming

## 1. Google Competition

#### Useful links

Google Code Jam Official Discussion groups [Here](https://groups.google.com/forum/#!forum/google-code)


#### How to compile and run in C++
```bash
# Regular problem
g++ -o test test.cpp
./test < test_in.txt > test_out.txt

# Interactive problem
g++ sol.cpp -std=c++14 -pthread -O3 -o sol.o
python testing_tool.py 0 sol.o
```

#### How to compile and run using Autoscript
```bash
# Ex: C++
./jam.sh filename.cpp

# Ex: python
./jam.sh filename.py
```

#### Sample Interaction
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

#### Interactive problem tips

Interactive runner links stdin and stdout, but leaves stderr. Use it for debugging
