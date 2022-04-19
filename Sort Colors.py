class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if nums==None or len(nums)==0:return 0
        a=0
        b=0
        c=0
    
        for i in range(len(nums)):
            if(nums[i]==0):
                a+=1
            elif(nums[i]==1):
                b+=1
            else:
                c+=1
        nums.clear()
        for j in range(a):
            nums.append(0)
        for j in range(b):
            nums.append(1)
        for j in range(c):
            nums.append(2)
        return nums
            
            