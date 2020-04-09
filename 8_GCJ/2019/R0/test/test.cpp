// g++ sample.cpp -std=c++14 -pthread -O3 -o sample.out

#include <iostream>
#include <string>

int main() {
  int num_test_cases;
  std::cin >> num_test_cases;
  for (int i = 0; i < num_test_cases; ++i) {
    int lo, hi;
    std::cin >> lo >> hi;
    int num_tries;
    std::cin >> num_tries;
    int head = lo + 1, tail = hi;
    while (true) {
      int m = (head + tail) / 2;
      std::cout << m << std::endl;
      std::string s;
      std::cin >> s;
      if (s == "CORRECT") break;
      if (s == "TOO_SMALL")
        head = m + 1;
      else
        tail = m - 1;
    }
  }
  return 0;
}
