"""
Problem: 48 - Rotate Image
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-image/

Problem Statement:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees 
(clockwise). You have to rotate the image in-place, which means you have to modify the 
input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Approach:
Multiple approaches:

1. Transpose + Reverse (Most intuitive)
   - First transpose the matrix (swap matrix[i][j] with matrix[j][i])
   - Then reverse each row
   - Time: O(N²), Space: O(1)

2. Rotate in layers/rings
   - Process matrix layer by layer from outside to inside
   - Rotate 4 elements at a time
   - Time: O(N²), Space: O(1)

Time Complexity: O(N²) - Visit each element once
Space Complexity: O(1) - In-place rotation
"""

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Transpose + Reverse approach - Most intuitive
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()
    
    # Layer by layer rotation
    def rotateLayered(self, matrix: List[List[int]]) -> None:
        """Rotate layer by layer"""
        n = len(matrix)
        
        # Process each layer
        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer
            
            for i in range(first, last):
                offset = i - first
                
                # Save top element
                top = matrix[first][i]
                
                # Left -> Top
                matrix[first][i] = matrix[last - offset][first]
                
                # Bottom -> Left
                matrix[last - offset][first] = matrix[last][last - offset]
                
                # Right -> Bottom
                matrix[last][last - offset] = matrix[i][last]
                
                # Top -> Right
                matrix[i][last] = top
    
    # Rotate 4 corners at a time
    def rotateCorners(self, matrix: List[List[int]]) -> None:
        """Rotate 4 corners simultaneously"""
        n = len(matrix)
        
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                # Save temp
                temp = matrix[n - 1 - j][i]
                
                # Move values in counter-clockwise direction
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = temp
    
    # Using zip (Pythonic but creates new lists)
    def rotatePythonic(self, matrix: List[List[int]]) -> None:
        """Pythonic way using zip"""
        # Transpose using zip
        matrix[:] = [list(row) for row in zip(*matrix)]
        # Reverse each row
        for row in matrix:
            row.reverse()


# Helper functions
def print_matrix(matrix: List[List[int]]) -> None:
    """Pretty print matrix"""
    for row in matrix:
        print(row)
    print()

def copy_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """Deep copy matrix"""
    return [row[:] for row in matrix]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: 3x3 matrix
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Input:")
    print_matrix(matrix1)
    solution.rotate(matrix1)
    print("Output after 90° rotation:")
    print_matrix(matrix1)
    print("Expected:")
    print("[[7, 4, 1], [8, 5, 2], [9, 6, 3]]\n")
    
    # Test case 2: 4x4 matrix
    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    print("Input:")
    print_matrix(matrix2)
    solution.rotate(matrix2)
    print("Output after 90° rotation:")
    print_matrix(matrix2)
    print("Expected:")
    print("[[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]\n")
    
    # Test case 3: 1x1 matrix
    matrix3 = [[1]]
    print("Input: [[1]]")
    solution.rotate(matrix3)
    print(f"Output: {matrix3}")
    print("Expected: [[1]]\n")
    
    # Test case 4: 2x2 matrix
    matrix4 = [
        [1, 2],
        [3, 4]
    ]
    print("Input:")
    print_matrix(matrix4)
    solution.rotate(matrix4)
    print("Output:")
    print_matrix(matrix4)
    print("Expected:")
    print("[[3, 1], [4, 2]]\n")
    
    # Compare approaches
    print("Compare different approaches:")
    matrix5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    m1 = copy_matrix(matrix5)
    solution.rotate(m1)
    print(f"Transpose+Reverse: {m1}")
    
    m2 = copy_matrix(matrix5)
    solution.rotateLayered(m2)
    print(f"Layered: {m2}")
    
    m3 = copy_matrix(matrix5)
    solution.rotateCorners(m3)
    print(f"Corners: {m3}")
