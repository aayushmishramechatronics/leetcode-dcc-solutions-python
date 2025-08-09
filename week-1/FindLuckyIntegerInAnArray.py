from collections import Counter 
class Solution:
    def findLucky(self, arr):
        frequncy = Counter(arr)
        answr = -1
        for num, count in frequncy.items():
            if num == count:
                answr = max(answr, num)
        return answr
