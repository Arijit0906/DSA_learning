class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s =""
        for c in s:
            if c.isalnum():
                clean_s=clean_s+c

        clean_s=clean_s.lower()
        print(clean_s)
        i=0
        j=len(clean_s) - 1

        while i<j:
            if clean_s[i]!=clean_s[j]:
                return False
            
            i+=1
            j-=1
        return True
