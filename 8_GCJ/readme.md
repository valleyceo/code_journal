# Google Code Jam Notes

## Useful links  
- https://groups.google.com/forum/#!forum/google-code
- https://github.com/indy256/codejam-templates


## How to compile and process input/output (C++)
```bash
g++ -o test test.cpp
./test < test_in.txt > test_out.txt

# my method (creates #_0in.txt and returns #_0out.txt)
./run.sh #_myfunc.cpp
```

### Compiling + interactive method
```bash
g++ sol.cpp -std=c++14 -pthread -O3 -o sol.o
python testing_tool.py 0 sol.o

# my method (2 - tester case)
./runpy.sh myfunc.cpp x y # x:test case num, y:compile cpp flag 0 or 1(optional)
```

### Sample Interaction
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

### Interactive tips
Interactive runner links stdin and stdout, but leaves stderr. Use it for debugging