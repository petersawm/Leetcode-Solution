/*
Problem: 48 - Rotate Image
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-image/

Problem Statement:
Rotate an n x n 2D matrix by 90 degrees (clockwise) in-place.

Approach:
1. Transpose + Reverse - Most intuitive
2. Layer by layer rotation

Time Complexity: O(N²) - Visit each element once
Space Complexity: O(1) - In-place rotation
*/

#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    // Approach 1: Transpose + Reverse
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        
        // Step 1: Transpose the matrix
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        
        // Step 2: Reverse each row
        for (int i = 0; i < n; i++) {
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
    
    // Approach 2: Layer by layer rotation
    void rotateLayered(vector<vector<int>>& matrix) {
        int n = matrix.size();
        
        // Process each layer
        for (int layer = 0; layer < n / 2; layer++) {
            int first = layer;
            int last = n - 1 - layer;
            
            for (int i = first; i < last; i++) {
                int offset = i - first;
                
                // Save top element
                int top = matrix[first][i];
                
                // Left -> Top
                matrix[first][i] = matrix[last - offset][first];
                
                // Bottom -> Left
                matrix[last - offset][first] = matrix[last][last - offset];
                
                // Right -> Bottom
                matrix[last][last - offset] = matrix[i][last];
                
                // Top -> Right
                matrix[i][last] = top;
            }
        }
    }
    
    // Approach 3: Rotate 4 corners
    void rotateCorners(vector<vector<int>>& matrix) {
        int n = matrix.size();
        
        for (int i = 0; i < (n + 1) / 2; i++) {
            for (int j = 0; j < n / 2; j++) {
                // Save temp
                int temp = matrix[n - 1 - j][i];
                
                // Move values
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j];
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i];
                matrix[j][n - 1 - i] = matrix[i][j];
                matrix[i][j] = temp;
            }
        }
    }
};

// Helper functions
void printMatrix(const vector<vector<int>>& matrix) {
    for (const auto& row : matrix) {
        cout << "[";
        for (int i = 0; i < row.size(); i++) {
            cout << row[i];
            if (i < row.size() - 1) {
                cout << ", ";
            }
        }
        cout << "]" << endl;
    }
    cout << endl;
}

vector<vector<int>> copyMatrix(const vector<vector<int>>& matrix) {
    return matrix;
}

int main() {
    Solution solution;
    
    // Test case 1: 3x3 matrix
    vector<vector<int>> matrix1 = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    cout << "Input:" << endl;
    printMatrix(matrix1);
    solution.rotate(matrix1);
    cout << "Output after 90° rotation:" << endl;
    printMatrix(matrix1);
    cout << "Expected: [[7,4,1],[8,5,2],[9,6,3]]" << endl << endl;
    
    // Test case 2: 4x4 matrix
    vector<vector<int>> matrix2 = {
        {5, 1, 9, 11},
        {2, 4, 8, 10},
        {13, 3, 6, 7},
        {15, 14, 12, 16}
    };
    cout << "Input:" << endl;
    printMatrix(matrix2);
    solution.rotate(matrix2);
    cout << "Output after 90° rotation:" << endl;
    printMatrix(matrix2);
    cout << "Expected: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]" << endl << endl;
    
    // Test case 3: 1x1 matrix
    vector<vector<int>> matrix3 = {{1}};
    cout << "Input: [[1]]" << endl;
    solution.rotate(matrix3);
    cout << "Output: [[" << matrix3[0][0] << "]]" << endl;
    cout << "Expected: [[1]]" << endl << endl;
    
    // Test case 4: 2x2 matrix
    vector<vector<int>> matrix4 = {
        {1, 2},
        {3, 4}
    };
    cout << "Input:" << endl;
    printMatrix(matrix4);
    solution.rotate(matrix4);
    cout << "Output:" << endl;
    printMatrix(matrix4);
    cout << "Expected: [[3,1],[4,2]]" << endl << endl;
    
    // Compare approaches
    cout << "Compare different approaches:" << endl;
    vector<vector<int>> matrix5 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    
    auto m1 = copyMatrix(matrix5);
    solution.rotate(m1);
    cout << "Transpose+Reverse: ";
    for (const auto& row : m1) {
        cout << "[";
        for (int val : row) cout << val << " ";
        cout << "]";
    }
    cout << endl;
    
    auto m2 = copyMatrix(matrix5);
    solution.rotateLayered(m2);
    cout << "Layered: ";
    for (const auto& row : m2) {
        cout << "[";
        for (int val : row) cout << val << " ";
        cout << "]";
    }
    cout << endl;
    
    auto m3 = copyMatrix(matrix5);
    solution.rotateCorners(m3);
    cout << "Corners: ";
    for (const auto& row : m3) {
        cout << "[";
        for (int val : row) cout << val << " ";
        cout << "]";
    }
    cout << endl;
    
    return 0;
}