# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 08:37:55 2024

@author: priya
"""

class Solution:
    def dividePlayers(self, skill):
        skill.sort()
        n = len(skill)
        total_sum = skill[0] + skill[-1]
        chemistry_sum = 0
        
        # Try to form pairs with equal total skill
        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != total_sum:
                return -1
            chemistry_sum += skill[i] * skill[n - 1 - i]
        
        return chemistry_sum

# Example usage
# The following code is typically handled by the judge, but you can test it locally:
if __name__ == "__main__":
    solution = Solution()
    print(solution.dividePlayers([3, 2, 5, 1, 3, 4]))  # Output: 22
    print(solution.dividePlayers([3, 4]))              # Output: 12
    print(solution.dividePlayers([1, 1, 2, 3]))        # Output: -1