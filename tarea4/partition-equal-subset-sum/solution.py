class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        suma_total = sum(nums)

        if suma_total % 2 != 0:
            return False

        objetivo = suma_total // 2

        dp = [False] * (objetivo + 1)
        dp[0] = True

        for numero in nums:
            for suma in range(objetivo, numero - 1, -1):
                if dp[suma - numero]:
                    dp[suma] = True

        return dp[objetivo]