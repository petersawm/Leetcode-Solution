class SparseVector:
    def __init__(self, nums: List[int]):
        self.vt = {k:v for k, v in enumerate(nums) if v}
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        com = set(i for i in self.vt).intersection(j for j in vec.vt)
        return sum(self.vt[c]*vec.vt[c] for c in com)
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)