from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count how many times each number appears
        # Counter does this in one line
        counts = Counter(nums)

        # most_common(k) returns the k most frequent items
        # as a list of (number, frequency) tuples, already sorted
        top_k = counts.most_common(k)

        # pull out just the numbers, drop the frequency counts
        return [num for num, freq in top_k]