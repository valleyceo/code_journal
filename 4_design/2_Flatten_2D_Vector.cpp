// Flatten 2D Vector

/*
Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

Follow up:
As an added challenge, try to code it using only iterators in C++ or iterators in Java.
*/

// my solution
class Vector2D {
public:
    Vector2D(vector<vector<int>>& vec2d) {
        x = vec2d.begin();
        xend = vec2d.end();
        if (x != xend) {
            y = x->begin();
        }
    }

    int next() {
        return *y++;
    }

    bool hasNext() {
        while (x != xend && y == x->end()) {
            ++x;
            y = x->begin();
        }
        return x != xend;
    }
private:
    vector<vector<int>>::iterator x, xend;
    vector<int>::iterator y;
};

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D i(vec2d);
 * while (i.hasNext()) cout << i.next();
 */