class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
         # Initialize max-heap with characters and their negative frequencies
        max_heap = []
        for freq, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if freq != 0:
                heappush(max_heap, (freq, char))

        result = []

        while max_heap:
            freq1, char1 = heappop(max_heap)

            # If last two characters are the same as the current one, choose the next most frequent character
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not max_heap:
                    break
                freq2, char2 = heappop(max_heap)
                result.append(char2)
                if freq2 + 1 < 0:
                    heappush(max_heap, (freq2 + 1, char2))
                heappush(max_heap, (freq1, char1))  # Push the first character back
            else:
                result.append(char1)
                if freq1 + 1 < 0:
                    heappush(max_heap, (freq1 + 1, char1))

        return ''.join(result)

# Example usage:
# solution = Solution()
# result = solution.longestDiverseString(a, b, c)        