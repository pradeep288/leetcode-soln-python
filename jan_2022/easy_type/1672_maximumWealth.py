class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        for account in range(len(accounts)):
            max_wealth = max(sum(accounts[account]), max_wealth)

        return max_wealth
