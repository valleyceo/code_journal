// Min Stack

/*
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
*/

// my solution
class MinStack {
public:
    stack<int> st;
    stack<int> new_stack;
        
    /** initialize your data structure here. */
    MinStack() {
        stack<int> empty;
        swap(st, empty);
    }
    
    void push(int x) {
        st.push(x);
    }
    
    void pop() {
        st.pop();
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        int min = INT_MAX;
        new_stack = st;
        while(!new_stack.empty()) {
            if (new_stack.top() < min) {
                min = new_stack.top();
            }
            new_stack.pop();
        }
        return min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */