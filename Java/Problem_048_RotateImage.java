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

class Solution {
    // Approach 1: Transpose + Reverse
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        
        // Step 1: Transpose the matrix
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        
        // Step 2: Reverse each row
        for (int i = 0; i < n; i++) {
            reverseRow(matrix[i]);
        }
    }
    
    private void reverseRow(int[] row) {
        int left = 0, right = row.length - 1;
        while (left < right) {
            int temp = row[left];
            row[left] = row[right];
            row[right] = temp;
            left++;
            right--;
        }
    }
    
    // Approach 2: Layer by layer rotation
    public void rotateLayered(int[][] matrix) {
        int n = matrix.length;
        
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
    public void rotateCorners(int[][] matrix) {
        int n = matrix.length;
        
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
    
    // Helper methods
    private static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            System.out.print("[");
            for (int i = 0; i < row.length; i++) {
                System.out.print(row[i]);
                if (i < row.length - 1) {
                    System.out.print(", ");
                }
            }
            System.out.println("]");
        }
        System.out.println();
    }
    
    private static int[][] copyMatrix(int[][] matrix) {
        int n = matrix.length;
        int[][] copy = new int[n][n];
        for (int i = 0; i < n; i++) {
            copy[i] = matrix[i].clone();
        }
        return copy;
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test case 1: 3x3 matrix
        int[][] matrix1 = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        System.out.println("Input:");
        printMatrix(matrix1);
        solution.rotate(matrix1);
        System.out.println("Output after 90° rotation:");
        printMatrix(matrix1);
        System.out.println("Expected: [[7,4,1],[8,5,2],[9,6,3]]\n");
        
        // Test case 2: 4x4 matrix
        int[][] matrix2 = {
            {5, 1, 9, 11},
            {2, 4, 8, 10},
            {13, 3, 6, 7},
            {15, 14, 12, 16}
        };
        System.out.println("Input:");
        printMatrix(matrix2);
        solution.rotate(matrix2);
        System.out.println("Output after 90° rotation:");
        printMatrix(matrix2);
        System.out.println("Expected: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]\n");
        
        // Test case 3: 1x1 matrix
        int[][] matrix3 = {{1}};
        System.out.println("Input: [[1]]");
        solution.rotate(matrix3);
        System.out.println("Output: [[" + matrix3[0][0] + "]]");
        System.out.println("Expected: [[1]]\n");
        
        // Test case 4: 2x2 matrix
        int[][] matrix4 = {
            {1, 2},
            {3, 4}
        };
        System.out.println("Input:");
        printMatrix(matrix4);
        solution.rotate(matrix4);
        System.out.println("Output:");
        printMatrix(matrix4);
        System.out.println("Expected: [[3,1],[4,2]]\n");
        
        // Compare approaches
        System.out.println("Compare different approaches:");
        int[][] matrix5 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        
        int[][] m1 = copyMatrix(matrix5);
        solution.rotate(m1);
        System.out.print("Transpose+Reverse: ");
        for (int[] row : m1) {
            System.out.print(java.util.Arrays.toString(row));
        }
        System.out.println();
        
        int[][] m2 = copyMatrix(matrix5);
        solution.rotateLayered(m2);
        System.out.print("Layered: ");
        for (int[] row : m2) {
            System.out.print(java.util.Arrays.toString(row));
        }
        System.out.println();
        
        int[][] m3 = copyMatrix(matrix5);
        solution.rotateCorners(m3);
        System.out.print("Corners: ");
        for (int[] row : m3) {
            System.out.print(java.util.Arrays.toString(row));
        }
        System.out.println();
    }
}