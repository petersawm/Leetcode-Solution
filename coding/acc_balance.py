from collections import defaultdict

class Solution:
    def minTransfers(self, transactions):
        bal = defaultdict(int)
        for frm, to, amt in transactions:
            bal[frm] -= amt
            bal[to] += amt

        balances = [v for v in bal.values() if v != 0]
        n = len(balances)
        if n == 0:
            return 0
        
        # DFS + backtracking
        def dfs(cur):
            # skip 0 pos
            while cur < n and balances[cur] == 0:
                cur += 1
            if cur == n:
                return 0
            
            res = float("inf")
            vis = set() # only travel once for same amount in same level
            for i in range(cur + 1, n):
                if balances[cur] * balances[i] < 0 and balances[i] not in vis:
                    vis.add(balances[i])

                    # match i and cur
                    # similar to put cur to i
                    balances[i] += balances[cur]

                    res = min(res, 1 + dfs(cur + 1))

                    # backtracking
                    balances[i] -= balances[cur]
            
            return 0 if res == float("inf") else res
        
        return dfs(0)
    
# Test
if __name__ == "__main__":
    sol = Solution()

    print("Test 1: empty")
    print(sol.minTransfers([]), "== 0")

    print("\nTest 2: self cancel")
    tx = [[0, 1, 10], [1, 2, 10], [2, 0, 10]]
    print(sol.minTransfers(tx), "== 0")

    print("\nTest 3: single")
    print(sol.minTransfers([[0, 1, 5]]), "== 1")

    print("\nTest 4: two independent pairs")
    tx = [[0, 1, 5], [2, 3, 5]]
    print(sol.minTransfers(tx), "== 2")

    print("\nTest 5: chain debt")
    tx = [[0, 1, 10], [1, 2, 5]]
    print(sol.minTransfers(tx), "== 2")

    print("\nTest 6: middle zero")
    tx = [[0, 1, 5], [1, 2, 5]]
    print(sol.minTransfers(tx), "== 1")

    print("\nTest 7: mixed small")
    tx = [[0, 1, 7], [2, 3, 4], [1, 2, 3], [3, 0, 2]]
    print(sol.minTransfers(tx), "== 3")