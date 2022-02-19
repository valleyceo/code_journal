// Rectangle Area

/*
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: -3, 0, 3, 4, 0, -1, 9, 2
Output: 45
Note:
Assume that the total area is never beyond the maximum possible value of int.
*/

// my solution
class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int x1 = max(A, E);
        int y1 = max(B, F);
        int x2 = min(C, G);
        int y2 = min(D, H);
        int tot_area = abs(A-C) * abs(B-D) + abs(E-G) * abs(F-H);
        
        if (x1 < x2 && y1 < y2)
            return tot_area-abs(x2 - x1) * abs(y1 - y2);
        else
            return tot_area;
    }
};