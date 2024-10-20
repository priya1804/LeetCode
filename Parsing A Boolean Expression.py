# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 11:10:47 2024

@author: priya
"""

class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """

        # Helper function for DFS with memoization
        def dfs(s, e, memo):
            if (s, e) in memo:
                return memo[(s, e)]

            # Base case: single character (either 't' or 'f')
            if s == e:
                return expression[s] == 't'

            exps = []  # To store subexpressions
            layer = 0  # To track parentheses layers
            op = None  # To store the operator
            left = None  # To mark the beginning of a subexpression

            for i in range(s, e + 1):
                c = expression[i]

                if layer == 0 and c in '!&|':  # Identify the operator
                    op = c

                elif c == '(':  # Open parenthesis, start a subexpression
                    layer += 1
                    if layer == 1:
                        left = i + 1  # Mark the start of a subexpression

                elif c == ')':  # Close parenthesis, end the subexpression
                    layer -= 1
                    if layer == 0:
                        # Recursively process the subexpression
                        exps.append(dfs(left, i - 1, memo))

                elif c == ',' and layer == 1:
                    # Process subexpression between commas
                    exps.append(dfs(left, i - 1, memo))
                    left = i + 1

            # Apply the operator to the collected sub-expressions
            if op == '|':
                result = functools.reduce(operator.or_, exps)
            elif op == '&':
                result = functools.reduce(operator.and_, exps)
            elif op == '!':
                result = not exps[0]

            # Memoize the result
            memo[(s, e)] = result
            return result

        # Memoization dictionary
        memo = {}
        # Start DFS from the entire expression
        return dfs(0, len(expression) - 1, memo)


