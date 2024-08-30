class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        for i in range(len(nums) - 2):
            firstNum = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                secondNum  = nums[j]
                thirdNum = nums[k]

                potentialSum = firstNum + secondNum + thirdNum 
                if potentialSum > 0:
                    k -= 1
                elif potentialSum < 0:
                    j += 1
                else:
                    triplets.add((firstNum , secondNum ,thirdNum))
                    j += 1
                    k -= 1
        return triplets


        #second solution 


        class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res=[]
        nums.sort()

        length = len(nums)

        for i in range (length-2):
            if i >0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=length-1

            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if total<0:
                    l=L+1
                elif total >0:
                    r=r-1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l=l+1
                    while l<r and nums[r]==nums[r-1]:
                        r=r-1

                    l=l+1
                    r=r-1
        return res                            