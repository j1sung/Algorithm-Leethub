"""
author : Ahn Ji Sung
github : https://github.com/j1sung
e-mail : dalssagi00@gmail.com
title : two-sum
description : 반복문, 리스트
"""
#continue 사용시 
class Solution:
    def twoSum(
        self, nums: List[int], target: int
    ) -> List[int]:  # 함수의 매개변수에서 '콜론:'은 변수 타입에 대한 주석이며 코드 강제성은 없다
        output = []  # 함수 선언 "콜론:"사이에 "->(형식)"으로 쓰면 리턴값 권장 주석이며 강제성은 없다
        for i in range(len(nums)):  # 2, 7, 11, 15
            i_val = nums[i]
            for j in range(i, len(nums)):  # 2, 7, 11, 15
                if i == j:
                    continue
                j_val = nums[j]
                if i_val + j_val == target:
                    output.append(i)
                    output.append(j)
                    return output
                    
#만약 break를 쓴다면 다음이 효율적인 코드!                    
'''                    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            i_val = nums[i]
            for j in range(1, len(nums)):
                j_val = nums[j]
                if i == j:
                    break
                if i_val + j_val == target:
                    output.append(i)
                    output.append(j)
                    return output
'''										
										
