class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_sort=sorted(s)
        # t_sort=sorted(t)
        
        # return s_sort==t_sort
        # ---
        freq={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        
        for i in t:
            if i not in freq:
                return False
            else:
                freq[i]-=1
        
        for i in freq.values():
            if i!=0:
                return False
        return True
        

