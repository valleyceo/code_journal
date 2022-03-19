// Max Points on a Line

/*
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6

*/

// my solution
/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */

/* 
y = ax + b
*/
#define EPS 1e-15

class Solution {
public:
    int maxPoints(vector<Point>& points) {
        if (points.size() < 3) {
            return points.size();
        }
        
        int maxp = 0;
        int temp = 0;
        long double slope, yint;
        
        for (int i = 0; i < points.size()/2 + 1; i++) {
            for (int j = i + 1; j < points.size(); j++) {
                if (abs(points[i].x - points[j].x) < EPS) {
                    slope = INT_MAX;
                    yint = points[i].x;
                } else {
                    slope = (long double)(points[i].y - points[j].y) / (points[i].x - points[j].x);
                    yint = points[i].y - slope * (long double)points[i].x;
                }
                
                temp = 2;
                
                for (int k = 0; k < points.size(); k++) {
                    if (k == i || k == j) continue;
                    
                    if (slope == INT_MAX) {
                        if (points[k].x == yint) {
                            temp += 1;
                            if (temp > maxp) maxp = temp;
                        }
                    } else if (abs(points[k].y - (slope * points[k].x + yint)) < EPS) {
                        temp += 1;
                    }
                }
                
                if (temp > maxp) {
                    maxp = temp;
                }
            }
        }
        return maxp;
    }
};