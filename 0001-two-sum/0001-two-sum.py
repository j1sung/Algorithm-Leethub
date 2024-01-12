class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: #함수의 매개변수에서 '콜론:'은 변수 타입에 대한 주석이며 코드 강제성은 없다
        output = []
        for i in range(len(nums)): # 2, 7, 11, 15
            i_val=nums[i]
            for j in range(len(nums)): # 2, 7, 11, 15
                if i==j:
                    break
                j_val=nums[j]
                if i_val+j_val == target:
                    output.append(i)
                    output.append(j)
                    return output
                
2,7/2,11/ 2,15
7,11/7,15
11,15



       