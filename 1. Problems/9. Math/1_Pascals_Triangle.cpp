// Pascal's Triangle

/*
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
*/

// my solution
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        
        if (numRows == 0) {
            return ans;
        }
        
        vector<int> list(1, 1);
        vector<int> new_list;
        ans.push_back(list);
        
        while(--numRows){
            new_list = list;
            
            for (int i = 1; i < ans.size(); i++) {
                list[i] = new_list[i] + new_list[i-1];
            }
            
            list.push_back(1);
            ans.push_back(list);
        }
        
        return ans;
    }
};