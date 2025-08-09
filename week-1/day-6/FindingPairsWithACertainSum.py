from collections import Counter
class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.count2 = Counter(nums2)
    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val
        self.count2[old_val] -= 1
        
        if self.count2[old_val] == 0:
            del self.count2[old_val]
        self.nums2[index] = new_val
        self.count2[new_val] += 1

    def count(self, tot: int) -> int:
        result = 0
        for a in self.nums1:
            target = tot - a
            result += self.count2.get(target, 0)
        return result
