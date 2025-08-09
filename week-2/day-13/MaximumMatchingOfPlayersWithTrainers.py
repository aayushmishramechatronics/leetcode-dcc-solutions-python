class Solution:
    def matchPlayersAndTrainers(self, p: List[int], t: List[int]) -> int:
        p.sort()
        t.sort()
        i=0
        j=0
        c=0
        while i<len(p) and j<len(t):
            if p[i]>t[j]:
                j+=1
            else:
                c+=1
                i+=1
                j+=1
        return c
