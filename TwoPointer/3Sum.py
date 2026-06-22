class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count_dict = {}
        for i,n in enumerate(nums):
            # print(i,n)
            count_dict[n]=i
        # print(count_dict)
        n=len(nums)
        a=set()
        for i in range(n):
            for j in range(i+1,n):
                req=-(nums[i]+nums[j])
                
                if req in count_dict and count_dict[req]!=i and count_dict[req]!=j: 
                    a.add(tuple(sorted([nums[i],nums[j],req])))
                    
        return list(a)
