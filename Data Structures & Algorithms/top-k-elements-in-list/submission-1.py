from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)

        # count each number's occurrences
        for num in nums:
            frequencies[num] += 1  # no need to check "if in" first

        # sort by frequency, highest first
        sorted_items = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

        # take top k, keep only the numbers
        return [num for num, freq in sorted_items[:k]]