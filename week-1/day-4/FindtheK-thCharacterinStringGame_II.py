import math
class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        levels = math.ceil(math.log2(k))
        add_count = 0
        for i in range(levels - 1, -1, -1):
            half = 1 << i
            if k > half:
                k -= half
                add_count += operations[i]
        return chr(ord('a') + (add_count % 26))
