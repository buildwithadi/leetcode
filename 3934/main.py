from collections import Counter

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        base = 100003
        mod = 10**9 + 7

        powers = [1] * (n + 1)
        prefix = [0]  * (n + 1)

        for i in range(n):
            powers[i + 1] = (powers[i] * base) % mod
            prefix[i + 1] = (prefix[i] * base + nums[i]) % mod 

        def check(length):
            counts = Counter()
            for start in range(n - length + 1):
                end = start + length
                h = (prefix[end] - prefix[start] * powers[length]) % mod
                counts[h] += 1
            return any(cnt == 1 for cnt in counts.values())

        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return ans